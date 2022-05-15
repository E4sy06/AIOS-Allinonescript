import platform
import socket
import re
import uuid
import psutil
import smtplib
from email.message import EmailMessage

def Systeminformationmenu():

    def getSystemInfo():
        try:
            info={}
            info['platform']=platform.system()
            info['platform-release']=platform.release()
            info['platform-version']=platform.version()
            info['architecture']=platform.machine()
            info['hostname']=socket.gethostname()
            info['ip-address']=socket.gethostbyname(socket.gethostname())
            info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            info['processor']=platform.processor()
            info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        finally:
            return info


    print ("""
--------------------------------------------------------------------------------------------------------------------------------------------------
 ,---.                       ,--.                      ,--.           ,---.                                       ,--.   ,--.
'   .-'  ,--. ,--.  ,---.  ,-'  '-.  ,---.  ,--,--,--. `--' ,--,--,  /  .-'  ,---.  ,--.--. ,--,--,--.  ,--,--. ,-'  '-. `--'  ,---.  ,--,--,
`.  `-.   \  '  /  (  .-'  '-.  .-' | .-. : |        | ,--. |      \ |  `-, | .-. | |  .--' |        | ' ,-.  | '-.  .-' ,--. | .-. | |      \
.-'    |   \   '   .-'  `)   |  |   \   --. |  |  |  | |  | |  ||  | |  .-' ' '-' ' |  |    |  |  |  | \ '-'  |   |  |   |  | ' '-' ' |  ||  |
`-----'  .-'  /    `----'    `--'    `----' `--`--`--' `--' `--''--' `--'    `---'  `--'    `--`--`--'  `--`--'   `--'   `--'  `---'  `--''--'
         `---'
--------------------------------------------------------------------------------------------------------------------------------------------------
(1)Print Systeminformation
(2)Mail Systeminformation
(3)Safe Systeminformation
(00)Back
--------------------------------------------------------------------------------------------------------------------------------------------------
    """)

    g = int(input("Enter The number of your Choise >>> "))
    if g=="1":
        var = getSystemInfo()
        print(var)
    if g=="2":
        print ("What is your Gmail-Adress >>> ")
        Gmail_login_name = (input(""))
        print ("What is your Gmail-Account-Password >>> ")
        Gmail_Password = (input(""))
        print ("Which Sender shoud used in the mail >>> ")
        Sender = (input(""))
        print ("How shoud received the mail >>> ")
        Emailadress = (input(""))
        Subject = "Systeminformation"
        #Sending a Mail with a File or a Link to a HTTP - Server
        # Erstellen Sie die Nachricht für die E-Mail
        while email_message!="exit":
            print ("""Enter your message, if you are fineshed type "exit" >>> """)
            email_message = (input(""))

        # EmailMessage-Objekt erstellen
        email = EmailMessage()
        # Von wem ist die E-Mail?
        email["from"] = Sender
        # An welche E-Mail Sie die E-Mail senden möchten
        email["to"] = Emailadress
        # Betreff der E-Mail
        email["subject"] = Subject
        email.set_content(email_message)

        # smtp-Server erstellen
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            # Sichere Verbindung zum Server
            smtp.starttls()
            # Melden Sie sich mit Benutzernamen und Passwort an einer Dummy-E-Mail an. Denken Sie daran, E-Mail so einzustellen, dass weniger sichere Apps zugelassen werden, wenn Sie Gmail verwenden.
            smtp.login(Gmail_login_name, Gmail_Password)
            # E-Mail senden.
            smtp.send_message(email)
        Systeminformationmenu()

    if g=="3":
        myfile = "Systeminformation.txt"
        information = getSystemInfo()
        with open(myfile, "w") as f:
            f.write(information)
        print("File is saved")

    else:
        Systeminformationmenu()
