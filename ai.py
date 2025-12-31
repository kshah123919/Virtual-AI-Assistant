import speech_recognition as sr
import datetime
import wikipedia
import time
import webbrowser
import os
import win32com.client
import pyjokes


speaker = win32com.client.Dispatch("SAPI.SpVoice")


def speak(text):
    
    speaker.Speak(text)


def speak_long_text(text, chunk_size=200):
    
    for i in range(0, len(text), chunk_size):
        speaker.Speak(text[i:i + chunk_size])


def wishme():
    
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Friday. Please tell me how may I help you")


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except Exception:
        return "None"


def calculate(expression):
    """Perform basic voice-based calculations"""
    try:
        expression = (expression
                      .replace("plus", "+")
                      .replace("minus", "-")
                      .replace("times", "*")
                      .replace("divided by", "/"))
        result = eval(expression, {"__builtins__": None}, {})
        return f"The result is {result}"
    except Exception:
        return "Sorry, I couldn't calculate that."


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()

        if query == "none" or query.strip() == "":
            continue

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            topic = query.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia")
                speak_long_text(result)
            except Exception:
                speak("Sorry, I couldn't find information.")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'the time' in query:
            time_now = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {time_now}")

        elif 'tell a joke' in query:
            speak(pyjokes.get_joke())

        elif 'calculate' in query:
            speak("Please say the expression")
            expression = takeCommand().lower()
            speak(calculate(expression))

        
        elif 'shutdown the system' in query:
            speak("Shutting down the system")
            
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            speak("Restarting the system")
            
            os.system("shutdown /r /t 5")

        elif 'lock the system' in query:
            speak("Locking the system")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        else:
            speak("Sorry, I didn't understand that command.")