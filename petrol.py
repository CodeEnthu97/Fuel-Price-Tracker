import requests
from bs4 import BeautifulSoup


place=input()
y=input()
z=place.replace(" ","-")

if y=="state":
  html_data=requests.get("https://www.ndtv.com/fuel-prices/diesel-price-in-"+z+"-state")
  beautify=BeautifulSoup(html_data.text,'html.parser')
  info_div=beautify.find("div",class_="tb-bar")

  print(info_div.get_text())
 
else:
  html_data=requests.get("https://www.ndtv.com/fuel-prices/diesel-price-in-"+z+"-city")
  beautify=BeautifulSoup(html_data.text,'html.parser')
  info_div=beautify.find("div",class_="tb-bar")

  print(info_div.get_text()) 
