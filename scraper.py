from bs4 import BeautifulSoup
import requests
import csv

#Retrieves the source code from the given link using .get from requests
source = requests.get('https://en.wikipedia.org/wiki/Africa').text

#Parse our source code stored in the source variable using lxml parser
soup = BeautifulSoup(source, 'lxml')

#Store the title of the Wiki page for reference in title
title = soup.find('h1').text

#Opens a csv file called 'words_mode' and creates writer
with open('words_mode.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')

    # Clean text/Create word list/Write to .csv file
    for text in soup.find_all('body'):
        text = text.text
        text = list(text.split())

    csv_writer.writerow([text])

    #for word in text:
     #   csv_writer.writerow(word)

    #print(text)


    #for element in text:
     #   csv_writer.writerow(element)


