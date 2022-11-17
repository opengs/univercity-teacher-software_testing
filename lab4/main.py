from weather_lib import get_weather_info_json, get_weather_info_text

def main():
    val = input("Please, enter your city: ")
    print(get_weather_info_text(val))

if __name__ == "__main__":
    main()