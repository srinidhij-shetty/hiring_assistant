from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(messages):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # fast + good for this task
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content