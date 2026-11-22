from openai import OpenAI
from dotenv import load_dotenv
import os 
import json
from tools import Tools, FUNCTION_NAME_TO_FUNCTION

load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

message=[
{
    "role":"system",
    "content":"You are a helpful assistant."
}
]

while True:

    user_input=input("\nUSER:: ").strip().lower()
    # print("\nUSER:: ", user_input)

    if( user_input in ["exit","quit",'bye']):
        break

    message.append({
        "role":"user",
        "content":user_input
    })

    completion = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=message,
        tools=Tools
    )

    # print("\n", completion.choices[0].message)



    if( completion.choices[0].message.tool_calls):

        for tool in completion.choices[0].message.tool_calls:   # first to get the name of the function it want to call

            function_name=tool.function.name   # it will be a string  
            name_tool=FUNCTION_NAME_TO_FUNCTION[( function_name ) ]  # find the res call function

            function_arg= json.loads(tool.function.arguments or {})  # tool.argument wll be a string convert it into the dict

            result= name_tool( **function_arg )  #  dictin unpacking  operator 

            message.append({
                "role":"tool",
                "tool_call_id":tool.id,
                "content":str(result)

            })


        response = client.chat.completions.create(
                model=os.getenv("MODEL_NAME"),
                messages=message,
                tools=Tools
        )
        completion=response



    message.append({
        "role":"assistant",
        "content":completion.choices[0].message.content
    })
    print( "\nASSISANT:: ", completion.choices[0].message.content)

print(message)


#completion = ChatCompletion(#
#     id='chatcmpl-123',
#     choices=[
#         Choice(
#             index=0,
#             message=ChatCompletionMessage(
#                 role='assistant',
#                 content=None, cursor is
#                 tool_calls=[
#                     ChatCompletionMessageToolCall(
#                         id='call_abc123',
#                         type='function',
#                         function=Function(
#                             name='get_weather',
#                             arguments='{"city": "Delhi"}'
#                         )
#                     )
#                 ]
#             ),
#             finish_reason='tool_calls'
#         )
#     ]
# )




