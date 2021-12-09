print("""Hii This is Jarvis Created by Aditya Class BCA 1st year and you can give any command to Him he will definatly help you If you have any qurey please contact me 
 """)


import datetime
from ntpath import join
import pyttsx3
import speech_recognition as sr
import os
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12 :
        speak("Good Morning Sir!")
        print("Good Morning Sir!")
    elif hour >=12 and hour<18 :
        speak("Good Afternoon Sir!")
        print("Good Afternoon Sir!")
    else:
        speak("Good Evening")
        print("Good Evening")
    speak("I am Artificial Intelligent VERSION 2.O Sir Tell me how may I help you")
    print("I am Artificial Intelligent Sir Tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing......!")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e :
        
        print("Say That Again....Please")
        return "None"
    return query





if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "open youtube" in query:
            webbrowser.open("youtube.com")

        if "open google" in query:
            webbrowser.open('google.com')
        if """ hi
            hello
            how are you""" in query:
            speak("File Sir")

        if "play music" in query:
            music_dir = input("Please Give a specific directory of your music: ")
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is : {strTime}\n")

        if "open file" in query:
            filepath = input("Please Give a Specific File Path To be open ")
            os.startfile(filepath)

        