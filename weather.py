import dotenv
import os
import requests

dotenv.load_dotenv()

def get_weather(city):
    if len(city.strip(' ')) == 0:
        city = 'ranchi'
    API_LINK = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"

    return requests.get(API_LINK).json()

if __name__ == '__main__':
    city = input('Enter city: ')
    print(get_weather(city))