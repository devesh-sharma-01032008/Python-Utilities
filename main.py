"""
Json module is used to parse string into dictionary in python.
Requests is used to get content from newsapi and weatherapi
Colors is custom module used to add colors in this project
Api_Keys contain the secret api keys to access newsapi and weatherapi

"""
from os import system

# Installing required module to use the app
try:
    system("pip install -r requirements.txt") # may give error if requirements.txt not exists
except Exception as e:
    system("pip install requests") # installing reqiest module


import api_keys
import requests
import json
from colors import *

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
        print("2 - To type the city name")
        print("3 - To automatically detect location using GPS( Google play services)")
        reset()

    def get_location(self):
        pass

    @staticmethod
    def get_location_by_city():
        pass

    @staticmethod
    def detect_location():
        pass

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
        print(news_obj.title)
        blue()
        print(news_obj.information)
        yellow()
        print(news_obj.date)
        purple()
        print(news_obj.author)
        red()
        print("Read More at :", read_more)
        print()

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
        print("q - to exit the program")
        reset()

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
            latitude = int(input("Enter Latitude : "))
            longitude = int(input("Enter Longitude : "))
            location = Location(latitude, longitude)
            location.get_location()

        elif location_choice == "2":
            city = input("Enter City name : ")
            Location.get_location_by_city();

        elif location_choice == "3":
            print("Detecting the location....")
            Location.detect_location()

        else:
            red()
            print("Select a correct option")

    elif user_aim == "2":
        News.user_manual()
        get_news(news_url)

    elif user_aim == "3":
        pass

    else:
        red()
        print("Select a correct option")
        reset()

    reset()
    print("Hello Devesh")
