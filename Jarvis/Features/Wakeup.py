import speech_recognition as sr
import os

def Litsen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #8 means listening till 8 sec not working then remove 0 and 8
    
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio,language="en") 
    
    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query 

def WakeupDetected():
    queery = Litsen().lower()
    
    if "wake up" in queery:
        os.startfile(r"D:\AI\Jarvis\Main.py")
    else:
        pass
        
while True:
    WakeupDetected()   