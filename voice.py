import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("you said:",text)
        return text.lower()
    except sr.UnknownValueError:
        return None
    
    except sr.RequestError:
        return None
        