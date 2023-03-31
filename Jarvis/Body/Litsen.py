# Three Functions
# 1 - Listen function
# 2 - English Tranlation
# 3 - Connect

import speech_recognition as sr
from googletrans import Translator #pip install googletrans==3.1.0a0

# 1 = Litsen : Hindi or English or Gujarati

def Litsen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source: # change Microphone(device_index=2) to change devices
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #8 means listening till 8 sec not working then remove 0 and 8
    
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio,language="gu-IN") 
    
    except:
        return ""
    
    query = str(query).lower()
    return query  

#print(Litsen())  

# 2 = Translation

def TranslationGujratiToEnglish(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}")
    return data

# 3 = Connect

def MicExecution():
    query = Litsen()
    data = TranslationGujratiToEnglish(query)
    return data

def Raw_English_Listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source: # change Microphone(device_index=2) to change devices
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #8 means listening till 8 sec not working then remove 0 and 8
    
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio,language="en-IN") 
    
    except:
        return ""
    
    query = str(query).lower()
    return query  