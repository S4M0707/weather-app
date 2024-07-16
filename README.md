# weather-app

This is a simple weather app built with Flask that displays weather information for a given city using the OpenWeatherMap API.

## Features

- Display current weather information for a city
- Shows temperature, weather description, pressure, humidity, visibility, and wind details
- Simple, elegant user interface

## Requirements

- Python 3.8

## Installation

1. Clone the repository:

```bash
git clone https://github.com/S4M0707/weather-app.git
cd weather-app
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the root directory of your project and add your OpenWeatherMap API key:

```bash
API_KEY=your_openweathermap_api_key
```

## Running the App

1. Run the app with Waitress:

```bash
python3 server.py
```

2. Open your browser and navigate to http://localhost:8000 to view the app.

## Usage

1. Open the app in your browser.

2. Enter a city name to get the current weather information.

## Live Demo
Check out the live demo: [Weather App](https://weather-app-9oul.onrender.com/)

## License
This project is licensed under the MIT License.

