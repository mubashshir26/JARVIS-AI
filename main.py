import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "b06dcba594564fd3b34614a353708a5c"

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice input
def recognize_speech():
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
            command = recognizer.recognize_google(audio).lower()
            status_label.config(text="Processing...")
            return command
        except sr.UnknownValueError:
            status_label.config(text="Could not understand audio.")
            return ""
        except sr.RequestError:
            status_label.config(text="Speech service down.")
            return ""
        except Exception as e:
            status_label.config(text=f"Error: {e}")
            return ""


def process_command(command):
    output_area.config(state='normal')
    output_area.insert(tk.END, f"User: {command}\n")
    
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
        response = "Opening Google..."
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com/feed/")
        response = "Opening LinkedIn..."
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube..."
    elif command.lower().startswith("play"):
        try:
            song = command.lower().split(" ")[1]
            link = musiclibrary.music[song]
            webbrowser.open(link)
            response = f"Playing {song}..."
        except KeyError:
            response = "Song not found in the music library."
    elif "news" in command.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                output_area.insert(tk.END, "Jarvis: Latest News Headlines:\n")
                for article in articles[:5]:  # Limit to 5 headlines for brevity
                    headline = article['title']
                    output_area.insert(tk.END, f"- {headline}\n")
                    speak(headline)
                output_area.config(state='disabled')
                return  # Skip the default response since news is handled
            else:
                response = "Failed to fetch news."
        except Exception as e:
            response = f"Error fetching news: {e}"
    elif "exit" in command.lower():
        response = "Goodbye!"
        output_area.insert(tk.END, f"Jarvis: {response}\n")
        output_area.config(state='disabled')
        speak(response)
        window.quit()
        return
    else:
        response = "Sorry, I didn't understand that command."
    
    output_area.insert(tk.END, f"Jarvis: {response}\n")
    output_area.config(state='disabled')
    speak(response)

# Function to handle text input
def handle_text_input():
    command = input_box.get().strip().lower()
    input_box.delete(0, tk.END)
    if command:
        process_command(command)

# Function to handle voice input
def handle_voice_input():
    command = recognize_speech()
    if command:
        process_command(command)
    status_label.config(text="Ready")

# Create the main window
window = tk.Tk()
window.title("Jarvis AI Assistant")
window.geometry("600x500")
window.configure(bg="#2c3e50")  # Dark background

# Title Label
title_label = tk.Label(window, text="Jarvis AI Assistant", font=("Helvetica", 20, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=10)

# Output Area (Chat Display)
output_area = scrolledtext.ScrolledText(window, height=15, width=60, font=("Arial", 12), bg="#34495e", fg="#ecf0f1", wrap=tk.WORD)
output_area.pack(pady=10)
output_area.config(state='disabled')

# Input Area
input_frame = tk.Frame(window, bg="#2c3e50")
input_frame.pack(pady=5)

input_box = tk.Entry(input_frame, width=40, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
input_box.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(input_frame, text="Send", font=("Arial", 12, "bold"), bg="#3498db", fg="#ecf0f1", command=handle_text_input)
send_button.pack(side=tk.LEFT, padx=5)

# Voice Input Button
voice_button = tk.Button(window, text="Speak to Jarvis", font=("Arial", 12, "bold"), bg="#e74c3c", fg="#ecf0f1", command=handle_voice_input)
voice_button.pack(pady=5)

# Status Label (for voice input feedback)
status_label = tk.Label(window, text="Ready", font=("Arial", 10), bg="#2c3e50", fg="#ecf0f1")
status_label.pack(pady=5)

# Clear and Exit Buttons
button_frame = tk.Frame(window, bg="#2c3e50")
button_frame.pack(pady=5)

clear_button = tk.Button(button_frame, text="Clear Chat", font=("Arial", 12, "bold"), bg="#95a5a6", fg="#ecf0f1", command=lambda: output_area.delete(1.0, tk.END))
clear_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12, "bold"), bg="#c0392b", fg="#ecf0f1", command=window.quit)
exit_button.pack(side=tk.LEFT, padx=5)

# Add keyboard shortcut for sending text input
input_box.bind("<Return>", lambda e: handle_text_input())

# Speak initialization message
speak("Initializing Jarvis...")

# Start the application
window.mainloop()