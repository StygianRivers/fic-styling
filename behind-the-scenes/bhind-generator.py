#!/usr/bin/env python3

import re
import os

html = []
css = []
character_count = 0
word_count = 0
groupchatname = "Wild Card Support Group"
usrone = "Minato"
usrone_alt = "Makoto"
usrtwo = "Yu"
usrthree = "Akira"

# chatroom container
html_intro = f"""<div class="flex">
        <details class="fadedetails">
            <summary>{groupchatname}<span class="overlay"></span></summary>
            <div class="phone">
                <h3 class="phoneheader">
                    <span class="hiddeninfo">Group chat: </span>
                    {groupchatname}
                </h3> 
                """

html_end = """
            </div>
        </details>
    </div>
    """

try:
    from olddata import *
except ImportError:
    print("No previous data found.")
    input_file = input("Which file to generate for?\n")
    output_file = re.match(r"(?:.*/)?(.+)\..*", input_file).group()
    start = 0
    typing_iteration = 0
    delaylist = []
    userpersist = "None"
    html.append(html_intro)

with open(input_file, "r") as f:
    contents = f.read()
messages = contents.strip().split("\n\n")

def rmbrackets(onemessage): 
    regmatch = re.match(r"(\[(\d*)?\s?.*\])?(\*\*(.*):\*\*)? ?(.*)?", onemessage)
    matchone = regmatch[2]
    matchtwo = regmatch[4]
    matchthree = regmatch[5]
    return matchone, matchtwo, matchthree

def autoTyping(count, user_typing):
    typing_iter = typing_iteration + 1
    time_spent_typing = count * 0.25
    delaylist.append(1)
    totaldelay = sum(delaylist)
    delaylist.append(time_spent_typing)
    autoty_html = f"""
    <p class="text visibly is-typing"><span class="fade-typing"><span class="t{typing_iter}"><span class="texthide"><strong><small>{user_typing} is typing...</small></strong></span></span></span></p>
        """
    autoty_css = f"""#workskin:has(.fadedetails[open]) .t{typing_iter} {{
        visibility: visible;
        transition: all {time_spent_typing}s linear {totaldelay}s;
    }}"""
    html.append(autoty_html)
    css.append(autoty_css)
    return typing_iter

def boldtags(boldmessage):
    try:
        nametag = re.sub(r"(@(Minato|Makoto|Yu|Akira))", r"<strong>\1</strong>", boldmessage)
        return nametag
    # if there is no match, return original message
    except TypeError:
        return boldmessage

def trycss(cclass, cuser, cmessage, chesitation):
    if cuser in [usrone, usrone_alt]:
        for character in cmessage:
            global character_count
            character_count = character_count + 1
        if character_count < 6:
            time_to_type = 1
        else:
            typing_iteration = autoTyping(character_count, cuser)
            time_to_type = 0
    elif cuser in [usrtwo, usrthree]:
        for word in re.finditer(r"\b\w+?\b", cmessage):
            global word_count 
            word_count = word_count + 1
        if word_count < 5:
            time_to_type = 1
        else:
            typing_iteration = autoTyping(word_count, cuser)
            time_to_type = 0
    suggested_time = chesitation + time_to_type
    while True:
        print('\033[96m' + "How much delay since the last message, in seconds?" + '\x1b[0m')
        print('\033[96m' + "Suggested time: " + str(suggested_time) + '\x1b[0m')
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
    altMessage = boldtags(baseMessage)
    # if the username is the same as the previous message, don't add the username for this one as well
    global userpersist 
    if userpersist == huser:
        return f"""<p class="text visibly m{hclass}"><span class="fallback">{altMessage}</span></p>"""
    else:
        userpersist = huser
        return f"""
<p class="username visibly m{hclass}"><strong>{huser}</strong></p>
<p class="text visibly m{hclass}"><span class="fallback">{altMessage}</span></p>
"""

def typingdots():
    html.append("<div class=\"relatyping\">")
    user_typing = input("Who is typing?\n")
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
        if more_typing in ['y', 'yes', 'ok']:
             typing_iter = typing_iter + 1
             continue
        else:
             html.append(ty_html)
             html.append("</div>")
             break

def saveProgress():
    save_progress = input("'Y' to save and quit \n").lower()
    if save_progress in ['y', 'yes', 'ok', 'save']:
        global i
        i = i + 1
        with open("olddata.py", "w") as old_data:
            old_data.write("input_file = \"" + input_file + "\"\noutput_file = \"" + output_file + "\"\nstart = " + str(i) + "\ntyping_iteration = " + str(typing_iteration) + "\ndelaylist = " + str(delaylist) + "\nuserpersist = \"" + userpersist + "\"")
            old_data.close()
            finalhtml = "\n".join(html)
            finalcss = "\n".join(css)
            with open (f"{output_file[1]}.html", "a") as fohtml:
                print(finalhtml, file=fohtml) 
            with open ("output.css", "a") as focss:
                print(finalcss, file=focss)
            exit
    else:
        return

for i, msg in enumerate(messages[start:]):
    delaylist.append(1)
    (time, user, message) = rmbrackets(msg)
    try:
        int(time)
        hesitation = int(time) * 60
        print('\033[31m' "[" + time + "mins] " + user + ": " + message + '\x1b[0m')
    except:
        hesitation = 0
        print('\033[31m' + user + ": " + message + '\x1b[0m')
    msg_css = trycss(i, user, message, hesitation)
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
            msg_css = trycss(i, user, message, hesitation)
            msg_html = tryhtml(user, message, i)
            continue
        elif confirm in ['html', 'message', 'text', 'msg']:
            msg_html = tryhtml(user, message, i)
            continue
        elif confirm in ['css', 'time', 'delay', 'int']:
            msg_css = trycss(i, user, message, hesitation)
            continue
        else: 
            print("Type 'skip' to skip this message, or 'retry' to change the input.")
    typing_indicator = input("Hesitation? \n").lower()
    if typing_indicator in ['y', 'yes', 'ok']:
        typingdots()
    saveProgress()

html.append(html_end)

finalhtml = "\n".join(html)
finalcss = "\n".join(css)

with open (f"{output_file[1]}.html", "a") as fohtml:
    print(finalhtml, file=fohtml) 

with open ("output.css", "a") as focss:
    print(finalcss, file=focss)

try: 
    os.remove("olddata.py")
except IOError:
    print("No save data to overwrite.")

print("Done!")