import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

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
