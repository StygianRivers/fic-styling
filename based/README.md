Features:
- Hiding work end notes on every chapter except the relevant ones
- Metadata styling
  - Chapter title replacement
  - Randomized title (custom percentage chance)
- Custom `<hr>`
- Name selection for multiple characters
- Text-speak replacement
- Graphic content optional replacement
- Consideration for whether the reader needs to re-do selections
- Explanatory comments in the workskin

To do:
- find someone with ancient screen reading technology to test all the screen reader accommodation
- upload a total 15 test chapters to test full functionality
- draw attention to the grcont click-to-reveal
- make work title replacement chance higher in ch9
- details button 'increase size' (lower margins) for ux
- chapter titles just slightly smaller than work title
- credits stick around after the chapter they're revealed (use :is() for the long row of chapters)
- navigator mental link dialogue styling instead of italics (keep html but font-style: normal;? for workskinless readers) (different for fuuka vs mitsuru)
- P3(R) key item-get graphic as linebreak for stuff like bobby pins, epipen, friendship bracelet,

Tested on ao3. Fixes to make:
- fix gr-content switch paragraph gap
- fix 'fix textspeak' function
- get rid of the pointless scroll bar in chapter 3
- make deskbuttons work again
  - wtf is teeny flexing for
  - rewrite pulley cycle
  - text should vanish when 'closing' file
- fix the showcase
  - remove blockquote line
  - fix button
  - remove link underline unless hovered
- add regular link underlines back
- ao3 deleting `&nbsp;` ???
- why is the Close text so tiny?? The Cancel text looks fine??
- awkward breaks in top notes (hidden text)

Mobile fixes:

- the title should have the option to fill most of the screen, not be squished like that 
- word wrap is still a problem????? Just the one word on the smallest screen I have, but if it's possible, it's an issue. All the rest of the white space positioning is perfect, though? How
- can I make the ficpitch exceed the notes boundaries...? Or at least fill them? They're readable, but so squished
- the credits look squished too

Workskinless fixes:
- (action) links once visited should have greyish text, not black text. Put in .actions container?

Default site skin fixes:
- why fic showcase links black?? those should be white