import pyttsx3 # text to speach
import speech_recognition as sr
engine = pyttsx3.init()
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1.0
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language="en-US")
        print (query)
    except Exception as e:
        print("Repet what you said")
        return "None"
    return query