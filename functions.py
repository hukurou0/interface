import json

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(function_args):
    location=function_args.get("location"),
    unit=function_args.get("unit"),
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

available_functions = {
        "get_current_weather": get_current_weather,
} 
