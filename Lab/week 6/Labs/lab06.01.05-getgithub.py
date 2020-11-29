import requests, json 
from xlwt import *

def getJSONFromUrl(url):
    response = requests.get(url)
    data = response.json()
    return data

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

data = getJSONFromUrl(url)
#print (data)
#Get the file name for the new file to write

filename = 'githubusers.json'

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

w = Workbook()
ws = w.add_sheet('github followers')
row = 0
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
row += 1

for user in data:
    ws.write(row,0,user["login"])
    ws.write(row,1,user["id"])
    ws.write(row,2,user["node_id"])
    ws.write(row,3,user["avatar_url"])
    row += 1

w.save('users.xls')

# to print in command prompt:
# python lab06.01.05-getgithub.py
# cat githubusers.json