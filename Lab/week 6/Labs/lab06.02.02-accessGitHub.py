import requests
import json


# remove the minus signs/two symbols are missing for security reasons
# If the file had got “bad credentials” written in it. Then the key you are using is invalid
apiKey = '6-105ab6d-2a8001-8b65519-3e293-cb787544182-5'
url = 'https://api.github.com/repos/karolinaszafranbelzowska/RepKeyTest'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)