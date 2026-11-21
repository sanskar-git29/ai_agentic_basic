from openai import OpenAI
from dotenv import load_dotenv
import os 


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

    user_input=input("\nUSER:: ").lower()

    if( user_input in ["exit","quit",'bye']):
        break

    message.append({
        "role":"user",
        "content":user_input
    })

    completion = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=message,
    )

    message.append({
        "role":"assistant",
        "content":completion.choices[0].message.content
    })
    print( "\nASSISANT:: ", completion.choices[0].message.content)
    
print(message)





