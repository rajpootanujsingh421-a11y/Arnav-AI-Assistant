import os
import webbrowser

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