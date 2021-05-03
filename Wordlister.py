"""
--------------
| The PyAlly |
--------------
| Wordlister |
--------------
"""


from time import sleep

#-- My custom function.
import PDFfunction as PDE
import TEXTfunction as TDE
import _pyally_main as pyally





# -- The Intro Function --
def wl_menu():
    print("""
---------------
| Wordlister  |
------------------------------------------------------------------------------
| Creates a wordlist with no duplicates or numbers out of a Text or PDF file.|
------------------------------------------------------------------------------    
""")

    # -- Call the File Choice function to start the program.
    fileChoice()

# --- End of Intro Function --






# -- The fileChoice Function here --
def fileChoice ():
    #-- info for user
    print("PLEASE NOTE: "
          "\nMake sure the file you are extracting is the same folder as PyAlly: Wordlister.")
    sleep(2)

    #-- The Menu of File Types..
    print("\n-----------"
          "\n| M E N U |"
          "\n-----------"
          "\n[1]: Text (.txt) File."
          "\n[2]: PDF (.pdf) File.")

    #-- UI: The type of file.
    sleep(1)
    file_type = int(input("What type of file are you using?: "))

    #-- Analysing the UI.
    if (file_type == 1):
        TDE.text_extractor()
    elif (file_type == 2):
        PDE.pdf_extractor()
    else:
        print("No such choice")

    internal_loop()

# -- End of File Choice Function --





#-- Internal Loop Function --

def internal_loop():
    loop_answer = input("\nMake another Wordlist? [y/n] : ")
    if loop_answer.lower()== 'y':
        fileChoice()
    else:
        pyally.mini_menu()

# --- End of Internal loop Function --









# The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    wl_menu()
