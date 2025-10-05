# DSC510-T301
# Week 12
# Final Project
# Author Ryan Krenke
# 5/31/23

import requests
import json

# API Key a1b225e72a631a029b2f2e60469ce46b


def zipCode():    # retrieves lat and lon from API based on user zip input
    zipInp = input("Please enter a 5-digit numeric zip code")
    url = "http://api.openweathermap.org/geo/1.0/zip?" \
          "zip=**" + zipInp + "**,US&appid=a1b225e72a631a029b2f2e60469ce46b"
    coordinates = ""
    headers = {
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("GET", url, data=coordinates, headers=headers)
    except requests.exceptions.Timeout as err:    # handling connection errors below
        print("An error has occurred with the connection to the website.")
        print("The following exception has been raised, ", err)
    except requests.exceptions.ConnectionError as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    except requests.exceptions.HTTPError as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    except requests.exceptions.TooManyRedirects as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    else:
        parsed = json.loads(response.text)
        try:
            lat = (parsed.get("lat", 0))
            assert lat != 0   # default lat for incorrect zip is 0
            lon = (parsed.get("lon", 0))
            assert lon != 0   # default lon for incorrect zip is 0
        except:
            print("Zip code entered is invalid. Please restart program and enter valid zip code.")
        else:
            return lat, lon


def city():    # retrieves lat and lon from API based on user city and state input
    cityInp = input("Please enter a city name")
    stateInp = input("Please enter a 2-letter state code")
    url = "http://api.openweathermap.org/geo/1.0/" \
          "direct?q=**" + cityInp + "**,**" + stateInp + "**,US&limit=1&appid=a1b225e72a631a029b2f2e60469ce46b"
    coordinates = ""
    headers = {
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("GET", url, data=coordinates, headers=headers)
    except requests.exceptions.Timeout as err:    # handling connection errors below
        print("An error has occurred with the connection to the website.")
        print("The following exception has been raised, ", err)
    except requests.exceptions.ConnectionError as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    except requests.exceptions.HTTPError as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    except requests.exceptions.TooManyRedirects as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    else:
        parsed = json.loads(response.text)
        try:    # error handling for invalid city or state entered (request doesn't return a lat/lon)
            lat = parsed[0]['lat']
            lon = parsed[0]['lon']
        except Exception as err:
            print("That city or state is not valid. "
                  "Please restart program and enter valid city and state. Error: ", err)
        else:
            return lat, lon


def fahrenheit(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=" \
          f"a1b225e72a631a029b2f2e60469ce46b&units=imperial"
    temperatures = ""
    headers = {
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("GET", url, data=temperatures, headers=headers)
    except requests.exceptions.Timeout as err:    # handling connection errors below
        print("An error has occurred with the connection to the website.")
        print("The following exception has been raised, ", err)
    except requests.exceptions.ConnectionError as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    except requests.exceptions.HTTPError as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    except requests.exceptions.TooManyRedirects as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    else:
        return response


def celsius(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=" \
          f"a1b225e72a631a029b2f2e60469ce46b&units=metric"
    temperatures = ""
    headers = {
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("GET", url, data=temperatures, headers=headers)
    except requests.exceptions.Timeout as err:    # handling connection errors below
        print("An error has occurred with the connection to the website.")
        print("The following exception has been raised, ", err)
    except requests.exceptions.ConnectionError as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    except requests.exceptions.HTTPError as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    except requests.exceptions.TooManyRedirects as err:
        print("An error has occurred with the connection to the website")
        print("The following exception has been raised, ", err)
    else:
        return response


def main():
    print("Welcome to the Weather Temperature Program. This program can display weather details for any"
          " location in the United States.")
    while True:
        entry1 = input("If you would like to look up weather for a location, please type 'y'. "
                       "Or type 'quit' to end program.")
        # determines whether to continue or end program
        if entry1.lower() == "y":    # start or continue using program
            entry2 = input("Enter 'zip' to search for temperature by zip code. Enter 'city' "
                           "to search for temperature by city and state")
            if entry2.lower() == "zip":
                lat, lon = zipCode()    # retrieves lat and lon from zip() function
                units = input("Would you like the temperature in Fahrenheit or Celsius? Type 'f'"
                              "for Fahrenheit and 'c' for Celsius.")
                if units.lower() == "f":    # retrieves json data from Fahrenheit() function
                    response = fahrenheit(lat, lon)
                    try:
                        parsed = json.loads(response.text)
                    except Exception as err:
                        print("There was an error making the request, ", err)
                    else:
                        # print(json.dumps(parsed, indent=4, sort_keys=True))  **for troubleshooting**
                        print("-" * 20)
                        print("Current Temperature:", parsed.get('main', {}).get('temp', 0), "Degrees F")
                        print("High Temperature:", parsed.get('main', {}).get('temp_max', 0), "Degrees F")
                        print("Low Temperature:", parsed.get('main', {}).get('temp_min', 0), "Degrees F")
                        print("Pressure:", parsed.get('main', {}).get('pressure', 0), "hPa")
                        print("Humidity:", parsed.get('main', {}).get('humidity', 0), "Percent %")
                        print("Cloudiness:", parsed.get('clouds', {}).get('all', 0), "Percent %")
                        # printing values from within returned json dictionary ^^^
                        print("-" * 20)
                elif units.lower() == "c":    # retrieves json data from celsius() function
                    response = celsius(lat, lon)
                    try:
                        parsed = json.loads(response.text)
                    except Exception as err:
                        print("There was an error making the request, ", err)
                    else:
                        print("-" * 20)
                        print("Current Temperature:", parsed.get('main', {}).get('temp', 0), "Degrees C")
                        print("High Temperature:", parsed.get('main', {}).get('temp_max', 0), "Degrees C")
                        print("Low Temperature:", parsed.get('main', {}).get('temp_min', 0), "Degrees C")
                        print("Pressure:", parsed.get('main', {}).get('pressure', 0), "hPa")
                        print("Humidity:", parsed.get('main', {}).get('humidity', 0), "Percent %")
                        print("Cloudiness:", parsed.get('clouds', {}).get('all', 0), "Percent %")
                        # printing values from within returned json dictionary ^^^
                        print("-" * 20)
            elif entry2.lower() == "city":
                lat, lon = city()    # retrieves lat and lon from city() function
                units = input("Would you like the temperature in Fahrenheit or Celsius? Type 'f'"
                              "for Fahrenheit and 'c' for Celsius.")
                if units.lower() == "f":    # retrieves json data from Fahrenheit() function
                    response = fahrenheit(lat, lon)
                    try:
                        parsed = json.loads(response.text)
                    except Exception as err:
                        print("There was an error making the request, ", err)
                    else:
                        print("-" * 20)
                        print("Current Temperature:", parsed.get('main', {}).get('temp', 0), "Degrees F")
                        print("High Temperature:", parsed.get('main', {}).get('temp_max', 0), "Degrees F")
                        print("Low Temperature:", parsed.get('main', {}).get('temp_min', 0), "Degrees F")
                        print("Pressure:", parsed.get('main', {}).get('pressure', 0), "hPa")
                        print("Humidity:", parsed.get('main', {}).get('humidity', 0), "Percent %")
                        print("Cloudiness:", parsed.get('clouds', {}).get('all', 0), "Percent %")
                        # printing values from within returned json dictionary ^^^
                        print("-" * 20)
                elif units.lower() == "c":    # retrieves json data from Celsius() function
                    response = celsius(lat, lon)
                    try:
                        parsed = json.loads(response.text)
                    except Exception as err:
                        print("There was an error making the request, ", err)
                    else:
                        print("-" * 20)
                        print("Current Temperature:", parsed.get('main', {}).get('temp', 0), "Degrees C")
                        print("High Temperature:", parsed.get('main', {}).get('temp_max', 0), "Degrees C")
                        print("Low Temperature:", parsed.get('main', {}).get('temp_min', 0), "Degrees C")
                        print("Pressure:", parsed.get('main', {}).get('pressure', 0), "hPa")
                        print("Humidity:", parsed.get('main', {}).get('humidity', 0), "Percent %")
                        print("Cloudiness:", parsed.get('clouds', {}).get('all', 0), "Percent %")
                        # printing values from within returned json dictionary ^^^
                        print("-" * 20)
                else:
                    print("Sorry that entry is invalid")
                    continue
            else:
                print("Sorry that entry is invalid")
                continue
        elif entry1.lower() == "quit":    # end program
            break
        else:
            print("Sorry that entry is invalid")
            continue


if __name__ == "__main__":
    main()
