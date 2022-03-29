# all are pip installs
import pyautogui
import python_weather
# standard libs
import smtplib
import asyncio

# myscripts
import News
import speakManager as sm
import web
import personalizing as pz
import OS
import TimeInfo as ti
import wol


def main():
    pz.StartUp()
    pz.wishme()
    while True:
        query = sm.TakeCommand().lower()
        if 'time' in query:  # tell the time
            ti.time_()
        elif "date" in query:  # tell the date
            ti.date_()
        elif "search wikipedia" in query:
            web.WikipediaSearch()
        elif "send email" in query:
            web.sendEmail()
        elif "open tab" in query:
            web.OpenTab()
        elif "search youtube" in query:
            web.YoutubeSearch()
        elif "search google" in query:
            web.GoogleSearch()
        elif "rename me" in query:
            pz.SaveSettings()
        elif "cpu" in query:
            OS.CPU()
        elif "joke" in query:
            pz.Joke()
        elif "open program" in query:
            OS.OpenApp()
        elif "write a note" in query:
            pz.WriteNote()
        elif "show note" in query:
            pz.ReadNote()
        elif "screenshot" in query:
            OS.Screenshot()
        elif "play music" in query:
            OS.PlaySong()
        elif "change music folder" in query:
            OS.ChangeMusicDir()
        elif "remember that" in query:
            pz.SetMemory()
        elif "do you remember anything" in query:
            pz.GetMemory()
        elif "where is" in query:
            web.Location(query)
        elif "news" in query:
            News.SearchWithATopic()
        elif "calculate" in query:
            wol.Calculate(query)
        elif "what is" in query or "who is" in query:
            wol.Question(query)
        elif "stop listening" in query:
            pz.StopListening()
        elif "weather" in query:
            web.Weather()
        elif "quit" in query:
            sm.speak("shutting down " + pz.userPronoun)
            quit()
        elif "log out" in query:
            OS.system("shutdown -l")
        elif "restart" in query:
            OS.system("shutdown /r /t 1")
        elif "shutdown" in query:
            OS.system("shutdown /s /t 1")


if __name__ == "__main__":
    main()
