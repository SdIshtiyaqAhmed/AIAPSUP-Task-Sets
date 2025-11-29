import requests
import json

def display_weather_details(city_name, api_key):
    """
    Display weather details of a city using OpenWeatherMap API with error handling.
    
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
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Get JSON data from response
        weather_data = response.json()
        
        # Check if the API returned an error (OpenWeatherMap returns errors in JSON format)
        if 'cod' in weather_data and weather_data['cod'] != 200:
            print("Error: Could not connect to API. Check your API key or network connection.")
            return
        
        # Extract weather details
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        
        # Display weather details in a user-friendly format
        print("\n" + "="*50)
        print(f"Weather Details for {city}")
        print("="*50)
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.title()}")
        print("="*50 + "\n")
        
    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError, 
            requests.exceptions.Timeout, requests.exceptions.HTTPError, 
            json.JSONDecodeError, Exception):
        # Handle all types of errors with the specified error message
        print("Error: Could not connect to API. Check your API key or network connection.")

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    city = "London"
    display_weather_details(city, api_key)