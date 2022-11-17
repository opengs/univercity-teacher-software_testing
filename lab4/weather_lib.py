import requests

def get_weather_info_text(location: str):
    '''Gets information about the weather in selected location'''
    url = f"https://wttr.in/{location}"
    return requests.get(url).text

def get_weather_info_json(location: str):
    url = f"https://wttr.in/{location}?format=j1"
    return requests.get(url).json()