import bs4
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = "./" + path + "/" + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

#json file write
path = "./"
fileName = "2017roster"

my_url = "https://hailvarsity.com/nebraska-football/roster"

uClient = uReq(my_url) #opens conn and parses page into var
page_html = uClient.read() #reads page into var
uClient.close() #closes conn

#parse HTML into page_soup var
page_soup = soup(page_html, "html.parser")

#find the class that has the roster table data
players = page_soup.findAll("div", {"class":"row"})

#loop over each row to find player data
for player in players:
    number_tag = player.find("div", class_="number")
    number = number_tag.text.strip()

    name_tag = player.find("div", class_="name")
    name = name_tag.contents[1].text

    position_tag = player.find("div", class_="position")
    position = position_tag.text.strip()

    photo_div = player.find("img", class_="mug")
    photo_url = photo_div["src"]

    year = player.find("span", class_="class-long").text

    data = {"number":number, "name":name, "position":position, "mug_url":photo_url,"year":year}

    writeToJSONFile(path, fileName, data)
