import speakManager as sm
from urllib.request import urlopen #newsapi
import json

def SearchWithATopic():
    try:
        sm.speak("tell me a topic and i will find the top news for it")
        question = sm.TakeCommand()
        question = question.replace(" ","%20")
        jsonObj = urlopen("https://newsapi.org/v2/everything?q="+question+"&language=en&sortBy=popularity&apiKey=0de944b463394c58ae669756921a54f7")
        data = json.load(jsonObj)
        i = 1
        sm.speak("Here are some top headlines")
        print("==========TOP HEADLINES=========\n")
        for item in data["articles"]:
            if item["description"]:
                print(str(i) + ". " + item["title"]+"\n")
                print(str(item["description"]+"\n"))
                print(str(item["url"]+"\n"))
                sm.speak(str(item["title"]))
                i += 1
    except Exception as e:
        print(str(e))

