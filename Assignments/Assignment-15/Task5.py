import requests
import json
from datetime import datetime

def display_weather_details(city_name, api_key, filename="results.json"):
    """
    Display weather details of a city using OpenWeatherMap API with error handling.
    Calls the API dynamically based on user input (city name) and appends raw JSON to file.
    
    Args:
        city_name (str): Name of the city
        api_key (str): API key for OpenWeatherMap API
        filename (str): Name of the JSON file to store weather details (default: results.json)
    
    Returns:
        None: Prints weather details in user-friendly format and appends raw JSON to file
    """
    # OpenWeatherMap API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use metric units (Celsius)
    }
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Make the API request
        response = requests.get(url, params=params)
        
        # Get JSON data from response
        weather_data = response.json()
        
        # Check if the city is invalid (OpenWeatherMap returns 404 for invalid cities)
        # The 'cod' field can be a string "404" or integer 404
        if 'cod' in weather_data and (weather_data['cod'] == '404' or weather_data['cod'] == 404):
            # Add timestamp and error info to the error response
            error_entry = {
                'timestamp': timestamp,
                'city_searched': city_name,
                'error': 'City not found',
                'raw_response': weather_data
            }
            print("Error: City not found. Please enter a valid city.")
            # Append error to JSON file
            append_to_json_file(filename, error_entry)
            return
        
        # Check for other API errors
        if 'cod' in weather_data and weather_data['cod'] != 200 and weather_data['cod'] != '200':
            # Add timestamp and error info to the error response
            error_entry = {
                'timestamp': timestamp,
                'city_searched': city_name,
                'error': 'API error',
                'raw_response': weather_data
            }
            print("Error: Could not connect to API. Check your API key or network connection.")
            # Append error to JSON file
            append_to_json_file(filename, error_entry)
            return
        
        # Extract weather details for user-friendly display
        city = weather_data['name']
        temperature = int(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        
        # Display weather details in user-friendly format
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.title()}")
        
        # Add timestamp to weather data before appending
        weather_data['timestamp'] = timestamp
        weather_data['city_searched'] = city_name
        
        # Append raw JSON to file
        append_to_json_file(filename, weather_data)
        print(f"\nRaw JSON data appended to {filename}\n")
        
    except requests.exceptions.ConnectionError:
        # Handle network connection errors
        error_entry = {
            'timestamp': timestamp,
            'city_searched': city_name,
            'error': 'Connection error',
            'message': 'Could not connect to API. Check your API key or network connection.'
        }
        print("Error: Could not connect to API. Check your API key or network connection.")
        append_to_json_file(filename, error_entry)
    except requests.exceptions.RequestException:
        # Handle other request errors
        error_entry = {
            'timestamp': timestamp,
            'city_searched': city_name,
            'error': 'Request error',
            'message': 'Could not connect to API. Check your API key or network connection.'
        }
        print("Error: Could not connect to API. Check your API key or network connection.")
        append_to_json_file(filename, error_entry)
    except json.JSONDecodeError:
        # Handle JSON parsing errors
        error_entry = {
            'timestamp': timestamp,
            'city_searched': city_name,
            'error': 'JSON decode error',
            'message': 'Could not connect to API. Check your API key or network connection.'
        }
        print("Error: Could not connect to API. Check your API key or network connection.")
        append_to_json_file(filename, error_entry)
    except Exception:
        # Handle any other unexpected errors
        error_entry = {
            'timestamp': timestamp,
            'city_searched': city_name,
            'error': 'Unexpected error',
            'message': 'Could not connect to API. Check your API key or network connection.'
        }
        print("Error: Could not connect to API. Check your API key or network connection.")
        append_to_json_file(filename, error_entry)


def append_to_json_file(filename, data):
    """
    Append data to a JSON file as an array. Creates the file if it doesn't exist.
    
    Args:
        filename (str): Name of the JSON file
        data (dict): Data to append to the JSON file
    """
    try:
        # Read existing data if file exists
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            # File doesn't exist, start with empty list
            existing_data = []
        except json.JSONDecodeError:
            # File exists but is invalid JSON, start with empty list
            existing_data = []
        
        # Append new data
        existing_data.append(data)
        
        # Write back to file with proper formatting
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)
            
    except Exception as e:
        print(f"Warning: Could not write to {filename}: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    
    # User input
    city = input("Enter city name: ")
    display_weather_details(city, api_key)