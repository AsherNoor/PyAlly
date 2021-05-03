"""
--------------
| The PyAlly |
--------------
| Leet-er |
-----------
"""


import sys
import _pyally_main as pyally

# -- To convert text to l33t sp34k.
def e_l33t ():
    ui_word = input("What to e-l33t: ")
    lw = ui_word.lower()
    el33ted = lw.replace("e", "3").replace("a", "4").replace("t", "7").replace("s", "5").replace("g", "6").replace("o", "0").replace("i", "1")
    print(el33ted.title())
    internal_loop()


# -- to convert l33t back to standard text.
def d_leet ():
    ui_word = input("What to d-leet: ")
    lw = ui_word.lower()
    dleeted = lw.replace("3", "e").replace("4", "a").replace("7", "t").replace("5", "s").replace("6", "g").replace("0", "o").replace("1", "i")
    print(dleeted)
    internal_loop()





def leeter_menu():
    print("""
-------------
| Leet-er  |
-------------------------------------------------------
| To convert text TO and FROM Leet Speak / 1337 sp34k |
-------------------------------------------------------
[1]: E-1337.
[2]: D-Leet.
[3]: PyAlly Menu.
[4]: Exit PyAlly.
    """)
    menu_answer = int(input("What is your option?: "))
    if menu_answer == 1:
        e_l33t()
    elif menu_answer == 2:
        d_leet()
    elif menu_answer == 3:
        pyally.pyally_menu()
    else:
        pyally.outro()



#-- Internal Loop Function
def internal_loop():
    loop_answer = input("\nBack to the Leet-er Menu? [y/n] : ")
    if loop_answer.lower()== 'y':
        leeter_menu()
    else:
        pyally.mini_menu()









#-- The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    leeter_menu()


