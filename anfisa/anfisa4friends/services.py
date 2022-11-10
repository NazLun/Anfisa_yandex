import requests

def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, weather_parameters)
    except requests.ConnectionError:
        return '<network error>'
    if response.status_code == 200:
        return response.text.rstrip()
    else:
        return '<Error in weather server. Try later>'


def what_temperature(weather):
    if (weather == '<network error>' or
        weather == '<Error in weather server. Try later>'):
        return weather
    temperarure = weather.split()[1]
    parsed_temperature = ''
    for char in temperarure:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature


def what_conclusion(parsed_temperature):
    try:
        temperature = int(parsed_temperature)
    except ValueError:
        return "Can't find out the weather"

    if temperature < 18:
        return 'Today is cold for the icecream!'
    elif 18 <= temperature <= 27:
        return "Let's go!"
    else:
        return 'Too hot today!'





