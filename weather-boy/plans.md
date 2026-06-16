sticky pop-up **menu**

- base: skill, item, persona, stats, quest, social link, calendar (leave out system)
  - yen count? Could update per chapter, but what about readers reading in full work mode? (Ah wait I can tie yen gain/loss in with the items buttons)
  - party members count!! Possibly, button to 'go to tartarus' activating the party member icons, with any members that are written in as being in the party locked in, and any undetermined characters in your party you can choose to replace
    - in tartarus: CYOA sections - button that periodically appears that you can press for Reaper fight? They're non-canon (because SEES always dies), optional, and static scenes, but it's a good measure of the party's strength at that point in the fic
  - probably make **skills** and **persona** inactive (that darker blue color and not a <details>) because those would canonically change way too often to keep track of
    - maybe Persona works but the only Persona it ever shows is Orpheus (...and later Thanatos too)
  - probably don't minic the sub-menu screens, only the functionality
  - I could make the explanatory text pop up for each menu item when :focus-ing them, but... Seems like a lot of effort for very little reward
- item submenu: opens only key items, if there are other 'tabs' they're inactive
- buttons in-fic to 'pick up' items (they won't last to the next chapter but that doesn't matter, whether the reader presses the button or not they're canonically picked up, so I can just put them as default in the next chapter(s), same with yen and stat and persona updates)
- stats: stats
- quest: current protagonist sidequests!!!
- social link: grid of cards using that one workskin card graphic, overlaying the arcana as icon. Clicking on one... I know I can make it a link, but can I make it a <details>? I'd like clicking on it to open a more detailed view of that one card with the others disappearing, but that might be too much
- calendar: I could totally make this work with up to 31 <details> per month. I wouldn't need to figure out a way to switch month screens if I make sure the month shown on screen is always the current one (which I should do either way). :focus should have the same effect as [open], which is displaying that <details>' assigned information to the right of the calendar.

Any non-Makoto interlude chapter(make them chapters not just sections): menu does not appear in that chapter (unless reading in full work mode)(full work mode readers will have to just deal with the menu not matching canon if they're too lazy to press any of the buttons)(what if they refresh the page though?) 
- put an update-menu button of some kind at the very start of the fic and put the update it causes as a default in every chapter after one. Then if it's *not* active, which indicates a reader in full work mode who either hasn't been pressing buttons or refreshed the page, throw up an ERROR in the menu rather than any data. Still same font as the details list.

Epilogue:
- menu is there (more indication that POV is still (partially) Makoto's)
- when opening the menu, all you get is an ERROR (selector: :has(#chapter-[epiloguenumber]) AND :has(#chapter-1) .last-stat-change (The Universe added? Full work readers would not get the chance to see the other cards disappear before they see the error, but chapter-by-chapter readers would))

Known issue to figure out: ao3 broke sticky a few days ago?