# Modify the script to use the html2pdf.app api with the key:
# The script should print out the status code of the response

import requests
import json

f = open('carviewer2.html', 'r')
html = f.read()
#print(html)

# remove the minus signs
apiKey = '4-6ceed91-0c24ff7cce82-40e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html' : html, 'apiKey': apiKey }

response = requests.post(url, json=data)
print(response.status_code)