# Weather Information App

A simple Python application that fetches real-time weather information for any city using the OpenWeatherMap API. The application allows users to search for a city and displays current weather details such as temperature, humidity, wind speed, and weather conditions.

---

## Features

* Search weather by city name
* Fetch live weather data from an API
* Parse JSON responses
* Display temperature, humidity, pressure, and wind speed
* Exception handling for invalid cities and network errors
* Easy-to-use command-line interface

---

## Technologies Used

* Python 3
* Requests Library
* OpenWeatherMap API

---

## Project Structure

```text
WeatherApp/
│
├── weather.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Requirements

* Python 3.8 or above
* Internet connection
* OpenWeatherMap API Key

Install the required package:

```bash
pip install -r requirements.txt
```

---

## Getting an API Key

1. Create a free account on OpenWeatherMap.
2. Generate a new API key.
3. Open `weather.py`.
4. Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your own API key.

---

## How to Run

Run the application using:

```bash
python weather.py
```

Enter the city name when prompted.

Type `exit` to close the application.

---

## Example Output

```text
========================================
      Weather Information App
========================================

Enter city name (or 'exit'): Delhi

========== Weather Report ==========
City        : Delhi
Country     : IN
Temperature : 34.2 °C
Feels Like  : 38.0 °C
Humidity    : 56 %
Pressure    : 1003 hPa
Weather     : Clear Sky
Wind Speed  : 4.1 m/s
====================================
```

---

## Error Handling

The application handles:

* Invalid city names
* No internet connection
* Request timeout
* Unexpected errors

---

## Assignment Requirements Covered

* Uses the `requests` module
* Parses JSON response
* Accepts user input
* Allows city search
* Displays formatted results
* Includes exception handling

---

## Future Improvements

* Weather forecast for upcoming days
* Search history
* Save results to a CSV file
* GUI using Tkinter or PyQt
* Support multiple weather APIs

---

## Author

Created as part of a Python API Integration assignment.
