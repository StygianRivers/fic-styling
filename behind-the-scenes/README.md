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

**Python generator**
- auto-bold tags ( @.* )
- if preceding message is by the same user, remove username
- add output file (one css, one html)
- iterate each message to add m# class
- insert typing indications if message is long, automatic length based on user ID and message length, wrap in relatyping divs
- insert custom typing indicators for each [#min] indicating hesitation, option multiple per
  - wrap multiple sibling indicators in relatyping div 
- iterate each typing indication to add t# class
- per hmessage, input alt text that will become the default
- per message, input number to output transition delay (add to last message's delay number)
- per typing indication, input two numbers to output transition delay and blink duration
- generate the css of those classes (using hmessage for content)
- relatyping divs

**Optional makes-my-life-easier**
- type messages without markdown to have them immediately added to the output file with the same html formatting 


**Optional Fancy GUI Generator**

**would need**
- add alt text to each message
- transition delay in seconds input (or in seconds since last message's input? may be more workable)
- 'character is typing' indicator add buttons
  - pick how long it stays visible
**Super optional**
- add option to remove all tails
- add option to switch between workskin styling
- add the option for more chatters
- add the option for POV chatter
- make 'character is typing' text customizable
- add the option to pick colored usernames and borders for each chatter
- option to change message order

