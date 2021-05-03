"""
--------------
| The PyAlly |
-------------------
| h4ck3r - h3lp3r |
-------------------
"""


from time import sleep
import _pyally_main as pyally



# -- Global Variables
# -- The List of Commands
# -- The UI (user input) IP address
the_commands_list = []
ip = ""



# Intro Function : Calls user_input()
def hh_menu():
        print("""
--------------------
| h4ck3r - h3lp3r  |
--------------------------------------------------------------------------------
| Give it an IP & Hacker Helper will give you a file of commands for your CTF. |
--------------------------------------------------------------------------------        

""")

        # -- Adding it to the top of the file
        helper_title = "\n[ The PyAlly : h4ck3r - h3lp3r ]\nby: ryn0f1sh\n"
        the_commands_list.append(helper_title)

        # -- Calling the User Input function
        # -- This will start the chain reaction
        user_input()




# User Input Function
# Will take in the user's input and call the next function: scanning()
def user_input():
    # -- User Input : The IP address as a string
    ip = str(input("\nEnter the Target IP: "))

    # -- Call the Scanning function
    scanning(ip)






# Scanning Function
# Will input the IP into the Scanning parameters and call the next function: enum()
def scanning(ip):
    print("\nConfiguring Nmap & Masscan"
          "\n--------------------------")
    sleep(2)

    # -- Title
    scan_title = "\n\n[PORT SCANNING]" \
                 "\n- - - - - - - -"
    # -- append The Command List
    the_commands_list.append(scan_title)

    # -- configure Nmap
    nmap = "NMAP:\n" \
           "nmap -T4 -n -sC -sV -Pn- -p- -vv -oA Nmap-Results.txt %s \n" % (ip)
    # -- append The Command List
    the_commands_list.append(nmap)

    # -- configure masscan
    masscan = "MASSCAN:" \
              "\nmasscan %s -p0-65535 --rate 5000 \n" % (ip)
    # -- append The Command List
    the_commands_list.append(masscan)

    # -- Call the Enum function
    enum(ip)





# Enum Function
# Will input the IP into the Enum parameters and call the next function: passwords()
def enum(ip):
    print("Configuring Nikto, GoBuster, & Enum4Linux"
          "\n------------------------------------------")
    sleep(2)

    # -- Title
    enum_title = "\n\n[ENUMERATION]" \
                 "\n- - - - - - -"
    # -- append The Command List
    the_commands_list.append(enum_title)

    # -- configure Nikto
    nikto = "NIKTO:\n" \
            "nikto -h %s > Nikto-Results.txt \n" % (ip)
    # -- append The Command List
    the_commands_list.append(nikto)

    # -- configure GoBuster
    gobuster = "GOBUSTER:\n" \
               "gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://%s > Gobuster-Results.txt \n" % (ip)
    # -- append The Command List
    the_commands_list.append(gobuster)

    # -- configure Enum4Linux
    enum4linux = "Enum4Linux:\n" \
                 "enum4linux -a %s \n" % (ip)
    # -- append The Command List
    the_commands_list.append(enum4linux)

    # -- Call the Passwords function
    passwords(ip)




# The Passwords Function
# Will input the IP into the Hydra parameters and call the next function: thefile()
def passwords(ip):
    print("Configuring Hydra"
          "\n-----------------")
    sleep(2)

    #-- Title
    pw_title = "\n\n[PASSWORD BRUTE FORCING]" \
               "\n- - - - - - - - - - - - -"
    # -- append The Command List
    the_commands_list.append(pw_title)

    # -- configure hydra_ftp
    hydra_ftp = "HYDRA FTP:\n" \
                "hydra -f -V -l [USER] -P /usr/share/wordlists/rockyou.txt ftp://%s \n" % (ip)
    # -- append The Command List
    the_commands_list.append(hydra_ftp)

    # -- configure hydra_http
    hydra_http = "HYDRA HTTP-GET:\n" \
                 "hydra -f -V -l [USER] -P /usr/share/wordlists/rockyou.txt http-get://%s \n" % (ip)
    # -- append The Command List
    the_commands_list.append(hydra_http)

    # -- configure hydra_ssh
    hydra_ssh = "HYDRA SSH:\n" \
                "hydra -t 1 -f -V -l [USER] -P /usr/share/wordlists/rockyou.txt %s ssh -e nsr \n" % (ip)
    # -- append The Command List
    the_commands_list.append(hydra_ssh)

    # -- Call the File creation function
    thefile()





# The File Function
# Will create and append a file with all the information in The Commands List
# It will also call the Again() function
def thefile():
    # - Open & Append the text file
    print("\n--- Appending Your Text File ---")
    with open("PyAlly_h4ck3r-h3lp3r.txt","a") as f:
        for x in range(len(the_commands_list)):
            print(the_commands_list[x], file=f)
    # - close the file
    f.close
    sleep(3)
    print("--[ Your hacker helper is ready ]--")

    # -- Call the again()
    again()






# The Again Function : 
# Will ask the user if they have another IP
# If YES it will start the process again
# If NO it will close the program
def again():
    answer = input("\nDo you have another IP? [y/n] : ")
    if (answer.lower() == 'y'):
        separator ="\n\n\n" \
                   "\n# # # # # # # # # # # # #\n"
        the_commands_list.clear() # <-- to Clear the list before adding new things
        the_commands_list.append(separator) # < -- Add a separator at the end of the file
        user_input() # < -- Call this function to start the process again
    else:
        # -- Go the PyAlly Mini Menu
        pyally.mini_menu()







# The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    hh_menu()



