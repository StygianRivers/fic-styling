#!/usr/bin/env python3

import re

try:
    old_data = open("olddata.txt", "r+")
    old_data.read()
except IOError:
    print("No previous data found.")
    input_file = input("Which file to generate for?\n")
    output_file = re.match(r"(?:.*/)?(.+)\..*", input_file)
    start = 0
    typing_iteration = 0
    delaylist = []
    userpersist = 0

with open(input_file, "r") as f:
    contents = f.read()
messages = contents.strip().split("\n\n")

html = []
css = []

html_intro = """<div class="flex">
        <details class="fadedetails">
            <summary>Wild Card Support Group<span class="overlay"></span></summary>
            <div class="phone">
                <h3 class="phoneheader">
                    <span class="hiddeninfo">Group chat: </span>
                    Wild Card Support Group
                </h3> 
                """

html_end = """
            </div>
        </details>
    </div>
    """

html.append(html_intro)

def rmbrackets(onemessage): 
    regmatch = re.match(r"(\[(\d)?\s?.*\])?(\*\*(.*):\*\*)? ?(.*)?", onemessage)
    matchone = regmatch[2]
    matchtwo = regmatch[4]
    matchthree = regmatch[5]
    return matchone, matchtwo, matchthree

# def boldtags(boldmessage):
#     nametag = re.match(r"( @.* )?", boldmessage)
#     print(nametag[1])
#     if nametag == None:
#         print("No tags")
#     else:
#         re.sub(r"( ).*", " <strong>", nametag[1])
#         re.sub(r".*( )", "</strong> ", nametag[1])

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
    # if the username is the same as the previous message, don't add the username for this one as well
    global userpersist 
    if userpersist == huser:
        return f"""<p class="text visibly m{hclass}"><span class="fallback">{baseMessage}</span></p>"""
    else:
        userpersist = huser
        return f"""
<p class="username visibly m{hclass}"><strong>{huser}</p></strong></p>
<p class="text visibly m{hclass}"><span class="fallback">{baseMessage}</span></p>
"""

def typingdots():
    html.append("<div class=\"relatyping\">")
    user_typing = input("Who is typing?")
    typing_iter = typing_iteration + 1
    while True:
        typing_length = input("How long does the indicator last?\n")
        ty_start = input("How long is the pause before the indicator appears?\n")
        delaylist.append(int(ty_start))
        totaldelay = sum(delaylist)
        delaylist.append(int(typing_length))
        ty_html = f"""
        <p class="text visibly is-typing"><span class="fade-typing"><span class="t{typing_iter}"><span class="texthide"><strong><small>{user_typing} is typing...</small></strong></span></span></span></p>
    """
        ty_css = f"""#workskin:has(.fadedetails[open]) .t{typing_iter} {{
    visibility: visible;
    transition: all {typing_length}s linear {totaldelay}s;
}}"""
        css.append(ty_css)
        more_typing = input("Another blink?\n")
        if more_typing == 'y' or 'yes' or 'ok':
             typing_iter = typing_iter + 1
             continue
        elif more_typing == 'n' or 'no' or 'quit':
             html.append(ty_html)
             html.append("</div>")
             break

for i, msg in enumerate(messages[start:]):
  print('\033[31m' + msg + '\x1b[0m')
  (time, user, message) = rmbrackets(msg)
  #boldtags(message)
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
        print("Type 'skip' to skip this message, or 'retry' to change the input.")
    print("Typing indicator flashing?")
    typing_indicator = input().lower()
    if typing_indicator == 'y' or 'yes' or 'ok': #why tf does this not work
        typingdots()
    else:
        continue
    save_progress = input("'Y' to save and quit").lower()
    if save_progress == 'y' or 'yes' or 'ok':
        open(old_data, "w")
        old_data.write("input_file = " + input_file + "\noutput_file = " + output_file + "\nstart = " + start + "\ntyping_iteration = " + typing_iteration + "\ndelaylist = " + delaylist + "userpersist = " + userpersist)
        old_data.close()
        finalhtml = "\n".join(html)
        finalcss = "\n".join(css)
        with open (f"{output_file[1]}.html", "a") as fohtml:
            print(finalhtml, file=fohtml) 
        with open ("output.css", "a") as focss:
            print(finalcss, file=focss)
    else:
        break

html.append(html_end)

finalhtml = "\n".join(html)
finalcss = "\n".join(css)

with open (f"{output_file[1]}.html", "a") as fohtml:
    print(finalhtml, file=fohtml) 

with open ("output.css", "a") as focss:
    print(finalcss, file=focss)

print("Done!")