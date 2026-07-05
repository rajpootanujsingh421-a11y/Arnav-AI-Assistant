import requests

API_KEY = "c6f1161955ca4b37832d8b32d5579cb9"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if data["status"] != "ok":
        return "Bhai, news nahi mil pa rahi."
    
    headlines = []
    
    for article in data["articles"][:5]:
        headlines.append(article["title"])
        
    return headlines
