import bs4
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = "https://hailvarsity.com/nebraska-football/roster"

uClient = uReq(my_url) #opens conn and parses page into var
page_html = uClient.read() #reads page into var
uClient.close() #closes conn

#parse HTML into page_soup var
page_soup = soup(page_html, "html.parser")

#find the class that has the roster table data
players = page_soup.findAll("div", {"class":"row"})

filename = "2017roster.csv"
f = open(filename, "w")

headers = "number, player_name, position, mug_url, year\n"

f.write(headers)

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

    print("number: " + number)
    print("name: " + name)
    print("position: " + position)
    print("photo_url: " + photo_url)
    print("year: " + year)

    f.write(number + "," + name + "," + position + "," + photo_url + "," + year + "\n")

f.close()
