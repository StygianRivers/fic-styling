**FEATURES**
- messages appear in real time
- blinking 'Character is typing...' indicator before it's replaced with a message
- option to turn off text-speak style without turning off Creator Style entirely
- readable without Creator's Style on
- fancy button to open chat
- message tails

**To do:**

- figure out whether screen readers will read text after transition-delay (if not, warn screen reader users to turn off the workskin)
- test hover outside of codepen
- test how long of a text message can be replaced before it starts to get messed up (check on mobile too)
- test on ao3

**To do: Python generator**
- either autotyping or typingdots function per message, not both
  - typingdots and autotyping distinction is a mess, typingdots is called from multiple different places?? 
    - possibly need to initiate autotyping from main, then within autotyping after doing the calculations give the choice to continue autotyping or to switch to manual input (typingdots)
- auto split big doc into scenes for input
- fix typing_iteration not saving (tried, now test it)
- make sure time indicators on their own line aren't counted as messages
- if [#min] stands on its own, # * 60 and append to delay-list. If it stands in front of a message, ask for user input on typing indication
  - don't ask for typing indication input if no [#min] in front of message
- wrap autotyping in relatyping divs with optional user input
- when fatal error occurs, save before exiting program