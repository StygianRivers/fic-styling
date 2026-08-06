**FEATURES**
- messages appear in real time
- blinking 'Character is typing...' indicator before it's replaced with a message
- option to turn off text-speak style without turning off Creator Style entirely
- readable without Creator's Style on
- fancy button to open chat
- message tails

**To do:**
- try to figure out sound effects frfr
- close-chat button at the end of the chat that then reveals the next open-chat button
- optional toggle for background and text color?
- figure out whether screen readers will read text after transition-delay (if not, warn screen reader users to turn off the workskin)
- test how long of a text message can be replaced before it starts to get messed up (check on mobile too)
- try relative positioning instead of absolute for overlay

**To do: Python generator**
- fix `it` resetting after saving (despite `start` saving)
- fix program repeating itself (importing then calling audio_generation.py causes it to repeat)
- add up think-time and read-time and round to the nearest integer before adding them to delay-list
- auto split big doc into scenes for input

**To do: Tutorial**
- mention .workskin-shown to prevent clutter
- typing indicators in method 2
- explain generator (separate chapter)(when generator is fully functional)