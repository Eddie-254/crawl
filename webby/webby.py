import re # regex
import urllib.request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opeming up connection, grabbing the page
uClient = uReq(my_url) 
 kurasa = uClient.read()
 uClient.close()
#html parsing 
 page_soup = soup(kurasa, "html.parser")

 #grabs each product
 containers = page_soup.findAll("div",{"class":"item-container"})

 for container in containers:
     brand_container = container.find_all("a",{"class":"item-brand"})
brand_name = brand_container[0].img["title"]
