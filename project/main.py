import pandas as pd
import os
from helper import *
from sqliteWeatherDb import *
#api_key=os.getenv('OPENWEATHER_API_KEY')
weatherKey='045a61058bcc8f4d71665879b41828a3'
cities = [
    "Cairo", "Giza", "Alexandria", "Port Said", "Suez", "Luxor", "Aswan", "Asyut",
    "Damanhur", "Beni Suef", "Mansoura", "Damietta", "Faiyum", "Tanta", "Ismailia",
    "Kafr El Sheikh", "Mersa Matruh", "Minya", "Shibin El Kom", "Kharga", "Arish",
    "Banha", "Qena", "Hurghada", "Zagazig", "Sohag", "El Tor"
]
temps=getWeather(apiKey=weatherKey,cities=cities)

for temp in temps:
    print(temp)
    print("*"*10)
print(temps)
#plotWeather(temps)
createDb('weather_db')
#temps={'Cairo': 28.42, 'Giza': 28.41, 'Alexandria': 26.86, 'Port Said': 27.84, 'Suez': 27.19, 'Luxor': 31.92, 'Aswan': 32.01, 'Asyut': 30.44, 'Damanhur': 24.54, 'Beni Suef': 29.17, 'Mansoura': 20.79, 'Damietta': 26.98, 'Faiyum': 28.56, 'Tanta': 25.85, 'Ismailia': 26.75, 'Mersa Matruh': 24.58, 'Minya': 30.23, 'Arish': 25.99, 'Banha': 27.28, 'Qena': 31.75, 'Hurghada': 32.7, 'Zagazig': 27.3, 'Sohag': 30.75}
insertWeatherData("weather_db",temps)