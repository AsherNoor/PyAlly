"""
--------------
| The PyAlly |
---------------
| CHMOD Helper|
---------------
"""


import _pyally_main as pyally

# ---- Defining Functions ----

# The Intro Function
def chmod_menu():
    print(""""
-----------------
| CHMOD Helper  |
----------------------------------------------------
| Helps you figure out the CHMOD permissions code. |
----------------------------------------------------
""")
    chmod() #-- calling the


# The CHMOD Options Function
def chmod():
    print("\n-----------------------"
    "\nChoose The Permissions"
    "\n-----------------------"
    "\n1: Execute [--x ]"
    "\n2: Write [ -w- ]"
    "\n3: Execute & Write [ -wx ]"
    "\n4: Read [ r-- ]"
    "\n5: Read & Execute [ r-x ]"
    "\n6: Read & Write [ rw- ]"
    "\n7: Read, Write, & Execute [ rwx ]" "\n")

    # UI's choices.
    # user
    u = int(input(" What is your choice for USER: "))
    
    # group
    g = int(input(" What is your choice for GROUP: "))

    # everyone
    e = int(input(" What is your choice for EVERYONE: "))

    
    # Concacting the code
    uicode = str(u)+str(g)+str(e)
    code = uicode
    vcode = (u, g, e)

    # code test
    #print("\nTest Code:"+ code)    
    
    # Dispalying the numeric results
    print("\nThis is your numeric CHMOD code: "+ code)
    
    # Call the visual function
    visual(vcode)



# Creating the Visuals of the permissions chosen 
def visual(vcode):  
    print("This will be your file's permissions: ", end="")
    for x in vcode:
        if (x == 1):
            print("--x", end="")
        elif (x == 2):
            print("-w-", end="")
        elif (x == 3):
            print("-wx", end="")
        elif (x == 4):
            print("r--", end="")
        elif (x == 5):
            print("r-x", end="")
        elif (x == 6):
            print("rw-", end="")
        elif (x == 7):
            print("rwx", end="")
        else:
            print("Invalid Option")
    
    # Call the again function
    internal_loop()


    
#-- Internal Loop Function
def internal_loop():
    loop_answer = input("\nBack to the CHMOD? [y/n] : ")
    if loop_answer.lower()== 'y':
        chmod()
    else:
        pyally.mini_menu()




# ----- End of Defining Functions ----

# The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    chmod_menu() # <-- calling the intro function


