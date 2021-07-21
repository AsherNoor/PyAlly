"""
--------------
| The PyAlly |
----------------------
| PDF Text Extractor |
----------------------
"""


import sys
from os import system, name
from subprocess import call
from PyPDF2 import PdfFileReader, PdfFileWriter
from time import sleep
import codecs
import pdfplumber
import _pyally_main as pyally
import pikepdf

'''------------------
DEFINING MY FUNCTIONS
---------------------'''

# The Intro function
#-------------------
def pte_menu():
    print("""
-----------------------------
| PDF Text Extractor (P.T.E.)  |
------------------------------------------------------------------------------------
| P.T.E. simply reads a PDF file, extracts the text, and inputs it in a text file. |
------------------------------------------------------------------------------------
""")
    sleep(2)
    # The PTE Menu Options: Decrypt or Extract
    print("""\n-------------
P.T.E. Menu
-------------
(1): Decrypt a PDF (You must have the password).
(2): Extract text from a PDF.
(3): Exit P.T.E.""")

    # User Input
    menu_answer = int(input("\nEnter Option: "))
    if (menu_answer == 1):
        pdf_decrypt() # Calling the Decryptor function.
    elif (menu_answer == 2):
        extractor() # Calling the Extractor function.
    else:
        pyally.mini_menu() # Calling the PyAlly mini menu.







''' THE PDF DECRYPTER STARTS HERE '''
def pdf_decrypt():
    print("\n----------"
          "\nIMPORTANT "
          "\n----------"
          "\nPlease make sure that PyAlly: P.T.E. & and your PDF file(s) are in the same file/folder location."
          "\n-----------------------------------------------------------------------------------------"
          "\n-- Decryptor --\n")
    sleep(3)
    # User Input:
    the_book = input("Name of the Book without the '.pdf' : ")
    the_password = input("The Password: ")

    # Decrypting the file and saving the new one.
    print("\nDecrypting your file now. "
          "\nThis may take a few minutes depending on size.")
    pdf = pikepdf.open(the_book+".pdf",password=the_password)
    pdf.save('Decrypted_'+the_book+'.pdf')
    print("Your PDF has been decrypted.")

    # Go Back to menu function.
    go_back_to_menu() # To go back to the P.T.E. Menu




''' THE TEXT EXTRACTOR STARTS HERE '''
# Define the extractor() function
#--------------------------------
def extractor():
    print("\n----------"
          "\nIMPORTANT "
          "\n----------"
          "\nPlease make sure that PyAlly: P.T.E. & and your PDF file(s) are in the same file/folder location."
          "\n-----------------------------------------------------------------------------------------"
          "\n-- Extractor --\n")
    sleep(3)

    '''--------------------- 
    The User Input Section 
    ----------------------'''
    # User Input : Name of the PDF file.
    ui_PDFFileName = str(input("Enter the PDF file name without the '.pdf': "))

    # User Input : Name of the TXT file.
    ui_TextFileName = str(input("Your desired output TEXT file name without the '.txt': "))

    '''-------------------------------- 
    The PDF info extraction Section 
    --------------------------------'''
    # This loops through the whole PDF
    with pdfplumber.open(ui_PDFFileName + ".pdf") as pdf:
        page = pdf.pages
        for i, pg in enumerate(page):
            text = page[i].extract_text()
            extracted = (f'-- PAGE: {i + 1} -- {text} \n\n')
            # print(extracted)
            # Write to a text file & close text file
            with open(ui_TextFileName +".txt", "a", encoding="utf-8") as text_file:
                text_file.write(extracted)
                text_file.close()



    '''-----------------------------------------------
    The Final message that the process is complete 
    ------------------------------------------------'''
    print("\nCreating your output text file, please wait.")
    sleep(2)
    print("\nYour output text file has been created.")
    sleep(1)
    go_back_to_menu() # To go back to the P.T.E. Menu

    ''' END OF EXTRACTOR FUNCTION '''


# The "Another File" question
def go_back_to_menu():
        gb_answer = str(input("\nGo back to the P.T.E. Menu? [y/n]: ").lower().strip())
        if gb_answer == "y":
            #-- Calling PTE Menu.
            pte_menu()
        else:
            #-- Go to the PyAlly Mini Menu.
            pyally.mini_menu()




# The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    pte_menu()









