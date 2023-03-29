# 2 Speak function

# Windows Based pip install pyttsx3
# Chrome Based pip install selenium==4.1.3


# windows Based
import pyttsx3

def Speak(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    print(f"\nYou : {Text}.\n")
    engine.say(Text)
    engine.runAndWait()   
    
#Speak("Hello sir")
 
# Chrome Based
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "DataBase\\chromedriver.exe" 
driver = webdriver.Chrome(Path,options = chrome_options)
driver.maximize_window()


website = "https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by = By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('US English / Matthew')

def Speak(Text):
    
    lengthToText = len(str(Text))
    
    if lengthToText == 0:
        pass
    
    else:
        print(f"\nJarvis : {Text}\n")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH , value = xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH , value = '//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH , value = xpathofsec).clear() #if not work then add xpathofsec value in it.
        
        if lengthToText >= 30:
            sleep(4)
         
        elif lengthToText >= 40:
            sleep(6)  
        
        elif lengthToText >= 55:
            sleep(8) 
            
        elif lengthToText >= 70:
            sleep(10) 
        
        elif lengthToText >= 100:
            sleep(13)    
        
        elif lengthToText >= 120:
            sleep(14)
               
        else:
            sleep(2)    
            
#Speak("hello jarvis how are you?")                      
