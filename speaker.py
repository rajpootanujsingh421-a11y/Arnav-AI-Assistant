import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",170) #Speaking speed

def speak(text):
    engine.say(text)
    engine.runAndWait()