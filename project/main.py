import requests
import pandas as pd
import os
api_key=os.getenv('OPENWEATHER_API_KEY')
print(api_key)
print("here")
response=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=Cairo&appid={'045a61058bcc8f4d71665879b41828a3'}&units=metric")
print(response.status_code)  # Output: 200
print(response.json())  # Output: JSON response from the API
output=response.json()
# mycsv=pd.DataFrame(output)
# print(mycsv)

# api_key = '045a61058bcc8f4d71665879b41828a3'
#export OPENWEATHER_API_KEY='045a61058bcc8f4d71665879b41828a3'