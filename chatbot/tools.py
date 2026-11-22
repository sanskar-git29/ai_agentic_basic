from datetime import datetime
def get_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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
    }
]

FUNCTION_NAME_TO_FUNCTION={
    "get_date":get_date
}