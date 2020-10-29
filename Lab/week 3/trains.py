# Write a program that stores stores the data for all trains in Ireland in a csv file
# Use the Irish rail API
# http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML
# to retrive the data

# This program gets all the trains that are located south of Dublin
# and stores the data associated with them 


import requests
import csv
from bs4 import BeautifulSoup


url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')
# When I ask to print this XML it will print all the trains in Ireland in that day.

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

with  open('train.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    listings = soup.findAll("objTrainPositions")

    for listing in listings:
        # print(listing) # It will print all the trains ahich are listed in nicer way
        # print(listing.TrainLatitude.string) # It will print all the trains but their Latitude
        # or
        # print(listing.find('TrainLatitude').string)
        lat = float( listing.TrainLatitude.string) # I am going to store trains that are South of Dublin
        if (lat < 53.4): # Approx. 53.4


            entryList = []
            for retrieveTag in retrieveTags:
                print(listing.find(retrieveTag).string)
                entryList.append(listing.find(retrieveTag).string)
            train_writer.writerow(entryList)

            

# print(soup.prettify())