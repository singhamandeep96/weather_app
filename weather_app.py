import requests
API_KEY= "86fe007f829e671851f43e3008f4bc46"
Base_URL= "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name:str):
    params= {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    response=requests.get(Base_URL, params=params)

    response.raise_for_status

    data= response.json()
    return data

def main():
    print("====Simple Weather App====")
    city=input("Enter city name").strip()

    if not city:
        print("You didn't enter a city name")
        return
    
    try:
        data=get_weather(city)

        main_info= data["main"]
        weather_info=data["weather"][0]

        temp= main_info["temp"]
        feels_like=main_info["feels_like"]
        humidity=main_info["humidity"]
        description=weather_info["description"].title()

        print(f"\nWeather in {city.title()}:")
        print(f"  Description : {description}")
        print(f"  Temperature : {temp}°C")
        print(f"  Feels like  : {feels_like}°C")
        print(f"  Humidity    : {humidity}%")

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occured", http_err)

    except Exception as e:
        print("An error occurred", e)


if __name__=="__main__":
    main()