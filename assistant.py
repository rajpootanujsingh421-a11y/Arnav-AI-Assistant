from datetime import datetime
import os
import webbrowser
from commands import *
def get_response(message):
    
    message = message.lower().strip()
    
    if message == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        return f"⌚ Current Time: {current_time}"
    
    if message == "open notepad":
        return open_notepad()
    
    if message == "open chrome":
        return open_chrome()
    
    if message == "open youtube":
        return open_youtube()
    
    if message == "open github":
        return open_github()

    responses = {           
        "hello": "Hello Anuj! 👋",
        "hi": "Hi Bhai ❤️", 
        "how are you": "Main mast hoon 😎, tum batao",
        "thanks": "Always bhai ❤️",
        "bye": "Bye Anuj! Coding mat chhodna. 👊"
    }
    
    return responses.get(
        message,
        "Sorry bhai, ye mujhe abhi nahi aata. 😅"
    )