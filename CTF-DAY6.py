import sys, os, re, base64, codecs

xdata = "bm9pdGFyaXBzbmkgdG5lY3JlcCBlbm8gc2kgc3VpbmVH"

def Function(xdata):
    spaces = "\"\"\""
    theFile = spaces + xdata + spaces
    theDecoded = base64.standard_b64decode(theFile)
    answer = theDecoded.decode("utf-8")
    r2 = "".join(reversed(answer))
    return r2




#---- FUNCTION CALLS ---
Function(xdata)









"""#-- Question Zero Base64 + Reverse
#-- thou count to three, no more, no less
TheString = "ssel on ,erom on ,eerht ot tnuoc uoht"
#stinglen =len(TheString)
#r2 = str(reversed(TheString))
r2 ="".join(reversed(TheString))
print(r2)
#//////////////////////////////////////////"""





