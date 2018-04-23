import requests
from bs4 import BeautifulSoup
import pandas

# load first page
r = requests.get("https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS")
c = r.content
soup = BeautifulSoup(c, "html.parser")
# page numbers
page_num = soup.find_all("a", {"class": "Page"})[-1].text
print(page_num)
# define a list and base URL
l = [ ]
base_url = "https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
# loop all pages
for page in range(0, int(page_num)*10, 10):

    # load a webpage
    r = requests.get ( base_url + str ( page ) + ".html")
    c = r.content
    soup=BeautifulSoup(c , "html.parser")
    # print(soup.prettify())

    # for the first item in list use the find method or the [0] item
    all = soup.find_all("div",{"class":"propertyRow"})

    #print(all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    for item in all:
        d={}
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["Locality" ]=item.find_all("span",{"class":"propAddressCollapse"})[1].text

    # for infoBed if the answer is None so .text will lead to an error, so using try and except can help!
        try:
            d["Bed"] = item.find("span", {"class": "infoBed"}).find("b").text
        except:
            d["Bed"] = None  # pass or print(None)
        try:
            d["Area"] = item.find("span", {"class": "infSqFt"}).find("b").text
        except:
            d["Area"] = None
        try:
            d["Full Bath"] = item.find("span", {"class": "infoValueFullBath"}).find("b").text
        except:
            d["Full Bath"] = None
        try:
            d["Half Bed"] = item.find("span", {"class": "infoValueHalfBath"}).find("b").text
        except:
            d["Half Bed"] = None
        try:
            for columnGroup in item.find_all("div",{"class":"columnGroup"}):
                #print(columnGroup)
                for featureGroup, featureName in zip(columnGroup.find_all("span",{"class":"featureGroup"}),columnGroup.find_all("span",{"class":"featureName"})):
                    #if featureGroup.text == "Lot Size":
                        if "Lot Size" in featureGroup.text:
                            d["Lot Size"] = featureName.text

        except:
            d["Lot Size"] = None

        l.append(d)

    # define data frame
df=pandas.DataFrame(l)
df.to_csv("out.csv")

