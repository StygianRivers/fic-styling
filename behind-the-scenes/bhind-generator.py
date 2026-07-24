#!/usr/bin/env python3

import re

def rmbrackets(onemessage): 
    regmatch = re.match(r"(\[(\d)\s?min\])?(\*\*(.*):\*\*)? ?(.*)?", onemessage)
    matchone = regmatch[2]
    matchtwo = regmatch[4]
    matchthree = regmatch[5]
    return matchone, matchtwo, matchthree

with open("example.md", "r") as f:
    contents = f.read()

messages = contents.strip().split("\n\n")

delaylist = []

html = []
css = []

typing_iteration = 0

def trycss(cclass, cmessage, ctime):
    while True:
        print('\033[96m' + "How much delay since the last message, in seconds?" + '\x1b[0m')
        print('\033[96m' + "Suggested time: " + str(ctime) + '\x1b[0m')
        delay = input()
        try:
            delaylist.append(int(delay))
            totaldelay = sum(delaylist)
            print('\033[96m' + "Total: " + str(totaldelay) + '\x1b[0m')
            return f"""
            #workskin:has(.fadedetails[open]) .m{cclass} {{
            visibility: visible;
            transition: all 1s linear {totaldelay}s;
            }}

            #workskin:not(:has(.notextspeak[open])) .text.m{cclass}::after {{
                content: "{cmessage}";
            }}
            """
        except ValueError:
            print("That's not a number!")

def tryhtml(huser, hmessage, hclass):
    print('\033[96m' + "Enter alt text:" + '\x1b[0m')
    baseMessage = input()
    return f"""
<p class="username visibly m{hclass}"><strong>{huser}</p></strong></p>
<p class="text visibly m{hclass}"><span class="fallback">{baseMessage}</span></p>
"""

def typingdots():
    html.append("<div class="relatyping">")
    user_typing = input("Who is typing?")
    typing_iter = typing_iteration + 1
    while True:
        ty_html = f"""
        <p class="text visibly is-typing"><span class="fade-typing"><span class="t{typing_iter}"><span class="texthide"><strong><small>{user_typing} is typing...</small></strong></span></span></span></p>
    """
        more_typing = input("Another blink?")
        if more_typing == 'y' or 'yes' or 'ok':
            typing_iter = typing_iter + 1
            continue
        elif more_typing == 'n' or 'no' or 'quit':
            html.append(ty_html)
            html.append("</div>")
            break
    #css

for i, msg in enumerate(messages):
  print('\033[31m' + msg + '\x1b[0m')
  (time, user, message) = rmbrackets(msg)
  try:
      int(time)
      hesitation = int(time) * 60
  except:
      hesitation = 0
  msg_css = trycss(i, message, hesitation)
  msg_html = tryhtml(user, message, i)
  while True:
    print('\033[96m' + "Resulting HTML:" + '\x1b[0m' + msg_html)
    print('\033[96m' + "Resulting CSS:" + '\x1b[0m' + msg_css)
    print('\033[96m' + "Confirm" + '\x1b[0m')
    confirm = input().lower()
    if confirm == '':
        html.append(msg_html)
        css.append(msg_css)
        break
    elif confirm == 'skip':
        break
    elif confirm == 'retry':
        msg_css = trycss(i, message)
        msg_html = tryhtml(user, message, i)
    elif confirm == 'html' or 'message' or 'text' or 'msg':
        msg_html = tryhtml(user, message, i)
    elif confirm == 'css' or 'time' or 'delay' or 'int':
        msg_css = trycss(i, message)
    else: 
        print("Type \'skip\' to skip this message, or 'retry' to change the input.")
  while True:
      print("Typing indicator flashing?")
      typing_indicator = input().lower()
      if typing_indicator == 'y' or 'yes' or 'ok':
         (typing_html, typing_css, typing_iteration) = typingdots
      else:
        break

finalhtml = "\n".join(html)
print(finalhtml)

finalcss = "\n".join(css)
print(finalcss)

with open ("output.html", "w") as fohtml:
    print(finalhtml, file=fohtml) 

with open ("output.css", "w") as focss:
    print(finalcss, file=focss)