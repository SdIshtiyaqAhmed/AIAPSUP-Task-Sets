import requests
import json

def display_weather_details(city_name, api_key):
    """
    Display weather details of a city using OpenWeatherMap API with error handling.
    
    Args:
        city_name (str): Name of the city
        api_key (str): API key for OpenWeatherMap API
    
    Returns:
        None: Prints weather details as JSON output or error message
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
        
        # Display weather details as JSON output
        print(json.dumps(weather_data, indent=4, ensure_ascii=False))
        
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