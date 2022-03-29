import speakManager as sm
import webbrowser as wb
import personalizing as pz
import requests
import wikipedia
import smtplib
import keys

def Location(query):
    query = query.replace("where is", "")
    location = query
    sm.speak("You are asking about " + location)
    wb.open_new_tab("https://www.google.com/maps/place/" + location)


def GoogleSearch():
    sm.speak("What would you like to search for?")
    search = sm.TakeCommand().lower()
    sm.speak("Searching now")
    wb.open_new("https://www.google.com/search?q=" + search)


def YoutubeSearch():
    sm.speak("What would you like to watch")
    search = sm.TakeCommand().lower()
    sm.speak("Searching now")
    wb.open_new("https://www.youtube.com/results?search_query=" + search)


def WikipediaSearch():
    sm.speak("What are you looking for")
    query = sm.TakeCommand()
    sm.speak("Looking it up now ")
    result = wikipedia.summary(query, sentences=3)
    sm.speak("According to Wikipedia")
    sm.speak(result)
    print(result)


def OpenTab():
    sm.speak("What site should I open")
    chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    # chromepath is the location of chrome install
    search = sm.TakeCommand().lower()
    wb.get(chromepath).open_new_tab(search + '.com')


def sendEmail():
    try:
        sm.speak("What should the email say?")
        content = sm.TakeCommand()

        sm.speak("I will need you to type the email adress sir.")
        recivever = input("Enter Email Adress: ")
        sm.speak(content)
        sm.speak("Email has been sent")
        send(recivever, content)
    except Exception as e:
        print(e)
        sm.speak("Unable to send the email.")


def send(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    # for this function, you must enable lowscurit mode
    server.login("bob94.samsson@gmail.com", keys.email_key)
    server.sendmail("bob94.samsson@gmail.com", to, content)
    server.close()


def Weather():
    sm.speak("What city would you like to know the weather of?")
    location = sm.TakeCommand()
    if location == "" or "type" in location or location == "None":
        location = input("type a location: ")
    key = keys.wether_key
    try:
        resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&APPID=' + key)
        data = resp.json()
        weather = data["weather"]
        temperature = int(-273.15 + data["main"]["temp"])
        feelsLike = int(-273.15 + data["main"]["feels_like"])
        wind = getWind(int(data["wind"]["deg"]))
        sm.speak("the current weather is " + weather[0]["description"])
        print("the current weather is " + weather[0]["description"])

        sm.speak("the temperature is " + str(temperature) + " but it feels like its " + str(feelsLike))
        print("the temperature is " + str(temperature) + " but it feels like its " + str(feelsLike))

        sm.speak(wind + " wind at a speed of " + str(data["wind"]["speed"]) + " meters per second")
        print(wind + " wind at a speed of " + str(data["wind"]["speed"]) + " meters per second")

        sm.speak("with a humidity of " + str(data["main"]["humidity"]))
        print("with a humidity of " + str(data["main"]["humidity"]))
    except Exception as e:
        sm.speak("I could not find the wether for " + location)


def getWind(query):
    wind = ""
    if query >= 315 and query <= 45:
        wind += "North"
    if query >= 135 and query <= 225:
        wind += "South"
    if query >= 45 and query <= 135:
        wind += "East"
    if query >= 225 and query <= 315:
        wind += "West"
    return wind
