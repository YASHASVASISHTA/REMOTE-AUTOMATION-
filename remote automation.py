import imapclient,pyzmail,webbrowser,subprocess,pyautogui,threading,time,os,datetime
import yagmail as email
import pywhatkit as kit

def get_email():
    
    dict={'Chrome':"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"}
    server=imapclient.IMAPClient('imap.gmail.com',ssl=True)
    server.login('#gmail','#gmailapp password')
    server.select_folder('INBOX',readonly=False)
    UIDs=server.search(['FROM' ,'#persons gmail '])
    print(UIDs)
    instructions=[]
    for uid in UIDs:
        rawMessage=server.fetch(uid,['BODY[]','FLAGS'])
        message=pyzmail.PyzMessage.factory(rawMessage[uid] [b'BODY[]'])
    
        if message.text_part != None:
            print(message.text_part.get_payload().decode(message.text_part.charset))
            instructions.append(message.text_part.get_payload().decode(message.text_part.charset))
            
    server.delete_messages(uid)
    server.logout()
   

    for instruction in instructions:
        print(instruction.split())
        for instruct in instruction.split():
            print(instruct)
            if 'torrent' in str(instruct) or str(instruct).startswith("magnet:?"):
                torrent=subprocess.Popen(["C:\Program Files\qBittorrent\qbittorrent.exe",str(instruct)])

                if torrent.poll() == None:
                    print('Process is still running')
                    time.sleep(10)
                    pyautogui.press('enter')
                    send_confirmation('qBittorrent',f"qBittorrent is up and running.")

            
                
            
            for app in dict.keys():
                
                if "Openall:" in instruct :
                    application=subprocess.Popen(dict[app])
                    if application.poll()== None:
                        print("Process running succesfully")
                        send_confirmation(app,f"{app} is up and running: {app} is online!!!")
                        
                if  "chrome" in instruct.lower() :
                    application=subprocess.Popen(dict[app])
                    if application.poll()== None:
                        print("Process running succesfully")
                        send_confirmation(app,f"{app} is up and running: {app} is online!!!!")
              
                
        
   
        
    
def send_confirmation(process,body,attachment=None):
    login=email.SMTP('#','#')
    if attachment:
        login.send(to='#',subject=f"{process} is running.",contents=body)
    else:
        login.send(to='#',subject=f"{process} is running.",contents=body,attachments=attachment)
    login.close()
           

get_email()
