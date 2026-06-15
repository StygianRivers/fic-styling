**FEATURES**
- messages appear in real time
- blinking 'Character is typing...' indicator before it's replaced with a message
- option to turn off text-speak style without turning off Creator Style entirely
- readable without Creator's Style on
- fancy button to open chat
- message tails


**To do:**

- amalgamate chatfic workskins into frankenstein's workskin
- figure out whether screen readers will read text after transition-delay (if not, warn screen reader users to turn off the workskin)
- test hover outside of codepen
- test how long of a text message can be replaced before it starts to get messed up (check on mobile too)
- test on ao3

**Generator**
- define chatters (option to select colors to make the background of their messages? to distinguish)
- add messages (1 button per chatter, freely available)
- delete messages
- easy bold-text option (for tagging chatters)
- add alt text to each message
- apply 'tail' class to each message preceded by another chatter's message (can't do this in pure CSS because of all the character-is-typing messages in-between)
- transition delay in seconds input (or in seconds since last message's input? may be more workable)
- 'character is typing' indicator add buttons
  - pick how long it stays visible
- actually generate html
**Super optional**
- add option to remove all tails
- add option to switch between workskin styling
- add the option for more chatters
- add the option for POV chatter
- make 'character is typing' text customizable
- add the option to pick colored usernames and borders for each chatter
- option to change message order
