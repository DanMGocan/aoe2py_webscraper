from os import error

import json
import requests
import re
import time

from bs4 import BeautifulSoup

from all_links import links_units
import helper_functions


all_units = []

# Can be used to scrape regular units, does not work for castle
link_allunits = "https://ageofempires.fandom.com/wiki/Units_(Age_of_Empires_II)"
req_allunits = requests.get(link_allunits)
soup_allunits = BeautifulSoup(req_allunits.content, "html.parser")
allunits = soup_allunits.find_all(attrs={
    "href": re.compile("/wiki")#,
    #"title": re.compile("(Age of Empires II)")
})

# Scraping units from the Infantry page
#link_allinf = "https://ageofempires.fandom.com/wiki/Infantry_units_(Age_of_Empires_II)"
#req_allinf = requests.get(link_allinf)
#soup_allinf = BeautifulSoup(req_allinf.content, "html.parser")
#allunits = soup_allunits.find_all(attrs={
#    "href": re.compile("/wiki")
#})

# Scraping units by building 
link_barracks = "https://ageofempires.fandom.com/wiki/Throwing_Axeman_(Age_of_Empires_II)"
req_barracks = requests.get(link_barracks)
soup_barracks = BeautifulSoup(req_barracks.content, "html.parser")
#all_barracks_tables = soup_barracks.find_all(attrs={
#    "class": "article-table"
#})
#all_barracks = all_barracks_tables[1]

table = soup_barracks.find("aside")
with open("taxeman.html", "a", 1, "utf-8") as file:
        file.write(str(table))

list_of_lists = requests.get("https://ageofempires.fandom.com/wiki/Category:Lists")
list_of_lists_bs = BeautifulSoup(list_of_lists.content, "html.parser")


def data_extractor(link):

    # Creating the request and the BS object
    new_request = requests.get(link)
    soup = BeautifulSoup(new_request.content, "html.parser")

    # Gathering all the attributes of a unit 
    unit_name = soup.h2.string
    unit_type = helper_functions.find_type(soup)
    unit_civ = soup.find(attrs={"data-source": "Civilization"}).div.a.find_next("a").string
    unit_age = soup.find(attrs={"data-source": "Age"}).div.a.find_next("a").string
    unit_cost = helper_functions.find_cost(soup)
    unit_training_time = helper_functions.find_training_time(soup)
    unit_hitpoints = soup.find(attrs={"data-source": "HP"}).div.string


    # Create the dictionary with all the information requested
    dict_to_add = {
        "name": unit_name,
        "type": unit_type,
        "civilization": unit_civ,
        "age": unit_age,
        "cost": unit_cost,
        "training time": unit_training_time,
        "hit points": unit_hitpoints
    }

    json_dict = json.dumps(dict_to_add, indent=4)
    all_units.append(f"{json_dict}, \n")
    

for element in links_units:
    data_extractor(element)
    time.sleep(1)
    

    


with open("test_file.json", "w", 1, "utf-8") as file:
    for element in all_units:
        file.write(f"{element} \n")

#print(list_of_lists.content)
#print(list_of_lists_bs)

#print(allunits)

#table_new = soup_new.find_all("aside")