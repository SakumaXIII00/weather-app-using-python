# few modules need to be included
# pip install beautifulsoup4
# pip install pillow
# pip install requests

import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

# weather url 
# orlando base location
url = "https://weather.com/weather/today/l/44290b42d653f3161cc4c1de02e397e6d0009fdc48676d3702e16b1aad8dfbd3"

# GUI
master = Tk()
master.title("weather App")
master.config(bg = "white")

# Img for GUI
img = Image.open("C:/Users/Sakuma/Desktop/Python/GitHub/Weather.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

# using Web Scraper to get content
def  get_weather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1',class_="CurrentConditions--location--2_osB").text
    temperature = soup.find('span',class_="CurrentConditions--tempValue--1RYJJ").text
    weatherPredication = soup.find('div',class_="CurrentConditions--phraseValue--17s79").text
    #print(location)
    #print(temperature)
    #print(weatherPredication)

    # text for GUI
    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredicationLabel.config(text=weatherPredication)

    # After 1 minutes update
    temperatureLabel.after(60000,get_weather)
    master.update()

# Label for GUI
locationLabel = Label(master,font=("Calibri bold",20),bg="white")
locationLabel.grid(row=0,sticky="N",padx=100)
temperatureLabel = Label(master,font=("Calibri bold",70),bg="white")
temperatureLabel.grid(row=1,sticky="W",padx=40)
Label(master, image=img,bg="white").grid(row=1,sticky="E")
weatherPredicationLabel = Label(master,font=("calibri bold",15),bg="white")
weatherPredicationLabel.grid(row=2,sticky="W",padx=40)

get_weather()
master.mainloop()