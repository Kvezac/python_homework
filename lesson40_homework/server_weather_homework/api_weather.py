from dotenv import load_dotenv
import requests
import os


def get_request(city):
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    url = fr"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&&appid={API_KEY}"
    response = requests.get(url)
    result = 'Something Went Wrong'
    if response.status_code == 200:
        result = ''
        weather_data = response.json()
        city = weather_data['name']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        description = weather_data['weather'][0]['description']
        result += f'City name: {city}\n' \
                  f'Temperature: {temp}℃\n' \
                  f'The temperature is felt: {feels_like}℃\n' \
                  f'Humidity: {humidity}%\n' \
                  f'Pressure: {pressure}hPa\n' \
                  f'Description: {description}\n' \
                  f'+++++++++++++++++++++++++++++++\n'

    return result


if __name__ == '__main__':
    print(get_request('Moscow'))
