# Write a python program that will read in a html page from a file and prints it out again 

import requests
import json

#html = '<h1>hello world</h1>This is html'
f = open("carviewer2.html", "r")
html = f.read()
print (html)

# ============================================================================================

# Modify the script to use the html2pdf.app api with the key:
# 46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad
# 6d4f1c4. The script should print out the status code of the response

# remove the minus signs
# apiKey = '4-6ceed91-0c24ff7cce82-40e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
# url = 'https://api.html2pdf.app/v1/generate'

# data = {'html': html,'apiKey': apiKey}
# response = requests.post(url, json=data)
# print (response.status_code)

# newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
# newFile.write(response.content)

