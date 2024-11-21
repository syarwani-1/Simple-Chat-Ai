import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API key not found. Make sure the .env file contains 'GROQ_API_KEY=<api_key>'")
client = Groq(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "your instructions here"
    }
]

while True:
    user_message = input("You: ")
    if user_message.lower() in ["exit", "quit", "bye"]:
        print("Exiting chat. See you later!")
        break
      
    messages.append({"role": "user", "content": user_message})
    
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    print("AI:", end=" ")
    ai_response = ""
    for chunk in completion:
        part = chunk.choices[0].delta.content or ""
        ai_response += part
        print(part, end="")
    print()
    
    messages.append({"role": "assistant", "content": ai_response})