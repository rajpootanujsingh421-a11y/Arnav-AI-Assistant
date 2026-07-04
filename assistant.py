from datetime import datetime
import os
import webbrowser
from commands import *
from speaker import speak
from language import is_english
from memory import remember,recall

print("Memory imported successfully")

def get_response(message):
    message = message.lower().strip()
    print(message)
    
    if message.startswith("search"):
        query = message.replace("search ","")
        response = search_google(query)
        speak(response)
        return response
    
    if message == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        response = f"Current Time is {current_time}"
        speak(response)
        return response
        return f"⌚ Current Time: {current_time}"
    
    if "notepad" in message:
        response = open_notepad()
        speak(response)
        return response

    if "chrome" in message:
        response = open_chrome()
        speak(response)
        return response
    
    if "youtube" in message:
        response = open_youtube()   
        speak(response)
        return response
    
    if "github" in message:
        response =  open_github()
        speak(response)
        return response
    
    if "screenshot" in message:
        response = take_screenshot()
        speak(response)
        return response
    
    if "calculator" in message or "calc" in message:
        response = open_calculator()
        speak(response)
        return response
    
    if "date" in message or "today" in message:
        response = get_date()
        speak(response)
        return(response)
    
    if message.startswith("remember my name is"):
        name = message.replace("remember my name is","").strip()
        remember("name",name)
        response = f"Okay bhai ❤️, I will remember your name is {name}."
        speak(response)
        return response
    
    if "what is my name" in message:
        name = recall("name")
        
        if name:
            response = f"Your name is {name}."
            
        else:
            response = "Sorry bhai, mujhe abhi tumhara naam yaad nahi hai."
        speak(response)
        return response
            
    responses_hi = {
        "hello": "Namaste bhai! ❤️",
    "hi": "Haan bhai bolo 😊",
    "thanks": "Koi baat nahi bhai ❤️",
    "bye": "Theek hai bhai, phir milte hain 👋"
}
    
    responses_en = {
    "hello": "Hello Anuj! 👋",
    "hi": "Hi Bro! ❤️",
    "thanks": "You're welcome!",
    "bye": "Bye Anuj! 👋"
}
    if is_english(message):
        response = responses_en.get(
        message,
        "Sorry, I don't know that yet."
    )
    else:
        response = responses_hi.get(
            message,
            "Sorry bhai, ye mujhe abhi nahi aata."
    )

    speak(response)
    return response
    