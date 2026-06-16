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

def trycss(cclass, cmessage):
    return f"""
#workskin:has(.fadedetails[open]) .m{cclass} {{
visibility: visible;
transition: all 2s linear 2s;
}}
#workskin:not(:has(.notextspeak[open])) .text.m{cclass}::after {{
    content: "{cmessage}";
}}
"""

def tryhtml(huser, hmessage, hclass):
    return f"""
<p class="username visibly m{hclass}"><strong>{huser}</p></strong></p>
<p class="text visibly m{hclass}"><span class="fallback">{hmessage}</span></p>
"""

html = []
css = []
for i, msg in enumerate(messages):
  (time, user, message) = rembrackets(msg)
  msg_html = tryhtml(user, message, i)
  msg_css = trycss(i, message)
  html.append(msg_html)
  css.append(msg_css)

print(css)

finalhtml = "\n".join(html)
print(finalhtml)

finalcss = "\n".join(css)
print(finalcss)

with open ("output.html", "w") as fohtml:
    print(finalhtml, file=fohtml) 

with open ("output.css", "w") as focss:
    print(finalcss, file=focss)