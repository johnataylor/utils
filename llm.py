import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, who won the world series in 2020?"}
    ]
)

print(response.choices[0].message.content)