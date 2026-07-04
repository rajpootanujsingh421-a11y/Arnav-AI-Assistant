from datetime import datetime
import os
import webbrowser
from commands import *
from speaker import speak
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
    
    if message == "open notepad":
        response = open_notepad()
        speak(response)
        return response

    if message == "open chrome":
        response = open_chrome()
        speak(response)
        return response
    
    if message == "open youtube":
        response = open_youtube()   
        speak(response)
        return response
    
    if message == "open github":
        response =  open_github()
        speak(response)
        return response
    
    if "screenshot" in message:
        response = take_screenshot()
        speak(response)
        return response

    responses = {           
        "hello": "Hello Anuj! 👋",
        "hi": "Hi Bhai ❤️", 
        "how are you": "Main mast hoon 😎, tum batao",  
        "thanks": "Always bhai ❤️",
        "bye": "Bye Anuj! Coding mat chhodna. 👊"
    }   
    
    response = responses.get(
        message,
        "Sorry bhai,ye mujhe abhi nahi aata. 😅"
    )
    speak(response) 
    return response