import datetime as dt
import requests

base_url= "http://api.openweathermap.org/data/2.5/weather?"
api_key= "Your API key"

def convert(kelvin):
    celsius= kelvin-273.15
    return celsius

while True:
    print("="*60)
    city= input("Enter the name of the city (Press 1 to exit): ")
    print("="*60)

    if city=="1":
        break
    else:
        url= base_url+"appid="+api_key+"&q="+city
        response= requests.get(url).json()

        temp_kelvin= response["main"]["temp"]
        temp_celsius= convert(temp_kelvin)
        feels_kelvin= response["main"]["feels_like"]
        feels_celsius= convert(feels_kelvin)
        humidity= response["main"]["humidity"]
        des= response["weather"][0]["description"]

        print(f"Temperature in {city}: {temp_celsius:.2f}°C")
        print(f"Temperature in {city} feels like: {feels_celsius:.2f}°C")
        print(f"Humidity in {city}: {humidity}%")
        print(f"General weather in {city}: {des}")