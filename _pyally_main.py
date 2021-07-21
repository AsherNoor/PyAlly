"""

-------------------------------
| PROGRAM NAME: The PyAlly .  |
| Version #:  002 .           |
| DATE:  July 2021.           |
------------------------------
--------------------------------------------------------------------
| UPDATES                                                         |
|                                                                 |
| Wordlister:                                                     |
| +Using a different library (pdfplumber).                        |
| +This improved the functionality of the program.                |
|                                                                 |
| PTE:                                                            |
| +Using a different library (pdfplumber).                        |
| +This improved the functionality of the program.                |
| +Added a "Decrypt" option. Only works if you have the password. |
--------------------------------------------------------------------


----------------------------------
| CONTRIBUTORS |                 |
----------------                 |
| Ash Noor (ryn0f1sh)            |
| Site: www.AshNoor.me           |
| Email: ryn0f1sh@protonmail.com |
| Blog: www.ryn0f1sh.blog        |
----------------------------------


-------------------------------------------------------------
| [bini-tek] learn \ make \ share |                         |
-----------------------------------                         |
| A tech group for niche and passion project actualization. |
| Site: www.binitek.com                                     |
| Email: binitek.baltimore@gmail.com                        |
| Discord: Home of bini-tek (https://discord.gg/4GqDrH)     |
| [-]\\                                                     |
-------------------------------------------------------------

"""

# -- IMPORTS --

from time import sleep
import Base64er
import Leeter
import CHMODHelper
import IMAGEgraber
import HACKERHelper
import PTE
import Wordlister


# -- The Main Menu to all the programs --
def pyally_menu():
    print("""
--------------
| The PyAlly |
--------------
--------------
| MAIN MENU  |
--------------
[1]: PDF Text Extractor..[Gives you a text file of your PDF] 
[2]: Wordlister..........[Gives you a wordlist of your file]
[3]: Hacker Helper.......[Gives you a file of CTF Commands]
[4]: Base64-er...........[Encoder / Decoder]
[5]: CHMOD Helper........[File Permission Codes]
[6]: Image Graber........[Downloads images for you]
[7]: Leet-er.............[l33t & Text Converter]
[8]: Exit PyAlly.

""""")
    sleep(1)
    # -- UI : Choice of the menu
    ui_pymenu = int(input("Make Your Selection: "))

    # -- Sorting through the menu
    if ui_pymenu == 1:
        PTE.pte_menu() #-- PDF Text Extractor Menu
    elif ui_pymenu == 2:
        Wordlister.wl_menu() #-- Wordlister Menu
    elif ui_pymenu == 3:
        HACKERHelper.hh_menu() #-- Hacker Helper Menu
    elif ui_pymenu == 4:
        Base64er.b64_menu() #-- Base64 Menu
    elif ui_pymenu == 5:
        CHMODHelper.chmod_menu() #-- CHMOD Menu
    elif ui_pymenu == 6:
        IMAGEgraber.ig_menu() #-- Image Grabber Menu
    elif ui_pymenu == 7:
        Leeter.leeter_menu() #-- Leeter Menu
    else:
        outro()

# --- End of PyAlly Main Menu Function --





#-- PyAlly Mini Menu --

def mini_menu():
    mm_answer = int(input("""
PyAlly Mini Menu:
(1): PyAlly Menu.
(2): Exit PyAlly.
Please select one:  """))
    if mm_answer == 1:
        pyally_menu()
    else:
        outro()

# --- End of PyAlly Mini Menu --






# -- The Run Again Function --

def run_again():
    # Getting the Y/N answer.
    yn_answer = input("\n\nAnother Selection? y/n : " )
    if (yn_answer.lower() == 'y'):
       # -- Call the Main Menu
       pyally_menu()

       # -- This Loop Call is just for the template.
       #run_again()
    else:
        #-- Call the Outro function.
        outro()

# --- End of Run Again Function --








#-------------------------
# -- The Outro Function --
def outro():

    print("\nExiting Program, please wait.")
    sleep(2)

    ryno_signature = """
                        ___   __ __     _     
     coded by:         / _ \ / _/_ |   | |    
      _ __ _   _ _ __ | | | | |_ | |___| |__  
     | '__| | | | '_ \| | | |  _|| / __| '_ \ 
     | |  | |_| | | | | |_| | |  | \__ \ | | |
     |_|   \__, |_| |_|\___/|_|  |_|___/_| |_|
            __/ |                             
           |___/      ryn0f1sh@protonmail.com
                      ryn0f1sh.blog

    """

    print(ryno_signature)
    # -- Any Key to Exit --
    input("\n\n\t>->-> [ Please press ENTER key to Exit ] <-<-<")
# --- End of Outro Function --
#-----------------------------





"""
Calling The functions here.
- I only need to call the Intro ()
- Intro () will call the program's main function.
- The others are embedded within that.
"""

'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    pyally_menu() #-- PyAlly Main Menu.
    #run_again()


