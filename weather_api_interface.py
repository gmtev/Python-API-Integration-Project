# both as a function and as a "while" loop
import requests


def get_weather_data():
        api_key = "ca01028ac3ba5fd56e08160dd836a7f3"
        city_name = input('Enter city name: ')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return (f'Temperature: {(temp - 273.15):.2f} C or {temp} K\n'
                    f'Description of the weather: {desc}')
        else:
            return 'Error fetching weather data'


print(get_weather_data())
#
#
# while True:
#     api_key = "ca01028ac3ba5fd56e08160dd836a7f3"
#     city_name = input('Enter city name (or "exit" if you want to quit): ')
#     if city_name == "exit ":
#         break
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         temp = data['main']['temp']
#         desc = data['weather'][0]['description']
#         print(f'''Temperature: {(temp - 273.15):.2f} C or {temp} K\nDescription of the weather: {desc}''')
#     else:
#         print('Error fetching weather data')
