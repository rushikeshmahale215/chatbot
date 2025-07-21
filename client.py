# groqapi ="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"
import os

from groq import Groq

client = Groq(
    api_key="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"
)
command = '''
[10:22 PM, 7/20/2025] Rutuja Gawande: 
😅
[10:22 PM, 7/20/2025] Rutuja Gawande: Thank you
[10:23 PM, 7/20/2025] Rushikesh Mahale: Are mavshi aahe majhi
[10:23 PM, 7/20/2025] Rutuja Gawande: Br br tula vatel te
[10:25 PM, 7/20/2025] Rushikesh Mahale: Zal ka j1
[10:25 PM, 7/20/2025] Rutuja Gawande: Ho tuz
[10:25 PM, 7/20/2025] Rushikesh Mahale: Ho
[10:26 PM, 7/20/2025] Rutuja Gawande: Br'''


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "You are a personed whose name is Rushi, He is from India, He is a software engineer, He is 20 years old, He is AI Agent Developer. You analyzed chat history and respond like Rushi"
        },
        {
            "role":"user",
            "content": command
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

