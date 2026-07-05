from datetime import datetime
import os
import webbrowser
from commands import *
from speaker import speak
from language import is_english
from memory import remember,recall
from weather import get_weather
from news import get_news

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
    
    if "weather" in message:
        response = get_weather("Bhopal")
        speak(response)
        return response
    
    if "news" in message:
    
        headlines = get_news()

        if isinstance(headlines, str):
            speak(headlines)
            return headlines

        response = "📰 Top Technology News:\n\n"

        for i, news in enumerate(headlines, 1):
            response += f"{i}. {news}\n\n"
            
        speak("Bhai, aaj ki top technology news suno.")
        return response
    
    if message.startswith("remember"):
        text = message.replace("remember ", "").strip()
        parts = text.split(" is ")
        
        if len(parts)<2:    
            response = "Bhai, mujhe samajh nahi aaya. 'Remember ... is ...' format me bolo."  
            speak(response)
            return response
        
        key = parts[0].strip()
        value = parts[1].strip()
        print("KEY =", key)
        print("VALUE =", value)
        remember(key, value)
        response = f"Okay bhai ❤️, I will remember {key} is {value}."
        speak(response)     
        return response
    
    if message.startswith("what is"):
        text = message.replace("what is ", "").strip()
        key = text
        print("key:", key)
        value = recall(key)
        print("Value:", value)
        if value:
            response = f"Your {key.replace('my ', '')} is {value}."
        else:
            response = "Sorry bhai, mujhe ye yaad nahi hai."
            
        speak(response)
        return(response)

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
    