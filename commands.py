import os
import webbrowser
import pyautogui
from datetime import datetime

def open_notepad():
    os.startfile("notepad.exe")
    return "Opening Notepad...📝"

def open_chrome():
    webbrowser.open("https://www.google.com")
    return "Opening Chrome...🌐"

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening Youtube...🎥"

def open_github():
    webbrowser.open("https://www.github.com")
    return "Opening Github...💻"

def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for {query}"

def take_screenshot():
    os.makedirs("screenshot", exist_ok=True)
    filename = os.path.join(
        "screenshot",
        datetime.now().strftime("Screenshot_%Y%m%d_%H%M%S.png")
    )
    pyautogui.screenshot(filename)
    return f"Screenshot saved as {filename}"

def open_calculator():
        os.system("calc")
        return "Opening Calculator... 🧮"
    