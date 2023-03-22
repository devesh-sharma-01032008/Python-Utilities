"""
Json module is used to parse string into dictionary in python.
Requests is used to get content from newsapi and weatherapi
Colors is custom module used to add colors in this project
Api_Keys contain the secret api keys to access newsapi and weatherapi

"""
from os import system
import sys
from utils.convert_pdf_to_mp3 import save_pdf_file_as_txt,save_txt_file_as_mp3,play_music
# Installing required module to use the app
try:
    system("pip install -r requirements.txt") # may give error if requirements.txt not exists
    system("clear") # may give error in windows
except Exception as e:
    system("cls")
    system("pip install requests") # installing request module

from utils import api_keys
import requests
import json
from utils.colors import *
import wikipedia as wiki
from time import sleep


# Url for news api
news_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_keys.news_api


# Location Class to locate weather in region
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def user_manual():
        purple()
        print("Type the following to get desired result")
        blue()
        print("1 - To type the latitude or longitude")
        red()
        print("Note : Might throught Exception if coordintates are not correct")
        blue()
        print("2 - To type the city name")
        red()
        print("Note : Only valid city name is supported. Wrong city name throws an error")
        blue()
        print("3 - To automatically detect location using GPS( Google play services)")
        red()
        print("Note : Only tested for linux system")
        reset()

    def get_weather(self):
        weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={api_keys.weather_api}"
        weather_data = requests.get(weather_api_url).text
        weather_obj = (json.loads(weather_data))
        blue()
        print("Weather Conditions : ",weather_obj.get('weather')[0].get('main'))
        print("Weather Description : ",weather_obj.get('weather')[0].get('description'))
        red()
        print("Temerature : ",float(weather_obj['main']['temp'])-273,"C")
        print("Temerature Feels Like : ",float(weather_obj['main']['feels_like'])-273,"C")
        print("Maximum Temerature : ",float(weather_obj['main']['temp_max'])-273,"C")
        print("Pressure : ",weather_obj['main']['pressure'],"atm")
        print("Humidity : ",weather_obj['main']['humidity'],"%")
        purple()
        print("Country : ",weather_obj.get('sys').get('country'))
        print("Sun Rise : ",weather_obj['sys']['sunrise'],"seconds")
        print("Sun Set : ",weather_obj['sys']['sunset'],"seconds")
        print("Time Zone : ",weather_obj['timezone'],"seconds")
        yellow()
        print("Coordinates : ",weather_obj.get('coord'))
    @staticmethod
    def get_weather_by_city(city):
        weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_keys.weather_api}"
        weather_details = json.loads(requests.get(weather_api_url).text)
        lat = weather_details.get("coord").get("lat")
        lon = weather_details.get("coord").get("lon")
        coordinates = Location(lat,lon)
        coordinates.get_weather()

    @staticmethod
    def detect_location():
        system("curl ipinfo.io/loc > coordinates.txt")
        coordinate = open("coordinates.txt","r").read()
        sep = coordinate.find(",")
        location = Location(coordinate[0:sep],coordinate[sep+1:len(coordinate)-1])
        location.get_weather()
        system("rm coordinates.txt")

# News class for making news objects
class News:
    def __init__(self, title, information, date, author):
        self.title = title
        self.information = information
        self.date = date
        self.author = author

    @staticmethod
    def user_manual():
        green()
        print("Red denotes the title")
        print("Blue denotes the clue")
        print("Yellow denotes the published time")
        print("Purple denotes the Author name")

# send request to url amd get data as string
def get_news_str(url):
    news = requests.get(url)
    return news.text

# gets the news and parse it into dictionary then show it in the terminal
def get_news(url):
    news_json = json.loads(get_news_str(url))
    articles = news_json['articles']
    for news in articles:
        author = news['author']
        title = news['title']
        desc = news['description']
        time = news['publishedAt']
        read_more = news['url']
        news_obj = News(title,desc,time,author)
        red()
        print("Title : ",news_obj.title)
        blue()
        print("Hint : ",news_obj.information)
        yellow()
        print("Date : ",news_obj.date)
        purple()
        print("Author : ",news_obj.author)
        green()
        print("Read More at :", read_more)
        print()

def search_wiki(topic):
    try:
        blue()
        about = wiki.summary(topic)
        print(about)
    except Exception as e:
        results = wiki.search(topic)
        red()
        print("Sorry, No results found. Possible searches may be")
        purple()
        for suggestion in results:
            print(suggestion)

# Basic app class contain the guide for using app
class App:
    @staticmethod
    def user_manual():
        system("clear")
        purple()
        print("Type the following to get desired result")
        blue()
        print("1 - for the temperature of your localiy by using latitude , longitude or city name")
        print("2 - for the news about the india")
        print("3 - for the wikipedia search for articles")
        print("4 - to convert pdf file to text file")
        print("5 - to convert pdf file to mp3 file")
        print("6 - to convert pdf file to mp3 and play it.")
        print("q - to exit the program")
        reset()

def delete_last_line():
	sys.stdout.write("\x1b[2K")

# To make it usable in other files without showing the actual file prompt in the terminal
if __name__ == "__main__":
    App.user_manual()
    user_aim = input("Select from options : ")
    if user_aim == "q":
        yellow()
        print("Thank you for using the program")

    elif user_aim == "1":
        Location.user_manual()
        location_choice = input("Select from options : ")
        if location_choice == "1":
            latitude = input("Enter Latitude : ")
            longitude = input("Enter Longitude : ")
            location = Location(latitude, longitude)
            location.get_weather()

        elif location_choice == "2":
            city = input("Enter City name : ")
            Location.get_weather_by_city(city);

        elif location_choice == "3":
            Location.detect_location()

        else:
            red()
            print("Select a correct option")

    elif user_aim == "2":
        News.user_manual()
        get_news(news_url)

    elif user_aim == "3":
        topic = input("Enter topic to search : ")
        search_wiki(topic)

    elif user_aim == "4":
        filename = input("Enter pdf file name to convert into text file : ")
        save_pdf_file_as_txt(filename)
    elif user_aim == "5":
        filename = input("Enter pdf file name to convert into mp3 file : ")
        save_pdf_file_as_txt(filename)
        save_txt_file_as_mp3(filename.split(".")[0]+".txt")
    elif user_aim == "6":
        filename = input("Enter pdf file name to convert into mp3 file  and play it: ")
        save_pdf_file_as_txt(filename)
        save_txt_file_as_mp3(filename.split(".")[0]+".txt")
        play_music(filename.split(".")[0]+".mp3")
    else:
        red()
        print("Select a correct option")
        reset()

    red()
    for  i in range(2):
        print("Exiting program in "+str(3-i),end="\r")
        sleep(1)

    delete_last_line()
    blue()
    print("\nProgram Ended Successfully")
    reset()


