import playsound
from Brain.AIBrain import ReplyBrain
from Body.Litsen import MicExecution
print("\n>> Starting The Jarvis : Wait For Some Seconds...")
playsound.playsound("wakeup.mp3",False)
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
        elif ValueReturn == None:
            if Data == "":
                continue 
            else:
                Replay = ReplyBrain(Data)
                Speak(Replay)
        else:
            Speak(ValueReturn)           

def ClapDetect():
    query = Tester()
    
    if "True-Mic" in query:
        print("\n>> Clap Detected <<\n")
        MainExecution()
        
    else:
        pass    
Speak("Do Clap")
ClapDetect()