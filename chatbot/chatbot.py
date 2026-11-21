from openai import OpenAI
from dotenv import load_dotenv
import os 


load_dotenv()


client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

while True:

    user_input=input("/nUSER:: ").lower()

    if( user_input in ["exit","quit",'bye']):
        break

    completion = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {"role": "developer", "content": "Talk like a genz worker  and   answer in  para only 200 words ."},
            {
                "role": "user",
                "content":user_input,
            },
        ],
    )
    print( "/nASSISANT:: ", completion.choices[0].message.content)





