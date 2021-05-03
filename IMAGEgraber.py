"""
--------------
| The PyAlly |
-----------------
| Image Grabber |
-----------------
"""


import mechanicalsoup
import os
import wget
import _pyally_main as pyally
from time import sleep



#-- Image Grabber Menu
def ig_menu():
    print("""
-----------------
| Image Grabber  |
-------------------------------------------------------------------------
| Type in a word and it will grab & save 20 images from Google locally. |
| Inspired by Maria Sha (Python Simplified) Youtube video.              |
-------------------------------------------------------------------------    
""")


    " -- Setting up the Browser side of things --"
    #-- Setting up a browser & url variable
    browser = mechanicalsoup.StatefulBrowser()
    url = "https://images.google.com/"

    #-- Request the page by Opening the URL in the browser
    browser.open(url)
    #print(browser.get_url()) #-- a Test print


    #-- Extrating the HTML from the webpage
    browser.get_current_page()
    #print(browser.get_current_page()) #-- a Test print

    #-- Targeting just the INPUT fields of the site
    browser.select_form()
    #browser.get_current_form().print_summary() #-- a Test print

    #-- Selecting the SEARCH field, which is called Q + the search term
    search_term = input("Search Term: ")
    browser["q"] = search_term

    #-- Submit /Click - to search
    browser.launch_browser() #-- to input the search term
    response = browser.submit_selected() #-- to capture the response


    " -- Now we navigate to the NEW Url to target the images --"

    #-- Open New URL
    new_url = browser.get_url()
    browser.open(new_url)

    #-- Get the HTML
    page = browser.get_current_page()
    all_images = page.find_all('img')

    #-- Target the Source : SRC attribute, put it into an empty list
    image_source = []
    for image in all_images:
        image = image.get('src')
        image_source.append(image)

    #-- Fixing the Broken/Incomplete image links
    image_source = [image for image in image_source if image.startswith('https')]


    #-- Creating a Local folder
    path = input("Type the full path of where to save the images: ") #-- UI: Where to save the file
    os.chdir(path) #-- to change dirctory of what's in path
    #path = os.getcwd() #-- To see where the current path is
    path = os.path.join(path, search_term) #-- Creating the new directory
    os.mkdir(path) #-- Confirming the creation of the new directory




    " -- Saving the images that we have found --"
    counter = 1 #-- Used in the naming
    for image in image_source:
        save_as = os.path.join(path, search_term + str(counter) + ".jpg") #-- to hold the path and image names
        wget.download(image, save_as) #-- (what we are saving, location to save it)
        counter += 1

    print("Your images have been saved.")
    sleep(1)

    #-- Calling the mini menu
    internal_loop()



#-- Internal Loop Function
def internal_loop():
    loop_answer = input("\nBack to the Image Grabber? [y/n] : ")
    if loop_answer.lower()== 'y':
        ig_menu()
    else:
        pyally.mini_menu()



# The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    ig_menu()