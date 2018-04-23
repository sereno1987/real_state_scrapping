#
import requests
from bs4 import BeautifulSoup

# load a webpage
r = requests.get ( "https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content
soup=BeautifulSoup(c , "html.parser")
# print(soup.prettify())

# for the first item in list use the find method or the [0] item
all = soup.find_all("div",{"class":"propertyRow"})
#print(all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
for item in all:
    try:
        print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
        print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
        print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    except:
        pass
        # for infoBed if the answer is None so .text will lead to an error, so using try and except can help!
    try:
        print(item.find("span", {"class": "infoBed"}).find("b").text)
    except:
        print(None) # pass
    try:
        print(item.find("span", {"class": "infSqFt"}).find("b").text)
    except:
        print ( None )
    try:
        print(item.find("span", {"class": "infoValueFullBath"}).find("b").text)
    except:
        print(None)
    try:
        print(item.find("span", {"class": "infoValueHalfBath"}).find("b").text)
    except:
        print ( None )
    try:
        for columnGroup in item.find_all("div",{"class":"columnGroup"}):
            #print(columnGroup)
            for featureGroup, featureName in zip(columnGroup.find_all("span",{"class":"featureGroup"}),columnGroup.find_all("span",{"class":"featureName"})):
                #if featureGroup.text == "Lot Size":
                    if "Lot Size" in featureGroup.text:
                        print(featureName.text)

    except:
        print(None)

    print(" ")
