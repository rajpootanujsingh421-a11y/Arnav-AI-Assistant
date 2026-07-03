from voice import listen

while True:
    
    command = listen()
    if command:
        print(command)