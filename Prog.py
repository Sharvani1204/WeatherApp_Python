import requests

API_KEY = "your_api_key_here"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + f"appid={API_KEY}&q={city}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']

        print(f"\nCity: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather.capitalize()}")
    else:
        print("City not found or API error.")

def menu():
    print("**********Weather App**********")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("Exiting Weather App..........")
            break
        get_weather(city)

if __name__ == "__main__":
    menu()