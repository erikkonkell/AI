import os
import random
import glob
import speakManager as sm
musicDir = "D:/Music"
def CPU():
    usage = str(psutil.cpu_percent())
    sm.speak("CPU is at " + usage)

    battery = psutil.sensors_battery()
    try:
        sm.speak("battery is at " + battery.percent)
    except Exception as e:
        sm.speak("You computer does not have battery stats")

def OpenApp():
    sm.speak(pz.userPronoun + " we have not yet implemented this")
    
    # import glob, os
    # def solution():
    # for fn in glob.glob("*_text.exe"):
    #      os.startfile(fn)
    #os.startfile(VARIABLE_WITH_EXE) todo fix this

def Screenshot():
    img = pyautogui.screenshot()
    img.save("D:/Bilder/pythonTest/screenshot.png")

def PlaySong():
    global musicDir
    music = os.listdir(musicDir)
    sm.speak("What would you like to hear?")
    sm.speak("select a number...")
    ans = sm.TakeCommand().lower()
    while("number" not in ans and ans != "random" and ans != "you choose"):
        sm.speak("I could not understand you. Please try again.")
        ans = sm.TakeCommand().lower()
    if "number" in ans:
        no = int(ans.replace("number",""))
    elif "random" or "you choose" in ans:
        no = random.randint(0,len(music)) 
    os.startfile(os.path.join(musicDir,music[no]))

def ChangeMusicDir():
    sm.speak("Sir what map would you like to select?")
    global musicDir 
    musicDir = "D:/Music"
    ans = sm.TakeCommand()
    temp = musicDir + "/" + ans
    if os.path.isdir(temp):
        musicDir = temp
    else:
        sm.speak("the folder could not be selected")
    print(musicDir)