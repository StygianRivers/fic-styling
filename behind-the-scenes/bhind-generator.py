#!/usr/bin/env python3

import re

def rembrackets(onemessage): 
    regmatch = re.match(r"(\[.*\])?\*\*(.*):\*\* ?(.*)?", onemessage)
    matchone = regmatch[1]
    matchtwo = regmatch[2]
    matchthree = regmatch[3]
    return matchone, matchtwo, matchthree


with open("example.md", "r") as f:
    contents = f.read()

messages = contents.strip().split("\n\n")

newlist = [rembrackets(x) for x in messages]

def tryhtml(htime, huser, hmessage):
    return f"""
<p class="username visibly m"><strong>{huser}</p></strong></p>
<p class="text visibly m"><span class="fallback">{hmessage}</span></p>
"""

thirdlist = [tryhtml(bracks, username, messtring) for bracks, username, messtring in newlist]
finalformat = "\n".join(thirdlist)
print(finalformat)

def trycss(cmessage, ctyping):
    return f"""
"""

with open ("output.html", "w") as fo:
    print(finalformat, file=fo) 