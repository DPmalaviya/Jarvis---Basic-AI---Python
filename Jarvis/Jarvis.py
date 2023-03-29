from Brain.AIBrain import ReplyBrain
from Body.Litsen import MicExecution
print("\n>> Starting The Jarvis : Wait For Some Seconds...")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> .. Jarvis Is Started .. <<")
from Main import MainTaskExecution

def MainExecution():
    
    Speak("Hello Dhruvik")
    Speak("I'm Jarvis , I'm Ready to Assist You")
    
    while True:
        Data = MicExecution()
        Data = str(Data)
        
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn == True:
            pass
        elif Data == "":
            continue 
        else:
            Replay = ReplyBrain(Data)
            Speak(Replay)   

def ClapDetect():
    query = Tester()
    
    if "True-Mic" in query:
        print("\n>> Clap Detected <<\n")
        MainExecution()
        
    else:
        pass    
Speak("Do Clap")
ClapDetect()