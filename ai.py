import speech_recognition as sr
import datetime
import wikipedia
import time
import webbrowser
import os
import win32com.client
import webbrowser
import pyjokes
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    speaker.Speak(text)

def speak_long_text(text, chunk_size=200):
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        speaker.Speak(chunk)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Friday sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query
def calculate(expression):
    try:
        expression=expression.replace("plus","+").replace("minus","-").replace("times","*").replace("divided by","/")
        result=eval(expression,{"__builtins__":None},{})
        return f"The result is {result}"
    except Exception as e:
        return "Sorry sir,I couldn't calculate that."
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
            time.sleep(5)
            break

        elif 'open google' in query:
            try:
                speak("Opening Google, sir.")
                webbrowser.open("https://www.google.com")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I couldn't open Google.")
            time.sleep(5)
            break

        elif 'open youtube' in query:
            try:
                speak("Opening YouTube, sir.")
                webbrowser.open("https://www.youtube.com")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I couldn't open YouTube.")
            time.sleep(5)
            break

        elif 'play music' in query:
            try:
                speak("Playing music sir")
                music_dir = "C:\\Users\\Administrator\\Downloads\\2nd year\\songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I couldn't play music.")

        elif 'the time' in query:
            try:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                print(f'Telling time: {strTime}')
                speak(f'Sir, the time is {strTime}')
            except Exception as e:
                print('Error:', e)
                speak("Sorry, I couldn't tell the time.")
        elif 'open code' in query:
            try:
                codePath="C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            except Exception as e:
                print('Error:', e)
                speak("Sorry, I couldn't open the code.")
                
        elif 'email to krish' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                if content.lower() == "none" or content.strip() == "":
                    speak("Sorry sir, I didn't catch that message.")
                else:
                    to = "krishshah062021@gmail.com"  # <-- replace with your actual email
                    speak("Opening Gmail to send the email.")
                    webbrowser.open(f"https://mail.google.com/mail/?view=cm&fs=1&to={to}&su=Message%20from%20Friday&body={content}")
                    speak("Your message is ready in Gmail, sir. Please click send.")
            except Exception as e:
                print("Error:", e)
                speak("Sorry sir, I couldn't open Gmail or send the email.")
           

        elif 'shutdown the system' in query:
            try:
                speak("Shutting down the system, sir.")
                os.system("shutdown /s /t 5")
            except Exception as e:
                print("Error:",e)
                speak("Sorry sir ,I wasn’t able to shutdown the system")
            
        
        elif 'restart the system' in query:
            try:
                speak("restarting the system ,sir")
                os.system("shutdown /r /t 5")
            except Exception as e:
                print("Error:",e)
                speak("Sorry sir ,I wasn’t able to restart the system")

        elif 'lock the system' in query:
            try:
                speak("locking the system ,sir")
                os.system("rundll32.exe user32.dll,LockWorkStation")
            except Exception as e:
                print("Error:",e)
                speak("Sorry sir ,I wasn’t able to lock the system")

        elif 'tell a joke' in query:
            try: 
                joke = pyjokes.get_joke()
                speak(joke)
            except Exception as e:
                print("Error:",e)
                speak("Sorry sir ,I can't tell a joke")
        elif 'calculate' in query:
                speak("Please say the math expression you want to calculate ")
                expression=takeCommand().lower()
                expression=expression.replace("calculate", "").strip()
                result=calculate(expression)
                print(result)
                speak(result)
        else:  
            speak("Sorry sir, I didn't understand that command.")
