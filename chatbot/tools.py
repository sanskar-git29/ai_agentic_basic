from datetime import datetime
def get_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_weather(city:str,temperature_unit:str,include_wind:bool=False)->str:
    # For demonstration purposes, we'll return a mock weather response.
    # In a real implementation, you would call a weather API here.
    if include_wind:
        return f"The current weather in {city} is sunny with a temperature of 25°{temperature_unit} and wind speed of 10 mph."
    return f"The current weather in {city} is sunny with a temperature of 25°{temperature_unit}."



Tools=[
    {

        "type":"function",
        "function":{
            "name":"get_date",
            "description":"Get the current date and time",
            "parameters":{
                "type":"object",
                "properties":{}
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_weather",
            "description":"Get the current weather for a given city",
            "parameters":{
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string",
                        "description":"The name of the city to get the weather for"
                    },
                     "temperature_unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit"
                    },
                    "include_wind": {
                        "type": "boolean",
                        "description": "Whether to include wind information"
                    }
                },
                "required":["city", "temperature_unit"]
            }
        }
    }
]

FUNCTION_NAME_TO_FUNCTION={
    "get_date":get_date,
    "get_weather":get_weather
}

