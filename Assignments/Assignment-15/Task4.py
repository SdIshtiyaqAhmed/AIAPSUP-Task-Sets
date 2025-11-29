import requests
import json
from datetime import datetime

def display_weather_details(city_name, api_key):
    """
    Display weather details of a city using OpenWeatherMap API with error handling.
    Calls the API dynamically based on user input (city name).
    
    Args:
        city_name (str): Name of the city
        api_key (str): API key for OpenWeatherMap API
    
    Returns:
        None: Prints weather details in a user-friendly format or error message
    """
    # OpenWeatherMap API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use metric units (Celsius)
    }
    
    try:
        # Make the API request
        response = requests.get(url, params=params)
        
        # Get JSON data from response
        weather_data = response.json()
        
        # Check if the city is invalid (OpenWeatherMap returns 404 for invalid cities)
        # The 'cod' field can be a string "404" or integer 404
        if 'cod' in weather_data and (weather_data['cod'] == '404' or weather_data['cod'] == 404):
            print("Error: City not found. Please enter a valid city.")
            return
        
        # Check for other API errors
        if 'cod' in weather_data and weather_data['cod'] != 200 and weather_data['cod'] != '200':
            print("Error: Could not connect to API. Check your API key or network connection.")
            return
        
        # Extract weather details
        city = weather_data['name']
        temperature = int(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        
        # Display weather details in the specified format
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.title()}")
        
    except requests.exceptions.ConnectionError:
        # Handle network connection errors
        print("Error: Could not connect to API. Check your API key or network connection.")
    except requests.exceptions.RequestException:
        # Handle other request errors
        print("Error: Could not connect to API. Check your API key or network connection.")
    except json.JSONDecodeError:
        # Handle JSON parsing errors
        print("Error: Could not connect to API. Check your API key or network connection.")
    except Exception:
        # Handle any other unexpected errors
        print("Error: Could not connect to API. Check your API key or network connection.")

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    
    # User input
    city = input("Enter city name: ")
    display_weather_details(city, api_key)