import re

# example variables for testing purposes
delay_sound_list = [3,5,18,28,33]
output_file = "/home/drift/custom-scripts/fic/behind-the-scenes/testing"

# user input variables
clip_length = 01.02
clip_name = "mixkit-message-pop-alert-2354.mp3"
title = f"""
TITLE: Notification Sounds {output_file} - TRACK 5
FCM: NON-DROP FRAME
"""

with open(f"{output_file}.edl", "w") as output:
    output.write(title)

track_number = 0
# convert clip length into hours-minutes-seconds-centiseconds format
clip_length_formatted = re.sub(r"(\d?\d)\.(\d\d?)", r"00:00:\1:\2", str(clip_length))

# convert seconds into hours-minutes-seconds-centiseconds format
for i in delay_sound_list:
    if i >= 60:
        hours = "00"
        minutes = i / 60
        seconds_string = re.match(r"\d+(\.?\d*)", str(minutes)).group()
        seconds = int(seconds_string) * 60
        centiseconds_string = re.match(r"\d+(\.\d*)?", str(seconds)).group()
        centiseconds = int(centiseconds) * 60
    elif i >= 3600:
        hours = i / 60 / 60
        minutes_string = re.match(r"\d+(\.\d*)", str(hours)).group()
        minutes = int(minutes_string) * 60
        seconds_string = re.match(r"\d+(\.?\d*)", str(minutes)).group()
        seconds = int(seconds_string) * 60
        centiseconds_string = re.match(r"\d+(\.\d*)?", str(seconds)).group()
        centiseconds = int(centiseconds) * 60
    else:
        hours = "00"
        minutes = "00"
        seconds = i
        centiseconds_string = re.match(r"\d+(\.\d*)?", str(seconds)).group()
        centiseconds = int(centiseconds_string) * 60
    (secclip, cenclip) = re.match(r"(\d?\d)\.?(\d*)", str(clip_length)).group(1,2)
    end_time_sec = seconds + int(secclip)
    end_time_min = minutes
    if end_time_sec >= 60:
        end_time_min = minutes + 1
        end_time_sec -= 60
    end_time_cen = centiseconds + int(cenclip)
    if end_time_cen >= 100:
        end_time_sec += 1
        end_time_cen -= 100
    start_time = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + str(centiseconds)
    end_time = str(hours) + ":" + str(end_time_min) + ":" + str(end_time_sec) + ":" + str(end_time_cen)
    track_number += 1
    # generate
    single_clip = f"""\n
00{track_number}  AX       A     C        00:00:00:00 {clip_length_formatted} {start_time} {end_time}
* FROM CLIP NAME: {clip_name}
* SOURCE FILE: ../../Videos/Openshot/{clip_name}
* VIDEO LEVEL AT 00:00:00:00 IS 100% BEZIER (REEL AX V)
* AUDIO LEVEL AT 00:00:00:00 IS 0.00 DB BEZIER (REEL AX A1)\n
"""
    with open(f"{output_file}.edl", "a") as output:
        print(single_clip, file=output)
