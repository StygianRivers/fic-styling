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
    output_file = re.match(r"(?:.*\/)?(.+)\..*", input_file).group()
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

def autoTyping(count, user_typing, typing_iteration):
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
    return typing_iter, time_spent_typing

def boldtags(boldmessage):
    try:
        nametag = re.sub(r"(@(Minato|Makoto|Yu|Akira))", r"<strong>\1</strong>", boldmessage) # can't figure out how to make regex read variables like usrone
        return nametag
    # if there is no match, return original message
    except TypeError:
        return boldmessage

def typingdots(upcoming_message):
    # open div in case of multiple blinks
    html.append("<div class=\"relatyping\">")
    print("Who is typing?\nNext message is:\n" + upcoming_message)
    user_typing = input()
    global typing_iteration
    typing_iter = typing_iteration + 1
    while True:
        typing_length = input("How long is the indicator visible?\n")
        ty_start = input("How long is the pause before the indicator appears?\n")
        delaylist.append(int(ty_start))
        totaldelay = int(sum(delaylist))
        # account for typing div in future transition-delay
        delaylist.append(int(typing_length) + 1)
        ty_html = f"""
<p class="text visibly is-typing"><span class="fade-typing"><span class="t{typing_iter}"><span class="texthide"><strong><small>{user_typing} is typing...</small></strong></span></span></span></p>
    """
        ty_css = f"""
#workskin:has(.fadedetails[open]) .t{typing_iter} {{
visibility: visible;
transition: all {typing_length}s linear {totaldelay}s;
}}"""
        css.append(ty_css)
        more_typing = input("Another blink?\n").lower()
        if more_typing in ['y', 'yes', 'ok']:
             typing_iter = typing_iter + 1
             continue
        else:
            break
    html.append(ty_html)
    # close div
    html.append("</div>")
    return typing_iter

def trycss(cclass, cuser, cmessage, chesitation, typing_iteration):
    if cuser in [usrone, usrone_alt]:
        for character in cmessage:
            global character_count
            character_count = character_count + 1
        if character_count > 5:
            (typing_iteration, base_typing_length) = autoTyping(character_count, cuser, typing_iteration)
    elif cuser in [usrtwo, usrthree]:
        for word in re.finditer(r"\b\w+?\b", cmessage):
            global word_count 
            word_count = word_count + 1
        if word_count > 4:
            (typing_iteration, base_typing_length) = autoTyping(word_count, cuser, typing_iteration)
    if chesitation == 0:
        totaldelay = int(sum(delaylist))
        css_result = f"""
#workskin:has(.fadedetails[open]) .m{cclass} {{
visibility: visible;
transition: all 1s linear {totaldelay}s;
}}

#workskin:not(:has(.notextspeak[open])) .text.m{cclass}::after {{
content: "{cmessage}";
}}
"""
        return css_result, base_typing_length
    else:
        typing_indicator = input("Hesitation? \n").lower()
        if typing_indicator in ['y', 'yes', 'ok']:
            (typing_iteration, css_result) = typingdots(chesitation)
        return typing_iteration, css_result, base_typing_length

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

def saveProgress(typing_iteration):
    save_progress = input("'Y' to save and quit \n").lower()
    if save_progress in ['y', 'yes', 'ok', 'save', 'q']:
        global i
        i = i + 1
        with open("olddata.py", "w") as old_data:
            old_data.write("input_file = \"" + input_file + "\"\noutput_file = \"" + output_file + "\"\nstart = " + str(i) + "\ntyping_iteration = " + str(typing_iteration) + "\ndelaylist = " + str(delaylist) + "\nuserpersist = \"" + userpersist + "\"")
            old_data.close()
        finalhtml = "\n".join(html)
        finalcss = "\n".join(css)
        with open (f"{output_file}.html", "a") as fohtml:
            print(finalhtml, file=fohtml) 
        with open ("output.css", "a") as focss:
            print(finalcss, file=focss)
        exit
    else:
        return

for i, msg in enumerate(messages[start:]):
    # every message is at least 1 second removed from the previous
    delaylist.append(1)
    # getting the components
    (time, user, message) = rmbrackets(msg)
    # check whether 'time' has a number, print only relevant components
    try:
        int(time)
        hesitation = int(time) * 60
        summMessage = '\033[31m' + "[" + time + "min] " + user + ": " + message + '\x1b[0m'
        print(summMessage)
        # give user the option to insert suggested hesitation
        typing_indicator = input("Hesitation? \n").lower()
        if typing_indicator in ['y', 'yes', 'ok']:
            typing_iteration = typingdots(summMessage)
        (typing_iteration, msg_css, base_length) = trycss(i, user, message, hesitation, typing_iteration)
    except TypeError:
        hesitation = 0
        print('\033[31m' + user + ": " + message + '\x1b[0m')
        (msg_css, base_length) = trycss(i, user, message, hesitation, typing_iteration)
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
            (typing_iteration, msg_css) = trycss(i, user, message, hesitation)
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
    # give the option to save and quit
    saveProgress(typing_iteration)

html.append(html_end)

finalhtml = "\n".join(html)
finalcss = "\n".join(css)

with open ("{output_file}.html", "a") as fohtml:
    print(finalhtml, file=fohtml) 

with open ("output.css", "a") as focss:
    print(finalcss, file=focss)

try: 
    os.remove("olddata.py")
except IOError:
    print("No save data to overwrite.")

print("Done!")