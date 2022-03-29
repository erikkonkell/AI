import speakManager as sm
import datetime
def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S") #24 Hour clock I for 12 hour
    sm.speak ("The current time is")
    sm.speak(Time)
def date_():
    year =  datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    sm.speak("the  current date is")
    sm.speak(year)
    sm.speak(month) #todo fix month names
    sm.speak(day)
