Workskins for Archive Of Our Own.

**Current projects:** 
based workskin

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
- title::before for the cover image <em>if</em> I can figure out how to add alt text to it
- draw attention to the grcont click-to-reveal
- make work title replacement chance higher in ch9
- details button 'increase size' (lower margins) for ux
- chapter titles just slightly smaller than work title
- credits stick around after the chapter they're revealed (use :is() for the long row of chapters)
- navigator mental link dialogue styling instead of italics (keep html but text-decoration: none;? for workskinless readers) (different for fuuka vs mitsuru)
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

- the title and subtitle should have the option to fill most of the screen, not be squished like that (nowrap for at least the subtitle)
- word wrap is still a problem????? Just the one word on the smallest screen I have, but if it's possible, it's an issue. All the rest of the white space positioning is perfect, though? How
- the musical linebreak should be slightly bigger
- can I make the ficpitch exceed the notes boundaries...? Or at least fill them? They're readable, but so squished
- I suspect ao3 awkwardly put a <br> in the first showcase
- the credits look squished too

Workskinless fixes:

- (action) links once visited should have greyish text, not black text. Put in .actions container?
- for (every?) fic showcase, underneath the show me that fic button, place a workskin-check button with the text "or turn on workskin, and then show the fic" or something similar, and it works (I hope) because you can link the reader back to the relevant chapter endnotes in the same link as you turn on the workskin
- hide fake typeits + cancel OR close with ao3 hidden class
- 1 space after "Loading..."
- <hr> between screxclusive and textspeak in ch2 notes
- grcontent warning add to grcont details

Default site skin fixes:
- why fic showcase links black?? those should be white
- credits need more left and right padding (also just doesn't look good at all)


**Future projects:**
weather boy workskin
behind the scenes workskin