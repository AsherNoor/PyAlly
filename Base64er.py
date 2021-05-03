"""
--------------
| The PyAlly |
--------------
| Base64 -er |
--------------
"""

import base64
import _pyally_main as pyally




#-- To ENCODE what is typed into Standard Base64
def nkoder():
    awords = input("Enter your sentence: ")
    awords_bytes = awords.encode('ascii')
    theEncoded = base64.standard_b64encode(awords_bytes)
    print(theEncoded.decode("utf-8"))
    internal_loop()


#-- To DECODE what is typed into standard English
def dkoder():
    bwords = input("Paste your Base64: ")
    theDecoded = base64.standard_b64decode(bwords)
    print(theDecoded.decode("utf-8"))
    internal_loop()




#-- Internal Loop Function
def internal_loop():
    loop_answer = input("\nBack to the Base64-er Menu? [y/n] : ")
    if loop_answer.lower()== 'y':
        b64_menu()
    else:
        pyally.mini_menu()


# -- The Base64 -er Menu
def b64_menu():
    print("""
--------------
| Base64-er  |
--------------------------------------------------------
| To help you convert text TO and FROM standard Base64 |
--------------------------------------------------------
[1] : Encode.
[2] : Decode.
[3] : PyAlly Menu.
[4] : Exit PyAlly.
    """)
    menu_answer = int(input("What is your option?: "))
    if menu_answer == 1:
        nkoder()
    elif menu_answer == 2:
        dkoder()
    elif menu_answer == 3:
        pyally.pyally_menu()
    else:
        pyally.outro()



'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    b64_menu()