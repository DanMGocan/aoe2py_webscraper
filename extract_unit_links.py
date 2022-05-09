import requests
import time

from bs4 import BeautifulSoup

exceptions = [
                "/wiki/Supplies", 
                "/wiki/Squires", 
                "/wiki/Arson",
                "/wiki/Husbandry",
                "/wiki/Bloodlines",
                "/wiki/Thumb_Ring",
                "/wiki/Parthian_Tactics",
                "/wiki/Dark_Age_(Age_of_Empires_II)",
                "/wiki/Feudal_Age_(Age_of_Empires_II)", 
                "/wiki/Castle_Age_(Age_of_Empires_II)",
                "/wiki/Imperial_Age_(Age_of_Empires_II)",
                "/wiki/Gillnets",
                "/wiki/Careening",
                "/wiki/Dry_Dock",
                "/wiki/Shipwright" 
]

links = [
        "https://ageofempires.fandom.com/wiki/Barracks_(Age_of_Empires_II)",
        "https://ageofempires.fandom.com/wiki/Stable_(Age_of_Empires_II)",
        "https://ageofempires.fandom.com/wiki/Archery_Range_(Age_of_Empires_II)",
        "https://ageofempires.fandom.com/wiki/Siege_Workshop_(Age_of_Empires_II)",
        "https://ageofempires.fandom.com/wiki/Dock_(Age_of_Empires_II)"
]


def units_extractor(links, exceptions):

    all_units = ["https://www.asdaswunsiejoadasdkasd.com"]

    for link in links:

        # Creating the request and the BS object
        new_request = requests.get(link)
        soup = BeautifulSoup(new_request.content, "html.parser")

        # Gathering all the attributes of a unit
        result = soup.find_all("table", {"class" : "article-table"})
        
        for element in result:
            for index, i in enumerate(element):
                for index, j in enumerate(i):
                    for index, k in enumerate(j):
                        try:
                            unit_link = k.find("a")["href"]
                            unit_full_link = f'https://ageofempires.fandom.com{unit_link}'
                            if unit_link not in exceptions and unit_full_link not in all_units:
                                all_units.append(unit_full_link)
                        except:
                            pass

        time.sleep(1)
    
    return all_units

all_unit_links = units_extractor(links, exceptions)