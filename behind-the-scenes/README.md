**FEATURES**
- messages appear in real time
- blinking 'Character is typing...' indicator before it's replaced with a message
- option to turn off text-speak style without turning off Creator Style entirely
- readable without Creator's Style on
- fancy button to open chat
- message tails
- optional toggle for color scheme

**To do:**
- try to figure out sound effects frfr
- close-chat button at the end of the chat that then reveals the next open-chat button
- actually design color schemes
  - also a revert button
  - also make the color buttons look nicer
  - also figure out how to extend background to 100% of the fic height (inherit?)
- figure out whether screen readers will read text after transition-delay (if not, warn screen reader users to turn off the workskin)
- test how long of a text message can be replaced before it starts to get messed up (check on mobile too)
- try putting `hidden workskin-shown` classes on relatyping divs

**To do: Python generator**
- update with latest HTMLCSS
- fix `it` resetting after saving (despite `start` saving)
- fix program repeating itself (importing then calling audio_generation.py causes it to repeat)
- add up think-time and read-time and round to the nearest integer before adding them to delay-list
- auto split big doc into scenes for input
- add to generator: iterate `fadedetails` class per section added

**To do: Tutorial**
- explain generator (separate chapter)(when generator is fully functional)