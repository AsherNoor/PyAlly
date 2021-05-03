"""

-------------------------------
| PROGRAM NAME: The PyAlly    |
| Version #:  001             |
| DATE:  April/May 2021      |
------------------------------

------------------------------------------------------------------------
| EXPLANATION |                                                        |
|--------------                                                        |
| This is a toolbox of tools, if you will.                             |
| I will keep adding more scripts/programs as I make them.             |
| Trying to create a single program with some of my mostly used tools. |
------------------------------------------------------------------------


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

import _pyally_main as pyally

"""
This file mainly to call the _pyally_main file.
Due to _pyally_main having a 'Main Guard', it was difficult to create an EXE file.
By having this file, without a 'Main Guard', I can call on the program, without fear of it affecting all
the other programs that call on to _pyally_main.

"""

#-- Calling the PyAlly Main Menu

pyally.pyally_menu()