"""Retrieve weather data from OpenWeatherMap and store it in a CSV file."""

import csv
import json

import requests


def get_city():
    """
    Prompt the user for a city name and validate the input.
    
    Returns:
        str: A non-empty city name.
    """
    while True:
        city = input("Enter a city name: ").strip()

        if city:
            return city

        print("City name cannot be empty. Please try again.")


def get_api_key():
    """
    Read the OpenWeatherMap API key from api_key.txt.
    
    Returns:
        str: The API key stored in the file.
        
    Raises:
        FileNotFoundError: If api_key.txt does not exist.
    """
    with open("api_key.txt", "r") as file:
        return file.read().strip()


def get_weather_data(city, api_key):
    """
    Retrieve current weather data from a city from OpenWeatherMap.
    
    Args:
        city (str): The city to search for.
        api_key (str): The OpenWeatherMap API key.
        
    Returns:
        dict or None: A dictionary of weather data if successful,
        otherwise None.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            print("Error: City not found.")
            return None

        if response.status_code == 401:
            print("Error: Invalid or inactive API key.")
            return None

        response.raise_for_status()

        try:
            data = json.loads(response.text)
        except json.JSONDecodeError:
            print("Error: Could not parse the API response.")
            return None

        weather_data = {
            "City": data["name"],
            "Country": data["sys"]["country"],
            "Temperature (C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Description": data["weather"][0]["description"]
        }

        return weather_data

    except requests.exceptions.RequestException:
        print("Request error: Unable to connect to the weather service.")
        return None


def print_weather_report(weather_data):
    """
    Print a formatted weather summary.
    
    Args:
        weather_data (dict): The weather information to display.
    """
    print("\nWeather Report")
    print(f"City: {weather_data['City']}")
    print(f"Country: {weather_data['Country']}")
    print(
        f"Temperature: {weather_data['Temperature (C)']} degrees Celsius"
    )
    print(f"Humidity: {weather_data['Humidity (%)']}%")
    print(f"Description: {weather_data['Description']}")


def write_to_csv(weather_data):
    """
    Append weather data to city_data.csv.
    
    Args:
        weather_data (dict): The weather information to save.
    """
    fieldnames = [
        "City",
        "Country",
        "Temperature (C)",
        "Humidity (%)",
        "Description"
    ]

    try:
        file_exists = False

        try:
            with open("city_data.csv", "r", newline=""):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open("city_data.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(weather_data)

        print("\nWeather data saved to city_data.csv.")

    except IOError as error:
        print(f"Error writing to CSV file: {error}")


def read_from_csv():
    """
    Read city_data.csv and report saved city names and temperatures.
    """
    try:
        with open("city_data.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        print(f"\nCities currently in file: {len(rows)}")

        for row in rows:
            print(
                f"{row['City']}: "
                f"{row['Temperature (C)']} degrees Celsius"
            )

    except FileNotFoundError:
        print("No city_data.csv file was found")

    except IOError as error:
        print(f"Error reading CSV file: {error}")


def main():
    """Run the city weather reporter program."""
    try:
        api_key = get_api_key()
    except FileNotFoundError:
        print("Error: api_key.txt was not found.")
        return

    if api_key == "YOUR_API_KEY_HERE" or not api_key:
        print(
            "API key is not ready yet. Replace the placeholder "
            "in api_key.txt with your OpenWeatherMap API key."
        )
        return

    city = get_city()
    weather_data = get_weather_data(city, api_key)

    if weather_data:
        print_weather_report(weather_data)
        write_to_csv(weather_data)
        read_from_csv()


if __name__ == "__main__":
    main()

    