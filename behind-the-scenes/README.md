**FEATURES**
- messages appear in real time
- blinking 'Character is typing...' indicator before it's replaced with a message
- option to turn off text-speak style without turning off Creator Style entirely
- readable without Creator's Style on
- fancy button to open chat
- message tails
- optional toggle for color scheme

**To do:**
- transition to using details or audio elements for click
- messages transparent background same color as the border but lower opacity
- try to figure out sound effects frfr
- close-chat button at the end of the chat that then reveals the next open-chat button
- figure out whether screen readers will read text after transition-delay (if not, warn screen reader users to turn off the workskin)
- test how long of a text message can be replaced before it starts to get messed up (check on mobile too)

**To do: Python generator**
- update with latest HTMLCSS
- fix `it` resetting after saving (despite `start` saving) (just `start += 1` every iteraton, and use `start` instead of `it`?)
- fix program repeating itself (importing then calling audio_generation.py causes it to repeat)
- add up think-time and read-time and round to the nearest integer before adding them to delay-list
- auto split big doc into scenes for input
- add to generator: iterate `fadedetails` class per section added (can just `fadedetails{output_file}` it)

**To do: Tutorial**
- explain generator (separate chapter)(when generator is fully functional)
- explain: got too excited and forgot elements need to be focusable. So in practice if you're using the `:active` method you should still only use focusable elements (since ao3 doesn't allow adding tabindex to elements)
- color schemes
  - oh cool color schemes. why is this in the chatfic tutorial you ask? Absolute Nightmare
    - this is half a tutorial and half my own attempt to understand my spaghetti code that somehow works
  - eternal mystery of why border properties I apply to userstuff refuse to work
  - transition properties refuse to transition back to original value, even if properly defined. how crazy is that
  - transition property is magic, if someone can explain this code to me I would be so grateful