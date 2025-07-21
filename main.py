import pyautogui
import time
import pyperclip
import os
from groq import Groq

client = Groq(
    api_key="GROQ_API_KEY"
)


# Short delay before starting to allow switching to target window
time.sleep(2)

# Step 1: Click on icon to activate the window or app
pyautogui.click(1400, 1038)
time.sleep(1)

# Step 2: Click and drag to select text
pyautogui.moveTo(1801, 219)
pyautogui.mouseDown()
pyautogui.moveTo(1784, 927, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy the selected text to clipboard
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1859,944)
time.sleep(0.5)  # wait for clipboard to update

# Step 4: Get the clipboard contents
chat_history = pyperclip.paste()

# Step 5: Print or use the copied text
print("Copied Text:")
print(chat_history)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "You are a personed whose name is Pavan, you are from India, you are a ENGINEER, you are 19 years old. You analyzed chat history and respond like Rushi"
        },
        {
            "role":"user",
            "content": chat_history
        }
    ],
    model="llama-3.3-70b-versatile",
)

response = chat_completion.choices[0].message.content
pyperclip.copy(response)

pyautogui.click(1123, 971)
time.sleep(0.5)

# Step 6: Paste the text and press Enter
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.2)
pyautogui.press('enter')
