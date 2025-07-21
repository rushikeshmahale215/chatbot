# groqapi ="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"
import os

from groq import Groq

client = Groq(
    api_key="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"
)
command = '''
RM:THANK YOU
SR:OK
RM:HOW ARE YOU
SR:FINE


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "You are a personed whose name is RM, He is from India, He is a software engineer, He is 20 years old, He is AI Agent Developer. You analyzed chat history and respond like SR"
        },
        {
            "role":"user",
            "content": command
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

