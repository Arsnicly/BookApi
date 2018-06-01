import json
from pprint import pprint
import requests



def search_for_json():
    search = input('What do you want to search for: ')
    print ("")
    
    link = "https://www.googleapis.com/books/v1/volumes?q="+search
    f = requests.get(link)
    json_string = (f.text)
    
    text_file = open("Output.json", "w", encoding = 'utf-8')
    text_file.write(json_string)
    text_file.close()
    
    return(json.load(open('Output.json', encoding = 'utf-8')))

#def extract_data_to_dict():


  

data = search_for_json()

results = int(input("How many results do you want to print (1-10): "))

print ("")

title = "blank"
isbn_type = "blank"
isbn_num = "blank"
isbn_num_clean = "blank"
publisher = "blank"
author = "blank"
date = "blank"
date_flipped = "blank"
image_url = "blank"
price = "blank"


for x in range(results):


    #Extracts each bit of data from the json file
    #TITLE EXTRACT
    title = data["items"][x]["volumeInfo"]["title"]

    #The json file puts isbn 10 and 13 in random order need if to workout which to print
    #ISBN EXTRACT
    try:
        if ((data["items"][x]["volumeInfo"]["industryIdentifiers"][0]["type"]) == "ISBN_13"):
            isbn_type = data["items"][x]["volumeInfo"]["industryIdentifiers"][0]["type"]
            isbn_num = data["items"][x]["volumeInfo"]["industryIdentifiers"][0]["identifier"]
        elif ((data["items"][x]["volumeInfo"]["industryIdentifiers"][0]["type"]) == "ISBN_10"):
            isbn_type = data["items"][x]["volumeInfo"]["industryIdentifiers"][1]["type"]
            isbn_num = data["items"][x]["volumeInfo"]["industryIdentifiers"][1]["identifier"]
        else:
            isbn_num = "NO ISBN NUMBER"
    except (KeyError):
        isbn_num = 'this is a bug';
    
    #AUTHOR EXTRACT
    try:
        author = data["items"][x]["volumeInfo"]["authors"]
    except KeyError:
        pass

    #PUBLISHER EXTRACT
    try:
        publisher = data["items"][x]["volumeInfo"]["publisher"]
    except KeyError:
        pass
    
    date = data["items"][x]["volumeInfo"]["publishedDate"]

    if(data["items"][x]["saleInfo"]["saleability"]=="FOR_SALE"):
        price = '$'+str(data["items"][x]["saleInfo"]["listPrice"]["amount"])
    else:
        price = "NOT_FOR_SALE"
    
    title = data["items"][x]["volumeInfo"]["title"]

    #changes formatting of data that is in the incorrect format
    if isbn_num != "NO ISBN NUMBER":
        isbn_num_clean = isbn_num[:3] + '-' + isbn_num[3:]
    else:
        isbn_num_clean = isbn_num
    if (len(date) == 4):
        date_flipped = date
    elif (len(date) == 7):
        date_flipped = date[-2:]+'/'+date[:4]
    else:
        date_flipped = date[-2:]+'/'+date[5:-3]+'/'+date[:4]
    
    #prints the final formatted information
    print(title)
    print(isbn_type+": "+isbn_num_clean)
    print(author)
    print(publisher+": "+date_flipped)
    print(price)
    print("")

input ("Press enter to exit")



