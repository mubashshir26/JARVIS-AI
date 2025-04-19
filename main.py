import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "b06dcba594564fd3b34614a353708a5c"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com/feed/")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])

    else: 
        pass 

if __name__ == "__main__":
    speak("Initializing jarvis......")
    while True:
        # listen for the wake word 'jarvis'
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("yes")
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=4)
                    command = r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print("error; {}".format(e))
