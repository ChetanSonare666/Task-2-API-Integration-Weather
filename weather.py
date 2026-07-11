import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

if not API_KEY:
    print("Error: API_KEY not found.")
    print("Create a .env file and add:")
    print("API_KEY=your_api_key")
    exit()


def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\n========== Weather Report ==========")
            print(f"City        : {data['name']}")
            print(f"Country     : {data['sys']['country']}")
            print(f"Temperature : {data['main']['temp']} °C")
            print(f"Feels Like  : {data['main']['feels_like']} °C")
            print(f"Humidity    : {data['main']['humidity']} %")
            print(f"Pressure    : {data['main']['pressure']} hPa")
            print(f"Weather     : {data['weather']['description'].title()}")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")
            print("====================================")

        elif response.status_code == 404:
            print("\nCity not found.")

        elif response.status_code == 401:
            print("\nInvalid API Key.")

        else:
            print(f"\nSomething went wrong. Status Code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("No internet connection.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit()

    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    print("=" * 40)
    print("      Weather Information App")
    print("=" * 40)

    while True:
        city = input("\nEnter city name (or 'exit'): ").strip()

        if city.lower() == "exit":
            print("Goodbye!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()