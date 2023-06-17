from dotenv import load_dotenv
import requests
import os


def main(city):
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    url = fr"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    print(response.json())


if __name__ == '__main__':
    main('Moscow')
