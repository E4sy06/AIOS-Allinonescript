from Chromepasswordstealing import *
from Wifipasswordsstealing import *
from GettingSearchHistory import *

def StealingPasswordmenu(nameofthemainclass):

    print("""
-----------------------------------------------------------------------------------------------------------------------------------------------------
 ,---.     ,--.                    ,--. ,--.                      ,------.                                                          ,--.
'   .-'  ,-'  '-.  ,---.   ,--,--. |  | `--' ,--,--,   ,---.      |  .--. '  ,--,--.  ,---.   ,---.  ,--.   ,--.  ,---.  ,--.--.  ,-|  |  ,---.
`.  `-.  '-.  .-' | .-. : ' ,-.  | |  | ,--. |      \ | .-. |     |  '--' | ' ,-.  | (  .-'  (  .-'  |  |.'.|  | | .-. | |  .--' ' .-. | (  .-'
.-'    |   |  |   \   --. \ '-'  | |  | |  | |  ||  | ' '-' '     |  | --'  \ '-'  | .-'  `) .-'  `) |   .'.   | ' '-' ' |  |    \ `-' | .-'  `)
`-----'    `--'    `----'  `--`--' `--' `--' `--''--' .`-  /      `--'       `--`--' `----'  `----'  '--'   '--'  `---'  `--'     `---'  `----'
-----------------------------------------------------------------------------------------------------------------------------------------------------
(1)Chromepasswords - Windows
(2)Wifipasswords - Windows
(3)Search-History  - Windows
(00)Back
-----------------------------------------------------------------------
        """)

    b = int(input("Enter The number of your Choise >>> "))
    if b == 1:
        Chromepasswordstealing()
    elif b == 2:
        Wifipasswordsstealing()
    elif b == 3:
        GettingSearchHistory()
    elif b == 00:
        nameofthemainclass()
    else:
        print("Not Found")
        StealingPasswordmenu()
