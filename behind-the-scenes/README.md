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
- auto-bold tags ( @.* )
- if preceding message is by the same user, remove username for current message
- insert typing indications if message is long, automatic length based on user ID and message length, wrap in relatyping divs
  - if user = minato, count message characters and produce a set typing length based on that (but only for anything over 5 characters)
  - if user != minato, count message words(separated by spaces) and produce a set typing length based on that (but only for anything over 4 words)
- insert custom typing indicators for each [#*] indicating hesitation, option of multiple typing indicators per [#*]
  - leave out [string] indicators without a number at the start
  - wrap multiple sibling indicators in a single relatyping div 
- iterate each typing indication to add .t# class
- per hmessage, input alt text that will become the default
  - ideally the messages would appear one by one and let me type alt text for each, without having to format it manually at all, then immediately move on to the next message when I hit enter
    - replacing the hmessage text with the alt text at that point
- per message, input number to output transition delay (add to last message's or indicator's delay number)
- per typing indication, input two numbers to output transition delay and blink duration

