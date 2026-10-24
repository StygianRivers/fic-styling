#!/usr/bin/env python3

import re
import os

# manual edit variables
groupchatname = "Wild Card Support Group"
usrone = "Minato"
usrone_alt = "Makoto"
usrtwo = "Yu"
usrthree = "Akira"
t9users = [usrone, usrone_alt]
smartphusers = [usrtwo, usrthree]
path = "/home/drift/custom-scripts/fic/behind-the-scenes/"
manual_var_list = [f"{groupchatname=}", f"{usrone=}", f"{usrone_alt=}", f"{usrtwo=}", f"{usrthree=}", f"{t9users=}", f"{smartphusers=}", f"{path=}"]

# delay lengths in seconds
character_typing = 0.3
word_typing = 0.7
# delay lengths per character
read_time = 0.04
think_time = 0.02
# focus multiplier
half_focus = 1.7
bad_focus = 2.25

# setting up variables
syscolor_start = "\033[96m"
errcolor_start = "\033[31m\033[1m"
textcolor_start = "\033[34m"
successcolor_start = "\033[32m"
color_end = "\033[0m"
f_state = 0
first_mess = "None"
it_boost_up = "None"
paragraph = False
html = []
css = []
sec_list = []
for i in range(2400):
    sec_list.append(str(i) + "s") 
added_time_seconds = sec_list

# chatroom container
html_end = """
            </div>
        </details>
"""

# review manual edit variables
print(syscolor_start + "Group Chat Name: " + color_end + textcolor_start + groupchatname + syscolor_start + "\nUser One: " + textcolor_start + usrone + syscolor_start + "\nUser One Alternate Username: " + textcolor_start + usrone_alt + syscolor_start + "\nUser Two: " + textcolor_start + usrtwo + syscolor_start + "\nUser Three: " + textcolor_start + usrthree)
# edit_var = input(syscolor_start + "\nEdit? " + color_end).lower()
# if edit_var in ['y', 'yes']:
    # print(syscolor_start + "'Enter' to keep it as it is." + color_end)
    # for i in manual_var_list:
        # x = input(f"{i}\nNew: ")
        # if x == "":
            # i = i
        # else:
            # i = x # this does not work to save new values for variables
    # print(successcolor_start + "Finished." + color_end)

print(syscolor_start + "Focus levels: 3 or 0 is normal focus, 2 is half focus, 1 is bad focus.\n" + color_end)

def big_file_split():
    bigconfirm = input(syscolor_start + "Split big file into scenes?\n" + color_end)
    if bigconfirm in ['y', 'yes', 'ok']:
        big_file = path + input(syscolor_start + "Which file to split?\n" + color_end)
        with open(big_file, "r") as fbig:
            all_scenes = fbig.read()
        # divide into individual scenes
        scenes = all_scenes.strip().split("\n\n-\n\n")
        for i, scn in enumerate(scenes):
            with open(f"{path}scene{i}.md", "w") as scene:
                print(scn, file=scene) 
            print("File scene" + str(i) + " created")
        return
    elif bigconfirm in ['n', 'no']:
        return
    else:
        print("Not a valid input (y/n)")
        # repeat prompt
        big_file_split()

def inputFileName():
    input_f = path + input(syscolor_start + "Which file to generate for?\n" + color_end)
    if os.path.isfile(input_f):
        return input_f
    else:
        print("File does not exist (check file name for errors or change path variable)")
        # repeat prompt
        input_f = inputFileName()
        return input_f

try:
    # check for save data
    from olddata import *
    print(syscolor_start + "Retrieving save file..." + color_end)
except ImportError:
    # no save data, start fresh
    print(syscolor_start + "No previous data found." + color_end)
    big_file_split()
    input_file = inputFileName()
    output_file = re.match(r"(?:.*\/)(.+)\..*", input_file).group(1)
    focus = 0
    focus_mult = 1
    start = 0
    message = "Not defined"
    typing_iteration = 0
    delaylist = []
    userpersist = "None"
    html_intro = f"""<details class="fade fadedetails{output_file}">
        <summary>{groupchatname}<span class="overlay"></span></summary>
        <div class="phone bordoor">
            <h3 class="phoneheader">
                <span class="hiddeninfo">Group chat: </span>
                    {groupchatname}
            </h3> 
"""
    html.append(html_intro)

# divide a single message into parts
def rmbrackets(onemessage): 
    regmatch = re.match(r"(\[(\d*)min\s?\])?(\[.*\])? ?(\*\*(.*):\*\*)? ?(.*)?", onemessage)
    time_indication = regmatch[2]
    fic_notes = regmatch[3]
    username = regmatch[5]
    message_body = regmatch[6]
    return time_indication, fic_notes, username, message_body

def focus_issues(f_state):
    global focus_mult
    if f_state in ['1', 1, '2', 2, '3', 3]:
        print(syscolor_start + "Previous level of focus: " + color_end + f_state)
        focus_check = input("Any change in focus?\n").lower()
        if focus_check in ['y', 'yes', '1', '2', '3']:
            while True:
                f_state = input("Current focus level: ")
                if f_state not in ['1', '2', '3']:
                    print("Please enter a valid number.")
                else:
                    break
            if f_state in ['0', '3']:
                focus_multiplier = 1
            elif f_state == '2':
                focus_multiplier = half_focus
            elif f_state == '1':
                focus_multiplier = bad_focus
        return focus_multiplier, f_state  
    elif f_state == 0:
        f_state = input(syscolor_start + "Starting focus level: [1-3]\n" + color_end)
        if f_state not in ['1', '2', '3']:
            print(errcolor_start + "Please enter a valid number." + color_end)
            f_state = 0
            focus_issues(f_state)
        if f_state in ['0', '3']:
            focus_multiplier = 1
        elif f_state == '2':
            focus_multiplier = half_focus
        elif f_state == '1':
            focus_multiplier = bad_focus
        return focus_multiplier, f_state
    else:
        print(errcolor_start + "Not a valid focus level!?"+ color_end + syscolor_start + "\nCorrecting...\nFocus level reset to 0." + color_end)
        f_state = 0
        focus_issues(f_state)
        return focus_multiplier, f_state

def calculate_read(user, nextuser, message, focus_mult):
    read_pause = [1]
    if nextuser not in [usrone, usrone_alt]:
        focus_mult = 1
    if user != nextuser:
        for i in message:
            read_pause.append(read_time * focus_mult)
        print(syscolor_start + "Time it'll take to read: " + color_end + str(int(sum(read_pause))))
    read_pause = int(sum(read_pause))
    return read_pause

def calculate_check(message):
    check_pause = [0.5]
    for i in message:
        check_pause.append(think_time * 2)
    if beginning_message:
        check_pause = [0]
    check_result = sum(check_pause)
    return check_result

def calculate_think(message, user, focus_mult):
    think_pause = []
    if user in [usrtwo, usrthree]:
        focus_mult = 1
    for i in message:
        think_pause.append(think_time * focus_mult)
    if beginning_message:
        think_pause = [1]
    think_pause = int(sum(think_pause))
    return think_pause

def t9split(message):
    global first_mess
    first_mess = message[:160]
    global second_mess
    second_mess = message [160:320]
    global third_mess
    third_mess = message[320:]
    
# account for focus in typing length
def typingCalc(user, count):
    if user in t9users:
        multiplier = character_typing * focus_mult
    elif user in smartphusers:
        multiplier = word_typing
    base_typing_length = count * multiplier
    return int(base_typing_length)

# find word or character count
def countCalc(user, message):
    character_count = 0
    word_count = 0
    # characters using t9
    if user in t9users:
        for character in message:
            character_count += 1
        count = character_count
    # characters using smartphone
    elif user in smartphusers:
        for word in re.finditer(r"\b\w+?\b", message): 
            word_count += 1
        count = word_count
    # only count messages over 5 characters or 4 words respectively
    if character_count > 5 or word_count > 4:
        base_typing_length = typingCalc(user, count)
    else:
        base_typing_length = 0
    if character_count > 160:
        t9split(message)
    return base_typing_length

# custom indicators
def typingdots(user, typing_iteration):
    # open div without closing in case of multiple blinks
    html.append("<div class=\"relatyping hidden workskin-shown\">")
    user_typing = input(syscolor_start + "Who is typing? (Default: " + color_end + user + syscolor_start + ") " + color_end)
    if user_typing == "":
        user_typing = user
    typing_iter = typing_iteration + 1
    while True:
        # user input
        ty_start = input(syscolor_start + "How long is the pause before the indicator appears? " + color_end)
        try:
            if int(ty_start) not in range(9999):
                print(errcolor_start + "Not a valid number!" + color_end)
                continue
            while True:
                typing_length = input(syscolor_start + "How long is the indicator visible? " + color_end)
                if int(typing_length) not in range(9999):
                    print(errcolor_start + "Not a valid number!" + color_end)
                    continue
                else:
                    break
            delaylist.append(int(ty_start))
            totaldelay = int(sum(delaylist))
            ty_html = f"""
    <p class="text visibly is-typing"><span class="fade-typing"><span class="t{typing_iter}"><strong><small>{user_typing} is typing...</small></strong></span></span></p>
    """
            ty_css = f"""
    #workskin:has(.fadedetails[open]) .t{typing_iter} {{
    visibility: visible;
    transition: visibility {typing_length}s {totaldelay}s;
    }}
    """
            delaylist.append(int(typing_length))
            css.append(ty_css)
            html.append(ty_html)
            more_typing = input(syscolor_start + "Another blink?\n" + color_end).lower()
            if more_typing in ['y', 'yes', 'ok']:
                # don't forget to iterate class
                typing_iter += 1
                continue
            elif more_typing in ["", "n", "no", "back", "quit"]:
                break
            else:
                user_input_all(more_typing)
                break
        except ValueError:
            print("Please enter only a number (in seconds)")
    # close div
    html.append("</div>")
    return typing_iter

# automatic indicators
def autoTyping(user_typing, typing_iteration):
    autoty_html = "None"
    autoty_css = "None"
    time_spent_typing = countCalc(user_typing, message)
    if time_spent_typing == 0:
        print(syscolor_start + "No typing indicator" + color_end)
        return typing_iteration, autoty_html, autoty_css
    # advance class iteration
    typing_iter = typing_iteration + 1
    totaldelay = sum(delaylist)
    autoty_html = f"""<p class="text visibly is-typing"><span class="fade-typing"><span class="t{typing_iter}"><strong><small>{user_typing} is typing...</small></strong></span></span></p>
        """
    autoty_css = f"""#workskin .fadedetails{output_file}[open] .t{typing_iter} {{
visibility: visible;
transition: visibility {time_spent_typing}s {totaldelay}s;
}}"""
    if not beginning_message:
        delaylist.append(time_spent_typing)
    print(successcolor_start + "Automatic typing indicator calculated." + syscolor_start + "\nTime spent typing: " + color_end + str(time_spent_typing) + "s")
    return typing_iter, autoty_html, autoty_css

# auto-bold tagged usernames
def boldtags(boldmessage):
    try:
        nametag = re.sub(r"(@\w+)", r"<strong>\1</strong>", boldmessage)
        return nametag
    # if there is no match, return original message
    except TypeError:
        return boldmessage

def trycss(cclass, cuser, cmessage):
    if cmessage is None:
        return
    totaldelay = sum(delaylist)
    css_result = f"""
#workskin .fadedetails{output_file}[open] .m{cclass} {{
visibility: visible;
transition: visibility 0s {totaldelay}s;
}}

#workskin:not(:has(.notextspeak[open])) .fadedetails{output_file} .text.m{cclass}::after {{
content: "{cmessage}";
}}
"""
    print(syscolor_start + "\nMessage class is " + color_end + "m" + str(cclass) + syscolor_start + "\nTotal delay before message sent is " + color_end + str(totaldelay) + "s")
    return css_result

def singlecss(sclass, smessage):
    css_result = f"""
#workskin:not(:has(.notextspeak[open])) .s{sclass}.text::after {{
content: "{smessage}";
}}
"""
    return css_result

def alt_text(message):
    # user input alt text (base text without workskin and for screen readers)
    baseMessage = input(syscolor_start + "Enter alt text: " + color_end)
    # if user only presses enter, assume the alt text is the same as the starting text
    if baseMessage == "":
        baseMessage = message
    altMessage = boldtags(baseMessage)
    return altMessage

def tryhtml(hclass, huser, hmessage):
    if hmessage == "None":
        return
    altMessage = alt_text(hmessage)
    # if the username is the same as the previous message, don't add the username for this one as well
    global userpersist 
    if userpersist == huser:
        return f"""<p class="text visibly m{hclass}"><span></span><span class="fallback">{altMessage}</span></p>"""
    else:
        userpersist = huser
        return f"""
<p class="username visibly m{hclass}"><strong>{huser}</strong></p>
<p class="text visibly m{hclass}"><span></span><span class="fallback">{altMessage}</span></p>
"""

def singlehtml(sclass, suser, smessage):
    if smessage == "None":
        return
    print(syscolor_start + "Isolated message: " + textcolor_start + suser + ": " + smessage + color_end)
    altMessage = alt_text(smessage)
    while True:
        confirmS = input(syscolor_start + "Confirm" + color_end).lower()
        if confirmS in ['n', 'no', 'retry', 'redo', 'restart', 'back', 'again', 'text', 'alt text']:
            result = singlehtml(sclass, suser, smessage)
            return result
        elif confirmS in ["", "y", "yes"]:
            break
        else:
            user_input_all(confirmS)
    return f"""
<p class="username s{sclass}"><strong>{suser}</strong></p>
<p class="text s{sclass}"><span></span><span class="fallback">{altMessage}</span></p>
    """

def simult(it, nextuser, nextmess):
    # send 0.1 seconds after last message, but eliminate standard 'read' time of 1s
    delaylist.append(0.1 - 1)
    # iterate class
    it += 1
    global it_boost_up
    it_boost_up = it
    print(syscolor_start + "Simultaneous message: " + textcolor_start + nextmess + color_end)
    cssresult = trycss(it, nextuser, nextmess)
    if cssresult is not None:
        css.append(cssresult)
    htmlresult = tryhtml(it, nextuser, nextmess)
    if htmlresult is not None:
        html.append(htmlresult)
    print(successcolor_start + "Message sent simultaneously." + color_end)
    return it

# save and quit
def saveProgress(typing_iteration, it_save):
    save_progress = input(syscolor_start + "'y' to save and quit, or 'skip' to quit without saving.\n" + color_end).lower()
    if save_progress in ['y', 'yes', 'ok', 'save', 'quit', 'q', 'exit']:
        if confirmed == True:
            it_save += 1
        with open(f"{path}olddata.py", "w") as old_data:
            old_data.write("html_intro = f\"\"\"" + html_intro + "\"\"\"\ninput_file = '" + input_file + "'\noutput_file = '" + output_file + "'\nstart = " + str(it_save) + "\ntyping_iteration = " + str(typing_iteration) + "\ndelaylist = " + str(delaylist_save) + "\nuserpersist = '" + userpersist + "'\nf_state = " + str(f_state) + "\nfocus_mult = " + str(focus_mult) + "\nfocus = '" + str(focus) + "'\nmessage = " + "'" + message + "'")
        finalhtml = "\n".join(html)
        finalcss = "\n".join(css)
        with open (f"{path}{output_file}.html", "a") as fohtml:
            print(finalhtml, file=fohtml) 
        with open (f"{path}output.css", "a") as focss:
            print(finalcss, file=focss)
        exit()
    if save_progress == "skip":
        exit()
    else:
        saveProgress(typing_iteration, it_save)

def user_input_all(inputS):
    if inputS in ['y', 'yes']:
        inputS = input(syscolor_start + "Do what? (type, focus, simul, #s) " + color_end).lower()
        user_input_all(inputS)
    elif inputS in ['typing', 'typing_indication', 'typing indication', 'type', 'blinking', 'blink', 'typingdots']:
        global typing_iteration
        typing_iteration = typingdots(user, typing_iteration)
    elif inputS in ['focus', 'focus-issues', 'focus-change', 'focus change']:
        focus_issues(f_state)
    elif inputS in ['simul', 'simult', 'simultaneous', 'same time']:
        simult(it_save, nextuser, nextmess)
    elif inputS in added_time_seconds:
        custom_time = re.match(r"\d{1,4}", inputS).group()
        delaylist.append(int(custom_time))
        print(syscolor_start + "Appended " + color_end + custom_time + syscolor_start + " second(s) to the delay.\nTotal delay: " + color_end + str(sum(delaylist)))
    else:
        print(syscolor_start + "'type' to add a typing indicator.\n'focus' to change the focus level of certain users.\n 'simult' to send this message at the same time as the next.\n''#s' (number of seconds) to add a number of seconds to the total delay." + color_end)
    return 

try:
    with open(input_file, "r") as fin:
        contents = fin.read()
    # divide into individual messages
    messages = contents.strip().split("\n\n")
    for it, msg in enumerate(messages[start:]):
        if it == it_boost_up:
            continue
        it_save = start + it
        # check if this is the last message in the container
        try:
            next_message = messages[it_save + 1]
            (nexttime, nextnotes, nextuser, nextmess) = rmbrackets(next_message)
        except IndexError:
            next_message = ""
        # check if this is the first message in the container
        if it_save == 0:
            prev_message = ""
            (prevtime, prevnotes, prevuser, prevmess) = rmbrackets(prev_message)
            beginning_message = True
        else:
            prev_message = messages[it_save - 1]
            (prevtime, prevnotes, prevuser, prevmess) = rmbrackets(prev_message)
            beginning_message = False
        # to make the save-and-quit behave as intended, I need to track whether the message has been appended or not
        confirmed = False
        # get the components
        (time, notes, user, message) = rmbrackets(msg)
        if user in [usrone, usrone_alt] and focus == 0:
            focus = input(syscolor_start + "Focus issues?\n" + color_end).lower()
            if focus in ['y', 'yes']:
                # ask for user input
                (focus_mult, f_state) = focus_issues(f_state)
            else:
                focus_mult = 1
        if user in t9users:
            countCalc(user, message)
        # if there is only a [note] or less
        if str(user) == "None" or str(message) == "None":
            # check if it's just hesitation time
            try:
                secs = int(time) * 60
                delaylist.append(secs)
                continue
            #else, show the [note] and ask for user input
            except TypeError:
                try:
                    print(textcolor_start + notes + color_end)
                    while True:
                        notes_check = input(syscolor_start + "Do anything with this?\n" + color_end).lower()
                        if notes_check in ['', 'n', 'no']:
                            break
                        else:
                            user_input_all(notes_check)
                    continue
                except TypeError:
                    if time == None and notes == None and user == None:
                        print(textcolor_start + str(message) + color_end)
                        no_mess = input(errcolor_start + "No message detected. Exit? " + color_end).lower()
                        if no_mess in ["y", "yes"]:
                            exit()
                        elif no_mess == "save":
                            saveProgress(typing_iteration, it_save)
                        elif no_mess in [added_time_seconds, 'help', 'focus', 'focus-issues', 'focus-change', 'focus change']: 
                            user_input_all(no_mess)
                        else:
                            if paragraph != True:
                                html.append(html_end)
                            paragraph_normal = ("<p>" + message + "</p>")
                            html.append(paragraph_normal)
                            paragraph = True
                            continue

        # if there is a user and message to find
        # first check if it's a single message all on its own
        if prevnotes == None and prevtime == None and prevuser == None and nextnotes == None and nexttime == None and nextuser == None:
            msg_html = singlehtml(it, user, message)
            if msg_html != "None":
                html.append(msg_html)
            msg_css = singlecss(it, message)
            if msg_css != "None":
                css.append(msg_css)
            continue
        # check if message is the start of a new section (after regular text or at the start of a scene)
        if paragraph or it_save == 0:
            paragraph = False
            html.append(html_intro)
        # look if there is hesitation time
        try:
            hesitation = int(time) * 60
            while True:
                print(textcolor_start + "[" + time + "min] " + user + ": " + message + color_end)
                typing_indicator = input(syscolor_start + "Hesitation? " + color_end).lower()
                if typing_indicator in ['y', 'yes', 'ok']:
                    base_typing_length = countCalc(user, message)
                    print(syscolor_start + "Time it would take to type message: " + color_end + str(base_typing_length) + syscolor_start + "\nSuggested hesitation time: " + color_end + str(hesitation))
                    typing_iteration = typingdots(user, typing_iteration)
                    break
                elif typing_indicator in ['n', 'no', 'none', 'skip']:
                # if custom hesitation not used, revert to auto-calculating 
                    think_pause = calculate_think(message, user)
                    delaylist.append(think_pause)
                    (typing_iteration, autoty_html, autoty_css) = autoTyping(user, typing_iteration)
                    break
                else:
                    user_input_all(typing_indicator)
        # if no time noted (time returns None)
        except TypeError as error:
            print(syscolor_start + "No extra hesitation time noted" + color_end)
            # time to add to delay before message is sent
            think_pause = calculate_think(message, user, focus_mult)
            delaylist.append(think_pause)
            (typing_iteration, autoty_html, autoty_css) = autoTyping(user, typing_iteration)
            # show message
            print(textcolor_start + str(user) + ": " + str(message) + color_end)
        # time to add to delay before message is sent
        check = input(syscolor_start + "Sent without user reading it? " + color_end).lower()
        if check not in ['y', 'yes']:
            check_pause = calculate_check(message)
            delaylist.append(check_pause)
        if first_mess != "None":
            msg_css = trycss(it_save, user, first_mess)
            msg_css = trycss(it_save, user, second_mess)
            msg_css = trycss(it_save, user, third_mess)
        else:
            msg_css = trycss(it_save, user, message)
        if first_mess != "None":
            msg_html = tryhtml(it_save, user, first_mess)
            msg_html = tryhtml(it_save, user, second_mess)
            msg_html = tryhtml(it_save, user, third_mess)
        else:
            msg_html = tryhtml(it_save, user, message)
        # time to add to delay after message is sent
        read_pause = calculate_read(user, nextuser, message, focus_mult)
        delaylist.append(read_pause)
        if nextuser:
            next_pause = []
            think_period = calculate_think(nextmess, nextuser, focus_mult)
            next_pause.append(think_period)
            if read_pause:
                next_pause.append(read_pause)
        if nexttime:
            nexttime = "[" + nexttime + "min] "
        else:
            nexttime = ""
        try:
            it += 1
            if nextuser is None:
                print(syscolor_start + "Next message: " + color_end + str(next_message))
            else:
                print(syscolor_start + "Next message: " + color_end + str(nexttime) + str(nextuser) + ": " + str(nextmess) + syscolor_start + "\nTime before autotyping starts: " + color_end + str('{0:.3g}'.format(sum(next_pause))))
            it -= 1
        except IndexError:
            print(syscolor_start + "Next message: " + color_end + "None")
        # confirm loop
        while True:
            confirm = input(syscolor_start + "Confirm\n" + color_end).lower()
            if confirm == '':
                try:
                    if autoty_html != "None":
                        html.append(autoty_html)
                        css.append(autoty_css)
                except NameError:
                    print(syscolor_start + "No typing indicator was automatically calculated." + color_end)
                if msg_html != "None":
                    html.append(msg_html)
                else:
                    print(syscolor_start + "No HTML to append." + color_end)
                if msg_css != "None":
                    css.append(msg_css)
                else:
                    print(syscolor_start + "No CSS to append." + color_end)
                delaylist_save = delaylist
                confirmed = True
                print(successcolor_start + "Code generated." + color_end)
                break
            elif confirm == 'skip':
                break
            elif confirm in ['retry', 'html', 'message', 'text', 'msg']:
                msg_html = tryhtml(it_save, user, message)
                continue
            elif confirm in ['simul', 'simult', 'simultaneous', 'same time']:
                try:
                    if autoty_html is not None:
                        html.append(autoty_html)
                        css.append(autoty_css)
                except NameError:
                    print(syscolor_start + "No typing indicator was automatically calculated." + color_end)
                if msg_html is not None:
                    html.append(msg_html)
                else:
                    print(syscolor_start + "No HTML to append." + color_end)
                if msg_css is not None:
                    css.append(msg_css)
                else:
                    print(syscolor_start + "No CSS to append." + color_end)
                simult(it, nextuser, nextmess)
                delaylist_save = delaylist
                confirmed = True
                print(successcolor_start + "Code generated." + color_end)
                break
            else:
                user_input_all(confirm)
    html.append(html_end)
    finalhtml = "\n".join(html)
    finalcss = "\n".join(css)
except KeyboardInterrupt:
    saveProgress(typing_iteration, it_save)
except Exception as error:
    print(errcolor_start + "An exception occurred: " + str(error) + color_end)
    saveProgress(typing_iteration, it_save)

# append final code to relevant files
with open(f"{path}{output_file}.html", "a") as fohtml:
    print(finalhtml, file=fohtml) 
with open(f"{path}output.css", "a") as focss:
    print(finalcss, file=focss)

try: 
    os.remove(f"{path}olddata.py")
except IOError:
    print(syscolor_start + "No save data to overwrite." + color_end)

print(successcolor_start + "Done!" + color_end)