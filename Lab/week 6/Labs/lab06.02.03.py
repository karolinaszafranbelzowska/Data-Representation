# Modify the program to write the binary data returned to a file .pdf

import requests
import json

f = open('carviewer2.html', 'r')
html = f.read()
#print(html)

apiKey = '4-6ceed91-0c24ff7cce82-40e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html' : html, 'apiKey': apiKey }

response = requests.post(url, json=data)
print(response.status_code)

newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)