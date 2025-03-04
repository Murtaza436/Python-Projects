import speech_recognition as sr
import webbrowser 
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d35bd7ce0b074c658c3beb9a924d0825"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
        # Parse the JSON response
            data = r.json()
            articles = data.get('articles', [])
            
            # Print the headlines
            print("Top headlines:")
            for i, article in enumerate(articles):
                speak(f"{i + 1}. {article.get('title')}")
    
    else:
        #Let OpenAI handle the request
        #API key is paid
        pass
        
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    # Listen for the wake word "Jarvis"
    while True:
        #obtain audio from microphone
        r = sr.Recognizer()
      
        #recognize speech using Google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word  = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Hello, how can I assist you?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                command  = r.recognize_google(audio)
                
                processCommand(command)
                     
        except Exception as e:
            print("Google Speech error; {0}".format(e))