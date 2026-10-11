#!/usr/bin/env python3

import re
import os

# manual edit variables
groupchatname = "Wild Card Support Group"
usrone = "Minato"
usrone_alt = "Makoto"
usrtwo = "Yu"
usrthree = "Akira"

path = "/home/drift/custom-scripts/fic/behind-the-scenes/"

# delay lengths in seconds
character_typing = 0.3
word_typing = 0.5
# delay lengths per character
read_time = 0.06
think_time = 0.01
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
html = []
css = []
sec_list = []
for i in range(2400):
    sec_list.append(str(i) + "s") 
added_time_seconds = sec_list
# at any user input, you may type #s to add a number of seconds to the delay before continuing what you were doing

# chatroom container
html_end = """
            </div>
        </details>
"""

# review manual edit variables
print(syscolor_start + "Group Chat Name: " + color_end + textcolor_start + groupchatname + color_end + syscolor_start + "\nUser One: " + color_end + textcolor_start + usrone + color_end + syscolor_start + "\nUser One Alternate Username: " + color_end + textcolor_start + usrone_alt + color_end + syscolor_start + "\nUser Two: " + color_end + textcolor_start + usrtwo + color_end + syscolor_start + "\nUser Three: " + color_end + textcolor_start + usrthree + color_end + "\n")

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
        print("Not a valid input")
        # repeat prompt
        big_file_split()

def inputFileName():
    input_f = path + input(syscolor_start + "Which file to generate for?\n" + color_end)
    if os.path.isfile(input_f):
        return input_f
    else:
        print("File does not exist (check file name for errors or change path)")
        # repeat prompt
        inputFileName()

try:
    # check for save data
    from olddata import *
except ImportError:
    # no save data, start fresh
    print(syscolor_start + "No previous data found." + color_end)
    big_file_split()
    input_file = inputFileName()
    output_file = re.match(r"(?:.*\/)(.+)\..*", input_file).group(1)
    focus = input(syscolor_start + "Focus issues in this section?\n" + color_end).lower()
    start = 0
    typing_iteration = 0
    delaylist = []
    delay_sound_list = []
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
    regmatch = re.match(r"(\[(\d*)min\s?\])?(\[.*\])?(\*\*(.*):\*\*)? ?(.*)?", onemessage)
    time_indication = regmatch[2]
    fic_notes = regmatch[3]
    username = regmatch[5]
    message_body = regmatch[6]
    return time_indication, fic_notes, username, message_body

def focus_issues(f_state):
    if f_state in ['1', '2', '3']:
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
        f_state = input(syscolor_start + "Starting focus level? [1-3]\n" + color_end)
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

# account for focus in typing length
def typingCalc(user, count):
    if user in [usrone, usrone_alt]:
        multiplier = character_typing * focus_mult
    else:
        multiplier = word_typing
    base_typing_length = count * multiplier
    return int(base_typing_length)

# find word or character count
def countCalc(user, message):
    character_count = 0
    word_count = 0
    # characters using t9
    if user in [usrone, usrone_alt]:
        for character in message:
            character_count += 1
        count = character_count
    # characters using smartphone
    elif user in [usrtwo, usrthree]:
        for word in re.finditer(r"\b\w+?\b", message): 
            word_count += 1
        count = word_count
    # only count messages over 5 characters or 4 words respectively
    if character_count > 5 or word_count > 4:
        base_typing_length = typingCalc(user, count)
    else:
        base_typing_length = 0
    return base_typing_length

# custom indicators
def typingdots(user, typing_iteration):
    # open div without closing in case of multiple blinks
    html.append("<div class=\"relatyping hidden workskin-shown\">")
    user_typing = input(syscolor_start + "Who is typing? (Default: " + user + ")\n" + color_end)
    if user_typing == "":
        user_typing = user
    typing_iter = typing_iteration + 1
    while True:
        # user input
        ty_start = input(syscolor_start + "How long is the pause before the indicator appears?\n" + color_end)
        if int(ty_start) not in range(9999):
            print(errcolor_start + "Not a valid number!" + color_end)
            continue
        while True:
            typing_length = input(syscolor_start + "How long is the indicator visible?\n" + color_end)
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
        else:
            break
    # close div
    html.append("</div>")
    return typing_iter

# automatic indicators
def autoTyping(user_typing, typing_iteration):
    autoty_html = "None"
    autoty_css = "None"
    time_spent_typing = countCalc(user_typing, message)
    if time_spent_typing == 0:
        return typing_iteration, autoty_html, autoty_css
    # advance class iteration
    typing_iter = typing_iteration + 1
    totaldelay = sum(delaylist)
    autoty_html = f"""
    <p class="text visibly is-typing"><span class="fade-typing"><span class="t{typing_iter}"><strong><small>{user_typing} is typing...</small></strong></span></span></p>
        """
    autoty_css = f"""#workskin .fadedetails{output_file}[open] .t{typing_iter} {{
visibility: visible;
transition: visibility {time_spent_typing}s {totaldelay}s;
}}"""
    delaylist.append(time_spent_typing)
    return typing_iter, autoty_html, autoty_css

# auto-bold tagged usernames
def boldtags(boldmessage):
    try:
        nametag = re.sub(r"(@(Minato|Makoto|Yu|Akira))", r"<strong>\1</strong>", boldmessage) # can't figure out how to make regex read variables like usrone
        return nametag
    # if there is no match, return original message
    except TypeError:
        return boldmessage

def trycss(cclass, cuser, cmessage):
    totaldelay = int(sum(delaylist))
    # exact time at which message is sent (to later add notification sounds)
    delay_sound_list.append(totaldelay)
    css_result = f"""
#workskin .fadedetails{output_file}[open] .m{cclass} {{
visibility: visible;
transition: visibility 0s {totaldelay}s;
}}

#workskin:not(:has(.notextspeak[open])) .fadedetails{output_file} .text.m{cclass}::after {{
content: "{cmessage}";
}}
"""
    return css_result

def tryhtml(hclass, huser, hmessage):
    # user input alt text (base text without workskin and for screen readers)
    baseMessage = input(syscolor_start + "Enter alt text:\n" + color_end)
    # if user only presses enter, assume the alt text is the same as the starting text
    if baseMessage == "":
        baseMessage = hmessage
    altMessage = boldtags(baseMessage)
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

# save and quit
def saveProgress(typing_iteration, it_save):
    save_progress = input(syscolor_start + "'y' to save and quit, or 'skip' to quit without saving\n" + color_end).lower()
    if save_progress in ['y', 'yes', 'ok', 'save', 'quit', 'q', 'exit']:
        if confirmed == True:
            it_save += 1
        with open(f"{path}olddata.py", "w") as old_data:
            old_data.write("input_file = \"" + input_file + "\"\noutput_file = \"" + output_file + "\"\nstart = " + str(it_save) + "\ntyping_iteration = " + str(typing_iteration) + "\ndelaylist = " + str(delaylist_save) + "\nuserpersist = \"" + userpersist + "\"" + "\nf_state = " + str(f_state) + "\nfocus_mult = " + str(focus_mult) + "\nfocus = " + "\"n\"" + "\ndelay_sound_list = " + str(delay_sound_list))
        finalhtml = "\n".join(html)
        finalcss = "\n".join(css)
        with open (f"{path}{output_file}.html", "a") as fohtml:
            print(finalhtml, file=fohtml) 
        with open (f"{path}output.css", "a") as focss:
            print(finalcss, file=focss)
        exit()
    if save_progress == "skip":
        exit()

try:
    with open(input_file, "r") as fin:
        contents = fin.read()
    # divide into individual messages
    messages = contents.strip().split("\n\n")
    if focus in ['y', 'yes']:
        # ask for user input
        (focus_mult, f_state) = focus_issues(f_state)
    else:
        focus_mult = 1
    for it, msg in enumerate(messages[start:]):
        it_save = start + it
        # to make the save-and-quit behave as intended, I need to track whether the message has been appended or not
        confirmed = False
        # get the components
        (time, notes, user, message) = rmbrackets(msg)
        think_pause = []
        # if there is only a [note]
        if str(user) == "None" or str(message) == "None":
            # check if it's just hesitation time
            try:
                secs = int(time) * 60
                delaylist.append(secs)
                continue
            #else, show the [note] and ask for user input
            except TypeError:
                print(textcolor_start + notes + color_end)
                while True:
                    notes_check = input(syscolor_start + "Do anything with this?\n" + color_end).lower()
                    if notes_check in ['y', 'yes']:
                        notes_check = input(syscolor_start + "Do what? (type, focus)\n" + color_end).lower()
                    elif notes_check in ['typing', 'typing_indication', 'typing indication', 'type', 'blinking', 'blink', 'typingdots']:
                        typing_iteration = typingdots(user, typing_iteration)
                    elif notes_check in ['focus', 'focus-issues', 'change-focus', 'focus-change']:
                        (focus_mult, f_state) = focus_issues(f_state)
                    elif notes_check in added_time_seconds:
                        custom_time = re.match(r"\d{1,4}", notes_check).group()
                        delaylist.append(int(custom_time))
                        print(syscolor_start + "Appended " + custom_time + "seconds to the delay." + color_end)
                    else:
                        break
                continue
        # if there is a user and message to find
        # first look if there is hesitation time
        try:
            hesitation = int(time) * 60
            while True:
                print(textcolor_start + "[" + time + "min] " + user + ": " + message + color_end)
                typing_indicator = input(syscolor_start + "Hesitation?\n" + color_end).lower()
                if typing_indicator in ['y', 'yes', 'ok']:
                    base_typing_length = countCalc(user, message)
                    print(syscolor_start + "Time it would take to type message: " + color_end + str(base_typing_length) + syscolor_start + "\nSuggested hesitation time: " + color_end + str(hesitation))
                    typing_iteration = typingdots(user, typing_iteration)
                    break
                elif typing_indicator in added_time_seconds:
                    custom_time = re.match(r"\d{1,4}", typing_indicator).group()
                    delaylist.append(int(custom_time))
                    print(syscolor_start + "Appended " + custom_time + " seconds to the delay." + color_end)
                # if custom hesitation not used, revert to auto-calculating 
                else:
                    for i in message:
                        think_pause.append(think_time * focus_mult)
                    delaylist.append(int(sum(think_pause)))
                    (typing_iteration, autoty_html, autoty_css) = autoTyping(user, typing_iteration)
                    break
        # if no time noted (time returns None)
        except TypeError as error:
            print(syscolor_start + "No hesitation time noted" + color_end)
            # show message
            print(textcolor_start + user + ": " + message + color_end)
            for i in message:
                # time to add to delay before message is sent
                think_pause.append(think_time * focus_mult)
            delaylist.append(int(sum(think_pause)))
            (typing_iteration, autoty_html, autoty_css) = autoTyping(user, typing_iteration)
        # time to add to delay before message is sent
        read_pause = []
        for i in message: 
            read_pause.append(read_time * focus_mult)
        delaylist.append(int(sum(read_pause)))
        msg_css = trycss(it_save, user, message)
        msg_html = tryhtml(it_save, user, message)
        # time to add to delay after message is sent
        read_pause = []
        for i in message: 
            read_pause.append(read_time * focus_mult)
        delaylist.append(int(sum(read_pause)))
        # confirm loop
        while True:
            print(syscolor_start + "Resulting HTML:" + color_end + msg_html)
            print(syscolor_start + "Resulting CSS:" + color_end + msg_css)
            print(syscolor_start + "Confirm" + color_end)
            confirm = input().lower()
            if confirm == '':
                if autoty_html is not "None":
                    html.append(autoty_html)
                    css.append(autoty_css)
                html.append(msg_html)
                css.append(msg_css)
                delaylist_save = delaylist
                confirmed = True
                break
            elif confirm == 'skip':
                break
            elif confirm in ['retry', 'html', 'message', 'text', 'msg']:
                msg_html = tryhtml(it_save, user, message)
                continue
            elif confirm in added_time_seconds:
                custom_time = re.match(r"\d{1,4}", confirm)
                delaylist.append(int(custom_time.group()))
                print(syscolor_start + "Appended " + str(custom_time.group()) + " seconds to the delay." + color_end)
                continue
            else:
                print(errcolor_start + "Type 'skip' to skip this message, or 'retry' to change the input." + color_end)
    html.append(html_end)
    # try:
        # from audio_generation import *
        # generate()
    # except ImportError:
        # print("Audio generator could not be found.")
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