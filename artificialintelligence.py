import pyttsx3     #to listen audio
import datetime
import os
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!!!")
    speak("I AM CHITTTI,PLEASTE TELL ME HOW CAN I HELP YOU")

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again...")
        return "None"
    return query


if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strftime}")

        elif 'open vs code' in query:
            codepath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'Prakhar' in query:
            codepath="C:\\Users\\hp\\Desktop"
            os.startfile(codepath)