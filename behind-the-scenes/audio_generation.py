import re
from bhind_generator import delay_sound_list, path, output_file

# user input variables
clip_length = 01.02
clip_name = "mixkit-message-pop-alert-2354.mp3"
title = f"""
TITLE: Notification Sounds {output_file} - TRACK 5
FCM: NON-DROP FRAME
"""

with open(f"{path}{output_file}.edl", "w") as output:
    output.write(title)

track_number = 0
# convert clip length into hours-minutes-seconds-centiseconds format
clip_length_formatted = re.sub(r"(\d\d)\.(\d\d?)", r"00:00:\1:\2", str(clip_length))

def correct_formatting(minsechrs):
    number = int(minsechrs)
    if not re.match(r"(\d\d)", str(number)):
        fin_number = re.sub(r"(\d)", r"0\1", str(number))
    return fin_number

# convert seconds into hours-minutes-seconds-centiseconds format
for i in delay_sound_list:
    if i >= 60:
        hours = "00"
        minutes_calc = i / 60
        minutes = re.match(r"(\d+)\.?\d*?", str(minutes_calc)).group(1)
        seconds_string = re.match(r"\d+(\.?\d*)", str(minutes_calc)).group(1)
        seconds = float(seconds_string) * 60
    elif i >= 3600:
        hours_calc = i / 60 / 60
        hours = re.match(r"(\d+)\.\d*?", str(hours_calc)).group(1)
        minutes_string = re.match(r"\d+(\.\d*)", str(hours_calc)).group(1)
        minutes = float(minutes_string) * 60
        seconds_string = re.match(r"\d+(\.?\d*)", str(minutes)).group(1)
        seconds = float(seconds_string) * 60
    else:
        hours = "00"
        minutes = "00"
        seconds = i
    hours = correct_formatting(hours)
    minutes = correct_formatting(minutes)
    seconds = correct_formatting(seconds)
    (secclip, cenclip) = re.match(r"(\d?\d)\.?(\d*)", str(clip_length)).group(1,2)
    end_time_sec = int(seconds) + int(secclip)
    end_time_min = minutes
    if end_time_sec >= 60:
        end_time_min = minutes + 1
        end_time_sec -= 60
    end_time_cen = int(cenclip)
    if end_time_cen >= 100:
        end_time_sec += 1
        end_time_cen -= 100
    end_time_min = correct_formatting(end_time_min)
    end_time_sec = correct_formatting(end_time_sec)
    end_time_cen = correct_formatting(end_time_cen)
    # final format
    start_time = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":00"
    end_time = str(hours) + ":" + str(end_time_min) + ":" + str(end_time_sec) + ":00"
    track_number += 1
    # generate
    single_clip = f"""\n
00{track_number}  AX       A     C        00:00:00:00 {clip_length_formatted} {start_time} {end_time}
* FROM CLIP NAME: {clip_name}
* SOURCE FILE: ../../Videos/Openshot/{clip_name}
* VIDEO LEVEL AT 00:00:00:00 IS 100% BEZIER (REEL AX V)
* AUDIO LEVEL AT 00:00:00:00 IS 0.00 DB BEZIER (REEL AX A1)\n
"""
    with open(f"{path}{output_file}.edl", "a") as output:
        print(single_clip, file=output)
