
import os 
import json

from openai import OpenAI
from dotenv import load_dotenv

from tools import Tools, FUNCTION_NAME_TO_FUNCTION, call_tool
from utility.utility import log 

load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

max_steps=int(os.getenv("MAX_STEPS"));

message=[
{
    "role":"system",
    "content":"You are a helpful assistant."
}
]

while True:

    user_input=input("\n👦USER:: ").strip().lower()
    # print("\nUSER:: ", user_input)

    if( user_input in ["exit","quit",'bye']):
        break

    message.append({
        "role":"user",
        "content":user_input
    })

    for  step in  range( max_steps):

        completion = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=message,
            tools=Tools
        )

        # print("\n", completion.choices[0].message)
        msg=completion.choices[0].message

        log(f" Steps {step+1} of {max_steps}");


        if not msg.tool_calls:
            break

        message.append( msg)
        
        for tool in msg.tool_calls:   # first to get the name of the function it want to call
            result= call_tool(tool)
            message.append({
                "role":"tool",
                "tool_call_id":tool.id,
                "content":str(result)

            })
    else:
        fallback = "Sorry, I could not finish this task."

        message.append({
            "role": "assistant",
            "content": fallback
        })
        print("🤖 Assistant: " + fallback)
        # chat_file_path = save_chat(chat_file_path, messages[1:])
        continue


    message.append({
        "role":"assistant",
        "content":msg.content
    })
    print( "🤖 Assistant: ", msg.content)

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




