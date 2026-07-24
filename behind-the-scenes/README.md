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
- insert typing indications if message is long, automatic length based on user ID and message length, wrap in relatyping divs
  - if user = minato, count message characters and produce a set typing length based on that (but only for anything over 5 characters)
  - if user != minato, count message words(separated by spaces) and produce a set typing length based on that (but only for anything over 4 words)
- make sure time indicators on their own line aren't counted as messages