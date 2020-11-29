import requests
import json
from xlwt import *

# Lab 06.01.01
#  Write a python program that will get all the cars from the server (using the API).
#  The program should output the returned json to the screen.

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

#output to console
print (data) #  The program should output the returned json to the screen

# ======================================================================================

# The program should output all the cars individually to the screen.
 
for car in data["cars"]:
    print (car)

# ======================================================================================

# The program should write the returned JSON neatly to a file.

#save this to a file
filename = 'cars.json'
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# to print in command prompt:
# python lab06.01.01-getJSON.py
# cat cars.json
# ======================================================================================

# The program should write the cars to an EXCEL file

w = Workbook()
ws = w.add_sheet('cars')
row = 0;
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1 
for car in data["cars"]:
    ws.write(row,0, car["reg"])
    ws.write(row,1,car["make"])
    ws.write(row,2,car["model"])
    ws.write(row,3,car["price"])
    row += 1

w.save('cars.xls')


