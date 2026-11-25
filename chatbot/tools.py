import json 

from datetime import datetime
from utility.utility import log


def get_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_weather(city:str,temperature_unit:str="celsius",include_wind:bool=False)->str:
    # For demonstration purposes, we'll return a mock weather response.
    # In a real implementation, you would call a weather API here.
    if include_wind:
        return f"The current weather in {city} is sunny with a temperature of 25°{temperature_unit} and wind speed of 10 mph."
    return f"The current weather in {city} is sunny with a temperature of 25°{temperature_unit}."

def get_city_name()->str:
    return "delhi"
 
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
                "required":["city"]
            }
        }
    },
    {
         "type":"function",
                "function":{
                    "name":"get_city_name",
                    "description":"Get the name of the city and this is the mock function for testing the function calling feature",
                    "parameters":{
                        "type":"object",
                        "properties":{}
                    }
                }
    }



]

FUNCTION_NAME_TO_FUNCTION={
    "get_date":get_date,
    "get_weather":get_weather,
    "get_city_name":get_city_name
}

def call_tool( tool):
    function_arg={};
    function_name=tool.function.name   # it will be a string  

    try:
        name_tool=FUNCTION_NAME_TO_FUNCTION[( function_name ) ]  # find the res call function

        log(f" 🔧 Calling tool: {function_name} with arguments: {tool.function.arguments}")         
        function_arg= json.loads(tool.function.arguments or {})  # tool.argument wll be a string convert it into the dict

        result= name_tool( **function_arg )  #  dictin unpacking  operator 

       
    except Exception as e:
        return f"Error calling tool {tool.function.name}: {str(e)}"
    
    
    return  result
    


