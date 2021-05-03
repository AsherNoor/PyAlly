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
import _pyally_main as pyally

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
    extractor() # calling the extractor function.


''' THE TEXT EXTRACTOR STARTS HERE '''
# Define the extractor() function
#--------------------------------
def extractor():
    print("\n----------"
          "\nIMPORTANT "
          "\n----------"
          "\nPlease make sure that PyAlly: P.T.E. & and your PDF file(s) are in the same file/folder location."
          "\n-----------------------------------------------------------------------------------------\n")
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
    # Opening the PDF file
    PDFfile = open(ui_PDFFileName+".pdf", "rb")
    # Reading the PDF file
    pdfread = PdfFileReader(PDFfile, strict=False)

    # Get the number of pages of this file.
    num_of_pages = pdfread.numPages
    print("\nOne moment, reading", ui_PDFFileName)
    sleep(2)
    print("\nThe page count is: ", num_of_pages)
    sleep(3)



    '''------------------------------------------ 
    The TEXT file creation & appending section 
    ------------------------------------------'''
    # A While loop to extract the whole file.
    i = 0
    while i < num_of_pages:
        pageinfo = pdfread.getPage(i)
        txt = pageinfo.extractText()

        #Encode the txt to utf-8 (converts bytes to string)
        encoded = txt.encode("utf-8")

        # Write to a text file & close text file
        text_file = open(ui_TextFileName + ".txt", "a")
        text_file.write("Page: "+str(i+1)+"\n"+str(encoded)+"\n"*2)
        text_file.close()
        i += 1


    '''-----------------------------------------------
    The Final message that the process is complete 
    ------------------------------------------------'''
    print("\nCreating your output text file, please wait.")
    sleep(2)
    print("\nYour output text file has been created.")
    sleep(1)
    another_file()

    ''' END OF EXTRACTOR FUNCTION '''


# The "Another File" question
def another_file():
        af_answer = str(input("\nHave another file? [y/n]: ").lower().strip())
        if af_answer == "y":
            #-- Calling the extractor function again.
            extractor()
        else:
            #-- Go to the PyAlly Mini Menu
            pyally.mini_menu()




# The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    pte_menu()











"""
-------------------
| The Scratch Pad |
-------------------
Slices of codes that was not used.
----------------------------------

#This is only to display it on the screen.
print("The while extract \n", encoded).




"""