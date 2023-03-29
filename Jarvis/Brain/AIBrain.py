from dotenv import load_dotenv
from pychatsonic.chat import ChatSonic

load_dotenv()

def ReplyBrain(question, chat_log=None):
    FileLog = open("DataBase\\chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
    #alternatic key = "" or "3a2c7d89-f35b-4833-8319-90f47f001cb7" or "847c03b5-474b-40f4-8fe2-cbb1801f1a5e"
    chat = ChatSonic("b9aa9dc0-af0a-4d5b-9903-e02f72465cc6", "en")
    
    if chat_log is None:
            chat_log = chat_log_template
            prompt = f'{chat_log}You : {question}\nJarvis :'
            answer = chat.ask(prompt)

    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
#     FileLog = open("DataBase\\chat_log.txt","w")
#     FileLog.write(chat_log_template_update)
#     FileLog.close()
    print(answer)
    return answer
# ReplyBrain("what is the whether in ahmedabad")