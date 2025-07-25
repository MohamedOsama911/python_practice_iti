import os
from helper import *
from sqliteWeatherDb import *
import schedule
import time
#api_key=os.getenv('OPENWEATHER_API_KEY')
weatherKey='045a61058bcc8f4d71665879b41828a3' #for testing purposes only, do not use in production
cities = [
    "Cairo", "Giza", "Alexandria", "Port Said", "Suez", "Luxor", "Aswan", "Asyut",
    "Damanhur", "Beni Suef", "Mansoura", "Damietta", "Faiyum", "Tanta", "Ismailia",
    "Kafr El Sheikh", "Mersa Matruh", "Minya", "Shibin El Kom", "Kharga", "Arish",
    "Banha", "Qena", "Hurghada", "Zagazig", "Sohag", "El Tor"
]

createDb('weather_db')
def job():
    print("Fetching weather data...")
    temps = getWeather(apiKey=weatherKey, cities=cities)
    insertWeatherData("weather_db", temps)
    #plotWeather(temps)
    schedule.every().hour.do(job)

try:
    while True:
        schedule.run_pending()
        time.sleep(60)
except Exception as e:
    print(f"error occurred {e}")
