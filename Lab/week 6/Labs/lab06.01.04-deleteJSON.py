# Write a python program that deletes a car from the server using the API.

import requests

url = 'http://127.0.0.1:5000/cars/08%20C%201234'
response = requests.delete(url)
print (response.status_code)
print (response.text)