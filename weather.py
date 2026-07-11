import os
from datetime import datetime

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Check if API key is available
if not API_KEY:
    print("Error: API_KEY not found.")
    print("Create a .env file and add:")
    print("API_KEY=your_api_key")
    exit()


def get_weather(city):
    """Fetch and display weather information for a city."""

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            print("\n========== Weather Report ==========")
            print(f"Date & Time : {current_time}")
            print(f"City        : {data['name']}")
            print(f"Country     : {data['sys']['country']}")
            print(f"Temperature : {data['main']['temp']} °C")
            print(f"Feels Like  : {data['main']['feels_like']} °C")
            print(f"Humidity    : {data['main']['humidity']} %")
            print(f"Pressure    : {data['main']['pressure']} hPa")
            print(f"Weather     : {data['weather'][0]['description'].title()}")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")
            print(f"Visibility  : {data['visibility'] / 1000} km")
            print("====================================")

        elif response.status_code == 404:
            print("\nCity not found. Please enter a valid city name.")

        elif response.status_code == 401:
            print("\nInvalid API Key. Please check your .env file.")

        else:
            print(f"\nSomething went wrong. Status Code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("\nNo internet connection.")

    except requests.exceptions.Timeout:
        print("\nRequest timed out.")

    except requests.exceptions.RequestException as e:
        print(f"\nRequest failed: {e}")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit()

    except Exception as e:
        print(f"\nUnexpected error: {e}")


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