import os 
import json
from types import SimpleNamespace

from openai import OpenAI
from dotenv import load_dotenv

from tools import Tools, FUNCTION_NAME_TO_FUNCTION, call_tool,build_tool_calls_payload
from utility.utility import log 

load_dotenv()

max_steps=int(os.getenv("MAX_STEPS"));

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def get_stream_response(history):
    stream = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=history,
            tools=Tools,
            stream=True
    )

    content=""
    label_printed = False
    calls={};
   

    for chunk in stream:

        if  not chunk:
            continue

        delta=chunk.choices[0].delta
        if delta.content : 
            if not label_printed:
                print("🤖 Assistant: ", end="", flush=True)
                label_printed = True
            print(delta.content, end="", flush=True)
            content += delta.content

        # print(f"full response ::: \n -> {content}")

        for tc in (delta.tool_calls or []):
            obj = calls.setdefault(
                tc.index,
                SimpleNamespace(id=None, function=SimpleNamespace(name="", arguments="")),
            )
            if tc.id:
                obj.id = tc.id
            if tc.function and tc.function.name:
                obj.function.name += tc.function.name
            if tc.function and tc.function.arguments:
                obj.function.arguments += tc.function.arguments

    calls_list=[]
    for key in sorted(calls):
        calls_list.append(calls[key]);

    return content ,calls_list,


message = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
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

        full_response,tool_calls =get_stream_response(message)

        log(f" Steps {step+1} of {max_steps}");

        if not tool_calls:
            break

        message.append({
            "role": "assistant",
            "content": full_response,
            "tool_calls": build_tool_calls_payload(tool_calls)
        })

        for tool in tool_calls:   # first to get the name of the function it want to call
            result= call_tool(tool)
            message.append({
                "role":"tool",
                "tool_call_id":tool.id,
                "content":str(result)

            })
    else:
        fallback = "Sorry, I could not finish this task."
        log(f" 🤖 Assistant: {fallback}")

        message.append({
            "role": "assistant",
            "content": fallback
        })
        continue

    message.append({
        "role":"assistant",
        "content":full_response
    })
    # print( "🤖 Assistant: ",full_response)

print((message))


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




