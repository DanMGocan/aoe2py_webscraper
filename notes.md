### Notes taken from Codecademy tutorial on Beautiful Soup 

BeautifulSoup breaks the HTML into different types of objects. 
- Based on tag (print(soup.div)) # will print the first div on the page
    print(soup.div.name) # will print name of tag
    print(soup.div.attrs) # will print a dictionary with all attributes 
    print(soup.div.string) # will print the content of the div

## Navigating the tags 
    for child in soup.li.children:  
        print(child) # will print all children under those tags 

    for parent in soup.li.parents:
        # will do the same, but with parent tags, going up all the way to <html>

### Find All
    if we want to find all the occurences of a tag, we can use
        print(soup.find_all("h1"))
    # this will return a list

    find_all() can take a list as imput such as:
        soup.find_all(["h1", "p", "div"])

    ## Using RegEx
    
    import re
    soup.find_all(re.compile("h[1-9]")) # this will return all the h tags

    ## Using attributes

    soup.find_all(attrs={"class": "banner", "id": "jumbotron"})