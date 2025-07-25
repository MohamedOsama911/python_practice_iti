import matplotlib.pyplot as plt
import requests

def plotWeather(weather_data:dict)->None:
    cities = list(weather_data.keys())
    temperatures = list(weather_data.values())

    plt.plot(cities, temperatures, marker='o')  # Line with points
    plt.xticks(rotation=90)
    plt.ylabel("Temperature (°C)")
    plt.title("City Temperatures")
    #plt.grid(True)
    #plt.tight_layout()
    plt.show()

def getWeather(apiKey:str, cities:list)->None:
    temps={}
    for city in cities:
        try:
            response=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric")
            output=response.json()
            print(output['main']['temp'])
            print(output['name'])
            temps[city]=float(output['main']['temp'])
        except Exception as e:
            print(f"error occurred {e}")
    return temps