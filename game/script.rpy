define hacker = Character("Hacker", color="#FF0000", what_prefix="~ ", what_suffix=" ~")
define narrator = Character(None)
define aisha = Character("Aisha")
default name = "MC"

image MChappy = im.Scale("MChappy.png", 500, 600)
image MCangry = im.Scale("MCangry.png", 500, 600)
image MCsad = im.Scale("MCsad.png", 500, 600)
image MCmyst = im.Scale("MCmyst.png", 500, 600)

image hacker = "hacker.webp"

image aisha happy = im.Scale("aisha_happy.png", 500, 600)
image aisha sad = im.Scale("aisha_sad.png", 500, 600)

image bg school_day = "bg_school_day.png"
image bg school_night = "bg_school_night.png"
image bg park_eve = "bg_park_eve.png"

label start:

    scene bg school_day
    with dissolve
    
    play music "audio/bgm.ogg" fadein 1.0

    show MChappy
    $ pn = renpy.input("Whats your name default MC")
    $ pn = pn.strip()
    if pn == "":
        $ pn = "MC"

    $ name = pn 

    $ mc = Character(name)

    mc "It's already 8:00 PM Everyone's gone home except me..."
    mc "Just one more page left for the science project, ahh"

    show msg
    with dissolve

    narrator "----- I know your secret!!!!! Play my game or I'll tell everyone -----"
    stop sound
    play sound "audio/typing.mp3"

    hide msg
    show MCangry

    mc "What the...???!!! Who's messing with me???!!"

    menu:
        "Ignore the message":
            jump ignore
        "Open the link":
            jump openg

label ignore:

    show MCsad
    mc "No way... It's just some prank. I'm not falling for this."

    "The phone screen goes dark. But the next morning, rumors spread across school..."
    "My secret... exposed."

    "Bad Ending: Ignorance isn't always bliss."

    stop music fadeout 1.0
    jump credits

label openg:

    stop music fadeout 1.0
    stop sound
    play sound "audio/secret.ogg"

    scene bg school_night
    with dissolve
 

    show MCmyst
    
    mc "What is this...? The classroom... glitched?"
    window hide
    scene bg school_night with hpunch
    window show

    show hacker

    hacker "Welcome to my game."

    menu:
        "Who are you?":
            jump who
        "Disconnect immediately":
            jump disconnect

label who:

    show MCangry
    mc "Who are you? Why are you doing this?"

    show hacker
    hacker "I'm the consequence of your lies. The one you tried to delete."

    mc "I don't understand!"

    hacker "Do you remember... the incident last summer?"

    mc "No... I didn't mean for that to happen..."

    show MCsad
    mc "That was an accident..."

    jump fb

label fb:

    scene bg park_eve
    with fade

    stop sound
    stop music fadeout 1.0
    play music "audio/streets.ogg" fadein 1.0

    show aisha happy at truecenter
    narrator "Last summer... before everything went wrong."

    narrator "Aisha wasn't just kind. She was the kind of person who made you believe the world wasn't all bad."

    aisha "Hey [name], you look like you're carrying the whole world on your back again."

    mc "Hah... Just school stuff. You know how it is."

    aisha "I do. But you forget I'm the queen of last minute homework. Want me to bring snacks next time? Brains work better with sugar."

    mc "(laughs) Maybe you're right."

    aisha "Promise me something? Don't bottle things up. Life's hard enough without fighting it alone."

    mc "I... yeah. Promise."

    narrator "She meant it. That was Aisha. Always the first to notice when someone was hurting."

    narrator "And I "

    hide aisha happy
    show aisha sad at truecenter
    with dissolve

    narrator "I let her down."

    narrator "We were messing around online. A harmless joke. Or so we thought."

    narrator "We never imagined it would spread like wildfire."

    mc "I remember the moment her secret got out... the moment the messages started... the way people laughed behind her back."

    narrator "The next day, Aisha didn't come to school."

    narrator "Days passed. Then weeks."

    narrator "Some said her parents moved her away. Others whispered that... something worse happened."

    show MCsad at truecenter
    with dissolve

    mc "I tried to tell myself it wasn't my fault... that I didn't mean for any of it."

    mc "But deep down... I knew. I let it happen. I watched."

    narrator "Her smile... I can't forget it. And I can't forgive myself."

    stop sound
    stop music fadeout 1.0
    play music "audio/bgm.ogg"
    jump conf



label conf:

    scene bg school_night
    show hacker
    show MCsad

    hacker "Accident or not, someone paid the price. And now it's your turn."

    menu:
        "Apologize sincerely":
            jump apologize
        "Refuse to take blame":
            jump deny

label apologize:

    show MCsad
    mc "I'm sorry... I truly am. I was scared. I didn't know what to do."

    hacker "It's too late for apologies. But I will offer you a chance..."

    hacker "Play my game. Win, and the past stays buried. Lose, and everyone will know."

    mc "What kind of game?"

    hacker "You'll find out... soon."

    stop music fadeout 1.0
    jump ep2


label deny:

    show MCangry
    mc "No! This isn't my fault. You can't blackmail me over something I didn't do."

    hacker "Denial... I expected as much."

    hacker "Very well. Let the first challenge begin."

    window hide
    scene bg school_night with hpunch
    window show

    stop music fadeout 1.0
    jump ep2


label disconnect:

    show MCsad
    mc "Forget this. I'm out."

    "I shut off the laptop. The classroom lights flicker."
    "But my phone lights up... the message is still there."

    "I can't escape."

    stop music fadeout 1.0
    jump ep2


label ep2:

    scene bg school_night
    with fade

    stop music fadeout 1.0
    play music "audio/dark.mp3" fadein 1.0

    show MCmyst
    mc "Where... where am I?"

    show hacker
    hacker "Welcome to Level One."

    hacker "Every choice you make from now on will have consequences. Are you ready to play?"

    mc "I don't even know what this is! What do you want from me?"

    hacker "Redemption... or Ruin. It's your choice."

    narrator "The air feels cold. The classroom I knew is gone replaced by darkness and flickering screens."

    narrator "In the distance, I hear... something. A faint echo. Aisha's voice?"

    stop sound
    play sound "audio/whisper.mp3"

    narrator "A whisper. Faint. 'Why... why did you...?'"

    mc "No... stop it!"

    show MCangry
    mc "This is just a nightmare. It has to be."

    hacker "Nightmare? Perhaps. Or perhaps your punishment has only just begun."

    hacker "Your first challenge is simple: Tell the truth. Or lie."
    menu:
        "Tell the truth about what happened":
            jump tru
        "Lie to protect yourself":
            jump lie

label tru:

    show MCsad
    mc "It was me. I was part of it. I laughed... I didn't stop it. I ruined her life."

    hacker "Honesty... rare these days."

    hacker "You may proceed to the next round."

    narrator "The darkness seems to lift, just a little. But I can still feel the weight of guilt crushing me."

    "To be continued..."
    stop sound
    stop music fadeout 1.0
    jump ep3

label lie:

    show MCangry
    mc "I didn't do anything! It wasn't my fault! People overreacted!"

    hacker "A lie, even now. Disappointing."

    hacker "Let the punishment begin."

    window hide
    scene bg school_night with hpunch
    window show

    stop sound
    play sound "audio/glitch.mp3"

    narrator "The screens around me shatter. The world dissolves into static."

    narrator "And then... silence."

    "To be continued..."

    jump ep3



label ep3:

    scene black
    with fade
    stop sound
    stop music fadeout 1.0
    play music "audio/nightmare.ogg" fadein 2.0

    show text "Episode 3: The Mirror" with dissolve
    pause 3

    scene bg school_night
    with fade

    show MCsad
    mc "I don't know how long I've been here. This endless game... the choices... none of it makes sense."

    narrator "The classroom melts into darkness. The screens around me flicker with distorted reflections of myself."

    show hacker
    hacker "Welcome to the final level."

    mc "What do you want? Who even are you?!"

    hacker "You still don't understand, do you?"

    window hide
    scene bg school_night with hpunch
    window show
    narrator "The Hacker's face glitches pixels tear apart.  
    For a brief moment... I see my own eyes staring back."

    mc "...What...?"

    hacker "I am the you that remembers. The you that can't forget. The you that still hears her voice at night."

    mc "No... You're lying."

    hacker "I am your guilt."

    narrator "My head pounds. I fall to my knees. The air vibrates with static."

    hacker "One last game. One last truth. Survive this... or fade into oblivion."

    menu:
        "Face the truth":
            jump t1
        "Run from it":
            jump ref

label ref:

    mc "I won't do this... I won't face it."

    hacker "Then you choose oblivion."

    stop music fadeout 1.0
    play sound "audio/bad.mp3"
    scene black
    narrator "Everything collapses into darkness."

    narrator "Bad Ending: Self Destruction."

    jump credits

label t1:

    scene bg park_eve
    with fade

    play music "audio/streets.ogg" fadein 1.0

    window hide
    scene bg park_eve with hpunch
    window show
    narrator "The park. Twisted. Burning with glitching fragments of my past."

    show MCmyst
    mc "This is... me. My memory."

    show aisha sad
    aisha "Why did you abandon me?"

    hacker "First Trial: Speak the truth. What was your real reason for staying silent?"

    menu:
        "I was afraid they'd turn on me.":
            jump tru1
        "I didn't think it would matter.":
            jump lie1

label tru1:

    show MCsad
    mc "I was terrified. I thought... if I spoke up, I'd be next."

    hacker "Cowardice... but honesty. Proceed."

    jump t2

label lie1:

    show MCangry
    mc "It didn't matter! It was just a joke!"

    hacker "Liar."

    narrator "The park cracks. Aisha screams in digital static."

    jump t2

label t2:

    scene bg school_night
    with fade

    show hacker

    hacker "Second Trial: Regret or Denial."

    hacker "When she disappeared... what did you truly feel?"

    menu:
        "I felt empty. Guilty.":
            jump r2
        "I felt relieved it wasn't me.":
            jump d2

label r2:

    show MCsad
    mc "I... I hated myself for it. I still do."

    hacker "A wound acknowledged can begin to heal. Proceed."

    jump final

label d2:

    show MCangry
    mc "Honestly... I was relieved. I was safe."

    hacker "Even now you hide. But the truth will consume you."

    jump final

label final:

    scene bg school_night
    with fade

    show hacker

    hacker "This is your last choice"

    window hide
    scene bg school_night with hpunch
    window show
    narrator "The glitching face fully resolves it's me. I am the Hacker. The guilt, the fear, the memory I tried to bury."

    show MCsad
    mc "I... I understand now."

    hacker "Choose: Live with the memory. Or erase it, and lose yourself forever."

    menu:
        "Live with the guilt become whole":
            jump endg
        "Erase it forget forever":
            jump endb

label endg:

    show MCsad
    mc "I will remember. I will carry this. I will change."

    narrator "The false world shatters. Light pours in."

    stop music fadeout 2.0
    stop sound
    play sound "audio/good.mp3"

    scene bg park_eve
    with dissolve

    narrator "I wake up. Tears on my face. But something's different. I'm free."

    "Good Ending: Integration."

    jump credits

label endb:

    show MCangry
    mc "Erase it. I don't want to remember."

    narrator "The Hacker my own reflection smiles."

    stop music fadeout 2.0
    stop sound
    play sound "audio/bad.mp3"

    scene black

    narrator "I wake up... hollow. Empty. A shell."

    "Bad Ending--- Oblivion."

    jump credits

label credits:

    narrator "Thank you for playing this game"
    narrator "This story was created by me Anirudh Sahu, who started this journey with nothing but an idea and Hack Club's support"
    narrator "I have always loved building things whether it was coding designing or just creating stories that make people feel something"
    narrator "This visual novel is one small step in my learning journey and I hope it touched you in some way"

    narrator "If you enjoyed this or just want to say hi you can find me on Hack Club Slack at '@Anirudh'' or check out my projects on GitHub https://github.com/Anirudh12032008"

    narrator "Keep building keep dreaming and most importantly never stop being curious"

    return
