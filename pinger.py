import requests
import time
from datetime import datetime

from bs4 import BeautifulSoup
from extract_unit_links import all_unit_links

with open("logs/ping_results.json", "w", 1, "utf-8") as file:
    file.write("")

## Ping all unit links, to make sure the links are working 
for element in all_unit_links:

    current_time = datetime.now()
    
    try:
        is_up = requests.get(element).status_code == 200
        with open("logs/ping_results.json", "a", 1, "utf-8") as file:
            file.write(f"URL at {element} was successfully pinged at {current_time}\n")

    except:
        with open("logs/ping_results.json", "a", 1, "utf-8") as file:
            file.write(f"!!! ERROR at {element}! Was UNSUCCESSFULLY pinged at {current_time}\n")

    time.sleep(1)
