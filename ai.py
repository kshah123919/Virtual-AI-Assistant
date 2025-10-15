import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_long_text(text, chunk_size=200):
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        engine.say(chunk)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception:
        print("Say that again please..")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '').strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                print("Wikipedia summary:", results)
                speak("According to Wikipedia")
                speak_long_text(results)
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I couldn't find any results for your query.")

            time.sleep(5)  # optional small pause
            break  # break after speaking completes
        # Add other command handlers here

