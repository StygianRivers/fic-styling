sticky pop-up **menu**

- base: skill, item, persona, stats, quest, social link, calendar, system
  - yen count? Could update per chapter, but what about readers reading in full work mode? (Ah wait I can tie yen gain/loss in with the items buttons)
  - party members count!! Possibly, button to 'go to tartarus' activating the party member icons, with any members that are written in as being in the party locked in, and any undetermined characters in your party you can choose to replace
    - in tartarus: CYOA sections - button that periodically appears that you can press for Reaper fight? They're non-canon (because SEES always dies), optional, and static scenes, but it's a good measure of the party's strength at that point in the fic
      - could be a link to a separate chapter that changes in content based on what ID is attached, while the intro and probably deaths get to remain largely the same
        - Tartarus as a whole could be its own chapter where parts keep changing based on the ID you link to
        - you'd need to make that workskin-less-accessible, or at the very least not extremely confusing
  - probably make **skills** and **persona** inactive (that darker blue color and not a <details>) because those would canonically change way too often to keep track of
    - maybe Persona works but the only Persona it ever shows is Orpheus (...and later Thanatos too)
    - or Persona and Skills submenu works but only change per chapter, if I really want to challenge my creativity in coming up with Persona stats and abilities
  - probably don't minic the sub-menu screens, only the functionality
  - I could make the explanatory text pop up for each menu item when :focus-ing them, but... Seems like a lot of effort for very little reward
- item submenu: opens only key items, if there are other 'tabs' they're inactive
- buttons in-fic to 'pick up' items (they won't last to the next chapter but that doesn't matter, whether the reader presses the button or not they're canonically picked up, so I can just put them as default in the next chapter(s), same with yen and stat and persona updates)
- stats: stats
- quest: current protagonist sidequests!!!
- social link: grid of cards using that one workskin card graphic, overlaying the arcana as icon. Clicking on one... I know I can make it a link, but can I make it a <details>? I'd like clicking on it to open a more detailed view of that one card with the others disappearing (card flip transition)
- calendar: I could totally make this work with radio buttons. I wouldn't need to figure out a way to switch month screens if I make sure the month shown on screen is always the current one (which I should do either way). effect is displaying that button's assigned date information to the right of the calendar.
  - if the date is both in a past chapter and noteworthy, add a link displaying as a 'memory' that links back to the written out event. would help returning readers catch up if they don't remember some events
- maybe don't leave out system submenu. maybe add system functionality in the form of picking background music at any time
  - except when in Tartarus (entire Dark Hour if it's possible to section that off subtly). music player dead
  - music player graphic
  - 'loop' checkbox
    - have the reader pick loop or no loop before making the music options clickable, have different audio elements available depending on their choice
  - track how many songs are available the same way as items/yen states
  - have game songs 'autoplay' when reader is navigating through choices
    - make optional
    - when opening the menu move the invisible controls of currently playing music to be over background music picking, so opening that submenu pauses the playing music while also still opening the menu (select: audio active (infinite) and menu open for this rule)
- also possibly in system menu
  - screenreader check
  - reduced motion options
  - check content warnings (entire fic and chapter-specific)
  - hide graphic content
    - separate checkboxes for each kind of graphic content you can hide
  - name input/change
  - no custom background images
    - no images, only image descriptions where relevant
  - turn off work skin entirely
  - 'send developer feedback' that just links you to the comments
  - tutorial page where you can re-read all tutorials

Actually, on page load (and therefore on refresh), pop up system menu with accessibility/input options- anything that's not been saved in the page ID. (just name input?)(all, if there is no :target active, implying they pressed the regular next chapter button)


Deeply necessary: (immersively styled) graphic TUTORIAL boxes, rather than author's notes that people tend to skip over. Examples:

TUTORIAL
In chapter-by-chapter reading mode, the settings that would be reset by refreshing the page will instead be maintained if you use the above buttons to navigate to the next chapter.

TUTORIAL
If your screen reader is willing to work with pseudoelements, and you're willing to navigate the clunky keyboard, you can make use of the custom name input feature. If not, simply skip to the main content with the default name input.

TUTORIAL
Refreshing the page resets the name input. When using a custom name, it's recommended to read this fic in Entire Work mode to avoid having to re-enter your name.

TUTORIAL
Click on the arrow on the left side of your screen to access the menu.

MUSIC 1/3
'Autoplay' will start playing ambient songs as you navigate the page. It's turned off by default. If do you want music, but more direct control over it, you can find your available music in the system menu. 

MUSIC 2/3
Press pause on the music player before navigating to the next or previous song, to prevent the songs from overlapping.

MUSIC 3/3
You will unlock more songs throughout the course of the fic. Don't forget to click the button to download them to your music player. 

COMBAT
In combat, you control only your own player character, while other characters act on their own. You will not natively be able to see the enemy status, your own status, or your teammates' status.

YOUR TURN
When it's your turn in combat, choose between three options: **Attack**, **Item**, or **Persona**.

YOUR TURN
**Attack:** Attack with your melee weapon.
**Item:** Use a consumable from your inventory.

YOUR TURN
**Persona:** Summon a Persona from your stock.
Through a Persona, you can use Skills to help your allies or hinder your enemies.

PERSONA
Skills cost 1 SP each. You won't be able to see, yourself, how much SP you have left, but you will notice when you run out. SP refills fully upon sleeping at the dorm, but there are also items that can temporarily boost your SP, if you can find them.

PERSONA 
Over time, your Persona will level up, giving you access to a more advanced skillset and a higher max SP. 

PASSIVE SKILLS
These skills are always active, and therefore not directly usable in combat. You can still hover over them to see what effect they provide.

SHUFFLE TIME
After a successful combat, you'll receive a random card. These cards have various beneficial effects and will take effect immediately upon pick-up. 

FUSION
In the Velvet Room, you can fuse your gathered Personas into new, more powerful Personas. Talk to Elizabeth for more information on how to fuse. 

FUSION
Elizabeth has very exacting standards. If you don't fuse the Persona she requests before you leave Tartarus, she won't save any of your Personas gathered today in the Persona Compendium. Don't worry, though, you can always try again later.

COMPENDIUM
Now that you have some Personas registered in the Persona Compendium, you may summon them at will. You'll only need to pay a small tribute in return.

SOCIAL LINKS
Occasionally, you may form a bond of a very special kind. This 'social link' increases the power of your fused Personas, and may come with additional benefits in the future. 

THE REAPER
Run, and pray it does not catch you.


Any non-Makoto interlude chapter(make them chapters not just sections): menu does not appear in that chapter (unless reading in full work mode)(full work mode readers will have to just deal with the menu not matching canon if they're too lazy to press any of the buttons)(what if they refresh the page though?) 
- music does not autoplay either even if the reader picked that option before
- put an update-menu button of some kind at the very start of the fic and put the update it causes as a default in every chapter after one. Then if it's *not* active, which indicates a reader in full work mode who either hasn't been pressing buttons or refreshed the page, throw up an ERROR in the menu rather than any incorrect data. Still same font as the details list.

Epilogue:
- menu is there (more indication that POV is still (partially) Makoto's)
- when opening the menu, all you get is an ERROR (selector: :has(#chapter-[epiloguenumber]) AND :has(#chapter-1) .last-stat-change (The Universe added? Full work readers would not get the chance to see the other cards disappear before they see the error, but chapter-by-chapter readers would))

Known issue to figure out: ao3 broke sticky by limiting overflow-y?

State changes:
Make states changes `details` to keep track of open/close state.

Most things are added to the base state after every chapter - if I give the option to pick up a key item in ch2, that will show up in the menu after choosing that option in ch2, but won't need to be carried over to ch3 (it will always be in the menu in ch3). Those are 'canon events'. Character stats also need to be canon.

State changes that are optional are different. If these are selected in a chapter, they should carry over to the next, even when reading chapter-by-chapter.
  - fic-wide graphic content hidden
  - last played song (to default to in system menu)
  - autoplay on/off
  - screenreader status
  - reduced motion on/off
  - all images/no images/no background images
  - consider offering music descriptions for Deaf readers
  How many possible combinations this would result in depends on the number of songs available.

  Modular Tartarus is its own whole thing.
  The first one or two Tartarus trips are static, but once the tutorial is over, the Tartarus button shows up on every free night and is wholly optional. Link would change based on MC's mood, character development, and what characters can join them.

  Rough draft:
  Base Tartarus (starting May - Mitsuru, Yukari, and Junpei - focused)
  Bad mood #bm
  Bloodlust (bored or angry) #bloodlust
  With Akihiko #aki
  With Fuuka (starting June) #fuuka
  Without Mitsuru (starting June) #nomitsu
  With Aegis (starting July) #aegis
  With Koromaru (starting August) #koro
  With Ken (starting September) #ken
  With Shinjiro (starting September, ending October) #shinji
  Full party (starting September, ending October) #all

  #bm-aki
  #bloodlust-aki
  #bm-fuuka
  #bloodlust-fuuka
  #aki-fuuka
  #bm-aki-fuuka
  #bloodlust-aki-fuuka
  #aki-nomitsu
  #bm-aki-nomitsu
  #bloodlust-aki-nomitsu
  #aki-aegis
  #bm-aki-aegis
  #bloodlust-aki-aegis
  #aki-fuuka-aegis
  #bm-aki-fuuka-aegis
  #bloodlust-aki-fuuka-aegis
  #aki-fuuka-aegis-nomitsu
  ...
  You get the idea. Every time there's a 'go to tartarus' button available, link the relevant components, then make sure the target exists. If it doesn't yet, write the relevant part.
  On a normal trip where the party isn't locked in, the reader is free to choose their party. 

  Let's say I go to Tartarus in a bad mood, with Aegis and Akihiko, without Mitsuru, at the twelfth option. The button links to #12-bm-aki-nomitsu-aegis. The HTML would then be:

  <a name="12-bm-aki-nomitsu-aegis"></a>
  <div class="aki-nomitsu-aegis">This is the reader's choice of party members: in this case they get to choose from Junpei, Yukari, Aegis, and Akihiko.</div>

  <div class="default">This is the full contents of the Tartarus trip. The dialogue within changes based on what `details` were opened in the character selection above, and could be changed by RNG to make Tartarus trips less repetitive.</div>
  <div class="bm hidden">This is the full contents of the Tartarus trip when MC is in a bad mood. The dialogue within changes based on what `details` were opened in the character selection above, and could be changed by RNG to make Tartarus trips less repetitive.</div>
  <div class="bloodlust hidden">This is the full contents of the Tartarus trip when MC is out for blood. The dialogue within changes based on what `details` were opened in the character selection above, and could be changed by RNG to make Tartarus trips less repetitive.</div>
  <a class="T-12 hidden" href="back to the button you came from">Retire for the night</a>

  The relevant CSS would then be:
#workskin [name$="bm-aki-nomitsu-aegis"]:target ~ .aki-nomitsu-aegis {
  display: block;
}

#workskin [name*="bm"]:target ~ .hidden.bm {
  display: block;
}

#workskin [name*="bm"]:target ~ .default, #workskin [name^="bloodlust"]:target ~ .default {
  display: none;
}

#workskin [name^="12"]:target ~ .T-12 {
  display: block;
}

I think, when arriving in the Tartarus chapter... I think it takes the trip number (t12 for example) and shows an action (details) with class .expand_all that corresponds to the trip number. So if trip 12 is in late June, it opens the invisible details of `.fuukanavigator` and `.june`, and uses that later on to determine what to show. I think that's the same, functionally, but more human-readable than packing it all into the trip number in the CSS.

At the end of the chapter, when reading chapter by chapter: fake next chapter buttons to keep the settings save states, of course, but also fake previous chapter buttons that do that same in case the reader wants to glance back real quick.


Turn based combat:
- random enemies
  - each floor should have 4+ predetermined combinations of 5 enemies that could appear on that floor. the combinations are randomly generated before being added to the CSS
  - max 5 enemies per floor, they do not respawn that same trip even if you 'teleport'
- shuffle time
  - winning battles gives a predetermined reward based on the enemy
    - if a reward would give a persona, but reader already has that persona registered, they get money instead
    - money is used (only in that same Tartarus trip) to summon Personas to fuse. The amount is not communicated back to the main story or saved over multiple trips.
      - if I'm willing to make sure the shuffle times are all siblings and all have the same path to the money descendant, I could get more specific with amounts gathered. based on the number of sibling details open, Elizabeth could parrot the number back to you (finite only because you stop getting any money rewards after the number reaches 10,000)
        - increments of 500? that's only 20 css rules and 20 matching html spans for Elizabeth to parrot it back to you
      - each persona summoning costs 1,000 yen
        - personas you gather and fuse in the velvet room are not the same as what you use in Tartarus. You can't pick up a Persona from shuffle time and start fighting with it
          - whenever you enter Tartarus after the first assignment, you get to pick a(ny) persona(s) of choice to add to your stock, for free. This is to fight with on that trip, specifically, and you can't use it for fusion.
            - your stock is 1 + number-of-finished-assignments
              - your stock is to fight with. you can hold an infinite amount of Personas for fusion purposes
          - could I change this? (yes, but I'd have to keep track of how full the stock is throughout the tartarus trip, and figure out a way for the reader to release the Personas they took with them at the start of Tartarus to make room)
      - you can only summon Personas once you've completed the assignment in which they were used, therefore registering them, and slept a night or more on it. You can't use them in the same trip you register them
        - I could make it work otherwise with extra effort, but I don't care enough to. this seems fair to me
        - yen rewards won't show up before you complete the first assignment (because you can't use any of the money)
      - you do enter Tartarus with a fixed (but low) amount of money every time. 1000 yen? enough to summon one persona if you've previously registered it
  - card graphic?
- compendium
  - Elizabeths gives the reader an assignment whenever they enter the velvet room (in order, based on what assignment was completed last)
    - pick fusions for the assignments
      - and their skills (could be custom)(should be custom, no revival or other things that will be useless in this battle system)(the explicitly fused assignment Personas can have predetermined inherited skills)
        - skills don't have to be visible while fusing, since there's no user choice involved in picking them
    - when completing a fusion assignment, all Personas involved will be registered in the compendium and can be summoned for money while in Tartarus or in the Velvet Room
      - the Velvet Room chapter needs to be in the Tartarus chapter to make this possible
  - all your compendium personas, and all of your allies' Personas, level up several levels after every full moon (canonically they're gradually leveling up, but this way I only have to keep track of the month rather than an ever-rising number) (it's all for show, anyway, since the enemies don't get harder over time, at least at this point in development)
- graphic effects
  - ?
- custom moves (with graphic support)
  - black out
- figure out if and how the planned confidant perks will interact with this battle system
  - Play Dead means that you mechanically cannot lose - if you get knocked out, either your friends finish the job or, if they're forced to scatter, you just wake up later
    - when you genuinely get knocked out and Play Dead activates, it's a mysterious[Elizabet's] voice that wakes you up, encouraging you and saying it's not yet your time
    - getting knocked out still means no shuffle time, though
- predetermined movesets for every party member
  - determine special movesets for bosses with gimmicks to them
  - after determining movesets and determining which moveset would count for which enemy, I can calculate exactly how much health the enemy would lose based on who is in the party, not accounting for the reader input choices
  - no 1-mores, just automatic all out attacks when a character would get 1-more
- all out attacks
  - if a weakness is hit, once per turn, do an extra 2x the normal damage (and display a message that an all out attack was used)
  - but not when MC is the only one in the party, or ailed/down with only one other party member standing
- If MC is low health, one of his party members will heal him if possible, but he has to be so low health that- no actually, they won't heal him unless Fuuka tells them he's dangerously low on health, and even Fuuka can't always tell, because if the enemy hits with an affinity he's weak to he might go from middling health to knocked out
- only MC can get ailed or 'knocked out'
  - pre-Solo Incident, 'knocked out' has him still awake and somewhat aware but unable to bring himself to get back up
  - code: whenever a party member deviates from their moveset to heal or cure MC, they're locked into attacking next turn
    - whenever Fuuka tells the party to heal MC: Yukari will do it if she's in the party, else Ken will do it, else Akihiko will do it, else pm2 will use a healing item, if there are no healers and no healing items nothing happens
    - whenever MC is ailed: Yukari will cure him, else pm2 will use a cure item, if no Yukari and no cure items the ailment will go away after 4 turns
      - I guess to take items into Tartarus (in addition to finding/earning them in Tartarus) there's a pop up every time the reader enters Tartarus, telling them that they brought some items in and letting them select 3 of a bunch of different restoration items 
        - once the third sibling `details` is opened, disappear the pop up
  - figure out if I'm smart enough to allow enemies to get ailed
    - if not, don't give the characters ailment skills or items
  - what's the point in MC having healing skills then?? figure this out 
    - (or: have Makoto think exactly that same thought throughout the fic.)
- there are no revival items in play, though they exist and are used in lore
  - dwi
- SP. there will be SP tracking.
  - again MC only, the party members will make sure they don't run out of SP themselves
  - amount of skills open per battle... how to most efficiently count that?
  - could add it to the end of the :target link and select it in the next battle with `[name$="SP30"]` (which selects any anchor that has that at the end, so I could use different anchors to keep the other save states, still)
  - if you have an SP recovery item in your inventory (chosen at the start of the trip) it's used automatically, you just have some more SP to spend, since you can't save it for another trip anyway
  - you should be able to ask Fuuka (after she joins) where your SP is at. She may not give you an exact number (a reader wouldn't know what to do with an exact number) but she'll give you a good idea and alert you if it's dangerously low.
  - health isn't preserved between battles like SP is probably
- teleporter???
  - the teleporting action (as well as moving up a floor) should be jarring and disruptive as if refreshing the page. but do not refresh the page
- when a reader is reading in entire work mode, they don't see the link that leads to the tartarus chapter, but instead a link that only has the anchor (so their page doesn't refresh at any point)
- can I code buffs to matter?
- should figure out exactly how much Guarding reduces damage, and how to code that
- need to figure out enemy health tracking in detail
  - should be able to ask Fuuka how close the enemy is to dying, too
    - should be able to ask Fuuka to tell you the enemy weaknesses and skills, but it takes the rest of your turn
- some occasional enemies have, instead of 4 movesets, 3 regular movesets and 1 moveset where they start the fight ailed (fear, confusion, or rage)
- skills are selectable in the battle based on which Persona is active (empty, hidden skill slots overlapping, add a size and `content` label to the skill slots with the appropriate classes for the reader to pick from)
- maybe at this point just warn users of older screen readers to stay away from the turn based combat entirely, with how much I seem to need to use pseudoelements without being able to use fallbacks because there is no appropriate default. They're not missing out on plot relevant information.
