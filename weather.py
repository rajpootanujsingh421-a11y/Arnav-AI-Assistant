import requests

API_KEY = "f53a2185f09833e898a57734ddad2711"

def get_weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != 200:
        return "Bhai, city nahi mili."
    
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    
    return f"{city} me abhi {temperature}°C hai aur {description} hai."

print(get_weather("Bhopal"))