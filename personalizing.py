import speakManager as sm
import datetime
import time
import pyjokes

username = ""
userPronoun = ""

def wishme():
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        sm.speak("Good Morning " + userPronoun + username)
    elif hour >= 12 and hour < 18:
        sm.speak("Good afterNoon " + userPronoun + username)
    elif hour >= 18 and hour < 24:
        sm.speak("Good Evening " + userPronoun + username)
    else:
        sm.speak("Good Night " + userPronoun + username)

    sm.speak("How may i be of service")

def SaveSettings():
    global username
    global userPronoun
    f = open("settings.txt", "w")
    sm.speak("By what name would I call you?")
    user = "None"
    while user == "None":
        user = sm.TakeCommand()
        username = user
    sm.speak("By what pronoun should i adress you by?")
    userPronoun = sm.TakeCommand()
    if userPronoun == "None":
        userPronoun = ""
    f.write(username + "\n" + userPronoun)
    f.close()
def LoadSettings():
    global username
    global userPronoun
    f = open("settings.txt", "r")
    username = f.readline()
    username = username[:-1]
    userPronoun = f.readline()
    f.close()

def WriteNote():
    sm.speak("What should I write, " + pz.userPronoun)
    notes = sm.TakeCommand()
    file = open("notes.txt", "w")
    sm.speak(pz.userPronoun + " should I include a timestamp?")
    ans = sm.TakeCommand()
    if "yes" in ans or "sure" in ans:
        strTime = datetime.datetime.now().strftime("%h:%M%S")
        file.write(strTime + "\n"+notes)
    else:
        file.write(notes)
    sm.speak("Done taking notes, " + pz.userPronoun)
def ReadNote():
    sm.speak("showing notes")
    file = open("notes.txt", "r")
    print(file.read())
    sm.speak(file.read())

def SetMemory():
    sm.speak("What should I remember?")
    memory = sm.TakeCommand()
    sm.speak("You asked me to remember the following: " + memory)
    remember = open("memory.txt", "w")
    remember.write(memory)
    remember.close()
def GetMemory():
    try:
        remember = open("memory.txt", "r")
        sm.speak("You asked me to remember: " + remember.read())
    except Exception as e:
        sm.speak("Sorry nothing comes to mind")
def StartUp():
    try:
        f = open("settings.txt", "r")
        f.close()
        LoadSettings()
    except Exception as e:
        SaveSettings()
""" test """
def StopListening():
    sm.speak("For how many seconds do you want me to stop listening to your commands?")
    ans = int(sm.TakeCommand())
    time.sleep(ans)
    sm.speak("I am awake")   

def Joke():
    joke = pyjokes.get_joke()
    sm.speak(joke)
    print(joke)