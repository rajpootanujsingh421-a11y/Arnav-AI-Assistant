def is_english(message):
    
    english_words = [
        "open", "search", "time", "date", "today",
        "hello", "hi", "what", "who", "where",
        "youtube", "chrome", "github", "calculator",
        "screenshot", "thank", "thanks", "bye"
    ]
    
    message = message.lower()
    
    for word in english_words:
        if word in message:
            return True
        
        return False