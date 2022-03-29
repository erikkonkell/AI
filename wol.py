import wolframalpha #https://developer.wolframalpha.com/portal/myapps/
import speakManager as sm
wolframalpha_app_id = "QU44PH-LWPHHWLT73"
def Calculate(query):
    try:
        client = wolframalpha.Client(wolframalpha_app_id)
        index = query.lower().split().index("calculate")
        query = query.split()[index + 1 :]
        res = client.query("".join(query))
        answer = next(res.results).text
        print("the answer is : " + answer)
        sm.speak("the answer is " + answer)
    except: 
        sm.speak("your question could not be calculated")
        print("your question could not be calculated")

def Question(query):
    #wolframalpha api
    client = wolframalpha.Client(wolframalpha_app_id)
    res = client.query(query)
    try:
        print(next(res.results).text)
        sm.speak(next(res.results).text) 
    except StopIteration:
        print("No results")
        sm.speak("No results")