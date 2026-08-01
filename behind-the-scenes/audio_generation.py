import re

clip_length = 01.02
clip_name = "mixkit-message-pop-alert-2354.mp3"
title = f"""
TITLE: Notification Sounds {output_file} - TRACK 5
FCM: NON-DROP FRAME
"""
#example delay_sound_list for testing purposes
delay_sound_list = [3,5,18,28,33]

with open("{output_file}.edl", "w") as output:
    output.write(title)

track_number = 1
#default start
start_silent_section = "00:00:00:00"
# convert clip length into hours-minutes-seconds-centiseconds format
clip_length_formatted = re.sub(r"(\d?\d)\.(\d\d?)", r"00:00:\1:\2", clip_length)

# convert seconds into hours-minutes-seconds-centiseconds format
for i in delay_sound_list:
    if i >= 60:
        hours = "00"
        minutes = i / 60
        seconds = re.match(r"\d+(\.\d*)", minutes) * 60
        centiseconds = re.match(r"\d+(\.\d*)", seconds) * 60
    elif i >= 3600:
        hours = i / 60 / 60
        minutes = re.match(r"\d+(\.\d*)", hours) * 60
        seconds = re.match(r"\d+(\.\d*)", minutes) * 60
        centiseconds = re.match(r"\d+(\.\d*)", seconds) * 60
    else:
        hours = "00"
        minutes = "00"
        seconds = i
        centiseconds = re.match(r"\d+(\.\d*)", seconds) * 60
    (secclip, cenclip) = re.match(r"(\d?\d)\.(\d)", clip_length)
    end_time_sec = seconds + secclip
    if end_time_sec >= 60:
        end_time_min += 1
        end_time_sec -= 60
    end_time_cen = centiseconds + cenclip
    if end_time_cen >= 100:
        end_time_sec += 1
        end_time_cen -= 100
    start_time = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + str(centiseconds)
    end_time = str(hours) + ":" + str(end_time_min) + ":" + str(end_time_sec) + ":" + str(end_time_cen)
    track_number += 2
    track_number_increase = track_number + 1
    # generate
    single_clip = f"""\n
00{track_number}  BL       V     C        00:00:00:00 00:00:00:00 {start_silent_section} {start_time}
00{track_number_increase}  AX       A     C        00:00:00:00 {clip_length_formatted} {start_time} {end_time}
* FROM CLIP NAME: {clip_name}
* SOURCE FILE: ../../Videos/Openshot/{clip_name}
* VIDEO LEVEL AT 00:00:00:00 IS 100% BEZIER (REEL AX V)
* AUDIO LEVEL AT 00:00:00:00 IS 0.00 DB BEZIER (REEL AX A1)\n
"""
    output.append(single_clip)
    # pass the end time to the next iteration
    start_section = end_time

output.close()