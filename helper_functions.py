from os import error
from bs4 import BeautifulSoup

# Function to find the type of a unit when more than one type is given
def find_type(param):
    types = []
    all_anchors = param.find(attrs={"data-source": "Type"}).div.find_all("a")
    for element in all_anchors: # function to return a list, even if one element to preserve data integrity
        types.append(element.string)
    return types


# Function to create a dictionary from the Training section, with all the buildings
def find_training_time(param):
    # Taking all buildings
    all_buildings = []
    all_training_times = []

    for element in param.find(attrs={"data-source": "Building"}).div.find_all("a"):
        if element.string:
            all_buildings.append(element.get_text())

    for element in param.find(attrs={"data-source": "TrainTime"}).div.find_all("span"):
        if element.string:
            all_training_times.append(element.get_text())

    new_dict = dict(zip(all_buildings, all_training_times))

    return new_dict

# Function to find the costs in resources for units
def find_cost(param):
    new_dict = {}
    for resource in ["Food", "Wood", "Gold", "Stone"]:
        try:
            new_dict[resource] = param.find(attrs={"data-source": f"{resource}"}).div.string
        except:
            new_dict[resource] = 0
    return new_dict

