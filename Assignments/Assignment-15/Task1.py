import requests
import json

def display_weather_details(city_name, api_key):
    """
    Display weather details of a city using OpenWeatherMap API.
    
    Args:
        city_name (str): Name of the city
        api_key (str): API key for OpenWeatherMap API
    
    Returns:
        None: Prints weather details as JSON output
    """
    # OpenWeatherMap API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use metric units (Celsius)
    }
    
    # Make the API request
    response = requests.get(url, params=params)
    
    # Get JSON data from response
    weather_data = response.json()
    
    # Display weather details as JSON output
    print(json.dumps(weather_data, indent=4, ensure_ascii=False))

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    city = "London"
    display_weather_details(city, api_key)