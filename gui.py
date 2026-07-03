import tkinter as tk
from assistant import get_response
from voice import listen


def start_app():

    root = tk.Tk()

    root.title("Arnav AI Assistant")
    root.geometry("900x600")
    root.configure(bg="#1e1e1e")


    def send_message():

        message = message_entry.get()

        if message == "":
            return

        chat_box.insert(tk.END, f"You : {message}\n")

        response = get_response(message)

        chat_box.insert(tk.END, f"Arnav : {response}\n\n")

        message_entry.delete(0, tk.END)
        
    def voice_command():
        command = listen()
    
        if command:
            chat_box.config(state="normal")
            chat_box.insert(tk.END,f"👤 You: {command}\n")
            response = get_response(command)
            chat_box.insert(tk.END, f"🤖 Arnav: {response}\n\n")
            chat_box.config(state="disabled")
            chat_box.see(tk.END)


    title = tk.Label(
        root,
        text="🤖 ARNAV AI ASSISTANT",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#1e1e1e"
    )

    title.pack(pady=20)


    chat_box = tk.Text(
        root,
        width=80,
        height=20,
        font=("Arial", 12),
        bg="#2d2d2d",
        fg="white"
    )

    chat_box.pack(pady=10)
    
    chat_box.insert(
        tk.END,
        "🤖 Arnav:\n"
        "Hello Anuj! 👋\n\n"
        "Main Arnav hoon.\n"
        "Tumhara Personal AI Assistant.\n\n"
        "Aaj kya banana hai? 😎\n\n"
    )


    message_entry = tk.Entry(
        root,
        width=60,
        font=("Arial", 12)
    )

    message_entry.pack(side="left", padx=20, pady=20)
    message_entry.bind("<Return>",lambda event: send_message())
    
    send_button = tk.Button(
        root,
        text="Send",
        font=("Arial", 12),
        command=send_message
    )
    
    send_button.pack(side="left")
    
    mic_button = tk.Button(
        root,
        text ="🎤",
        font =("Arial",14),
        command=voice_command
    )    
    
    mic_button.pack(side="left",padx=10)

    root.mainloop()