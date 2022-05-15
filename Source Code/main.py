
from Wifihackingmenu import *
from Reversshellmenu import *
from Mailattackmenu import *
from Systeminformationmenu import *
from StealingPasswordmenu import *
from Passwordmenu import *

def main():
    print("""

-------------------------------------------------------------------------------                                                                                                                                                                                                                                                                                          
   ,---.   ,--. ,--.         ,--.                   ,-----.                         
  /  O  \  |  | |  | ,-----. `--' ,--,--,  ,-----. '  .-.  ' ,--,--,   ,---.    
 |  .-.  | |  | |  | '-----' ,--. |      \ '-----' |  | |  | |      \ | .-. :    
 |  | |  | |  | |  |         |  | |  ||  |         '  '-'  ' |  ||  | \   --.    
 `--' `--' `--' `--'         `--' `--''--'          `-----'  `--''--'  `----'                                                                                                                       
------------------------------------------------------------------------------                                                                     
(1)Wifi-Hacking - Linux  (x)  
(2)Revers Shell - Linux > Linux / Linux > Windows               
(3)Mail-Attacks - Linux                            
(4)Systeminfomation - Linux/Windows 
(5)Stealing Passwords - Windows (x)            
(6)Cracking / Hashing / Passwordattacks - Linux
(00)Exit
-----------------------------------------------------------------------
        """)

    y = int(input("Enter The number of your Choise >>> "))
    if y == 1:
        Wifihackingmenu(main)
    elif y == 2:
        Reversshellmenu()
    elif y == 3:
        Mailattackmenu()
    elif y == 4:
        Systeminformationmenu()
    elif y == 5:
        StealingPasswordmenu(main)
    elif y == 6:
        Passwordmenu()
    elif y == 00:
        exit
    else:
        print("Not Found")
        main()

if __name__ == "__main__":
    main()