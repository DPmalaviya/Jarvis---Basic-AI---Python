import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from Body.Speak import Speak
from Body.Litsen import Raw_English_Listen

def OpenExe(Query):
    Query = str(Query)
    
    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        cls_web = Nameofweb.replace(" ","")
        Link = f"{cls_web}.com"
        webbrowser.open(Link)
        return True
    elif "open" in Query:
        Nameofapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    elif "start" in Query:
        Nameofapp = Query.replace("start ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        cls_web = Nameofweb.replace(" ","")
        Link = f"{cls_web}.com"
        webbrowser.open(Link)
        return True
    #spotify song play
    elif 'play' in Query:
        
        while True:    
            Speak('Sir what song should i play...')
            song = Raw_English_Listen()
            if song != "":
                Speak('Playing some music for you now. Enjoy!')
                break
        
        webbrowser.open(f'https://open.spotify.com/search/{song}')
        sleep(6)
        pyautogui.doubleClick(x=975, y=383)
        # for taking x and y value f screen
        # import pyautogui
        # from time import sleep
        # sleep(1)
        # kkk = pyautogui.position()
        # print(kkk)
        Speak('Playing ' + song)
        return True
    
    # elif 'play' in Query or 'can you play' in Query or 'please play' in Query:
    #     Speak("OK! here you go!!")
    #     Query = Query.replace("play", "")
    #     Query = Query.replace("could you play", "")
    #     Query = Query.replace("please play", "")
    #     webbrowser.open(f'https://open.spotify.com/search/{Query}')
    #     sleep(10)
    #     pyautogui.click(x=1055, y=617)
    #     print('Enjoy! ' + Query)
    #     Speak("Enjoy Sir!!") 
    #     return True    
