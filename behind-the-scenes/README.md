**FEATURES**
- messages appear in real time
- blinking 'Character is typing...' indicator before it's replaced with a message
- option to turn off text-speak style without turning off Creator Style entirely
- readable without Creator's Style on
- fancy button to open chat
  - next button won't show up until previous chat is opened
- message tails
- optional toggle for color scheme
- HTML/CSS generator

**To do:**
- try to figure out sound effects frfr
- figure out whether screen readers will read text after transition-delay (if not, warn screen reader users to turn off the workskin)
- test how long of a text message can be replaced before it starts to get messed up (check on mobile too)

**To do: Python generator**
- function to edit original message when shown it
- simult() should skip the next iteration of the for loop
- paragraph handling
  - single text messages surrounded by paragraphs aren't wrapped in phone container or transitioned
- test all functions
  - t9 splitting
  - do all possible inputs handle invalid input smoothly?
  - don't exit the program completely when encountering a non-message paragraph
  - simult() reading iteration correctly
- try to determine the proper read/think times frfr
- rewrite it but better
  - if name is main
  - function to append to html list
  - function to append to css list
  - function to append to delaylist
  - function to save progress separate from asking for input on saving progress
  - function to reset to the start of the for loop but keeping the iteration
  - try / except format for checking input validity

**To do: Tutorial**
- explain generator (separate chapter)(when generator is fully functional)
- method 2 generator???
  