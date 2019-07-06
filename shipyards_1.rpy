label shipyards_1:
    "Off to the shipyards it is, then."

    scene shipyards
    "There's several people here, probably all from muster."
    "As I see them walk into one warehouse, deafening explosions come from another."

    scene warehouse1
    show unknown
    with easeinbottom

    "The man speaks into a recorder."

    usn "R&D Notes. Attempt 15: failed. It doesn't seem to be the fuzes."

    usn "Returning to launch device. Powder bags are a no go."

    menu: #choice 1
        "I probably shouldn't be here, it's dangerous!":
            i "I should go."

            "I turn away to leave, but accidentally bump into someone."

        "I probably should help put out the fire he just made.": #I need to look at documentation again for points. #Scoots' note: Done.
            $ unknownPoints += 1
            i "Need help in there?"
            usn "Yes, please."
            "The man looks too nonchilant for starting a massive fire."
            "I grab a fire extinguisher and help him snuff out said fires."

    show Maya_Bae at right
    with easeinbottom
    mm "What's up nerd, start another fire?"
    usn "...maybe. "
    mm "Who's the new girl?"
    usn "I don't know. I though it was you cheating on Maya again."
    mm "Oi!"
    "Maya's apparent boyfriend picks up a hammer from a nearby table and raises it."
    "His face also morphs into a frog's. The explosives guy doesn't seem to care." #Insert badly photoshopped poggers sprite here?
    usn "So, new girl. What's your name?"
    i "I'm Ibuki. I'm a new shipgirl who got stationed here."
    un "Welcome to hell. I'm Unknown, the R&D guy and MP."
    un "That AA obsessed monkey over there is Maya_Bae, but we just call him Mayo."
    un "He's der führer around these parts."

    mb "hit ur face"
    un "As you can see, he's also {i}super witty{/i}."
    un "So, what can I do you for? Need some rigging or something?"
    i "Oh, no, I'm just finding my way around the base."
    un "Well, you picked a good time to come by. There's gonna be some exercises soon. It'll make for a good show."
    mb "So how's the 25mm cannon for the wifey going?"
    un "Poorly. Shooting more literal crap in the sky won't shoot down more planes."
    mb "Your guns are poo poo."
    un "I'm just making them according to spec, plus some. There's no improving on those."
    mb "ur face"
    un "That's something a middle schooler would say."
    "Mayo opens his mouth, but a loud bell rings, and a voice over the loudspeaker announces the start of live fire exercises."

    scene ocean_exercises
    "Another loud explosion rings in the distance, as exercises begin. Six fellow shipgirls are out there."
    "I'm told their names are Kirishima, Suzuya, Kumano, Souryuu, Akizuki, and Shiranui. They seem very well equipped."
    "Kirishima has a strange gun on her turret. It's covered in a yellow and black wrap. I'm instantly nervous as that could only mean one thing."
    "Almost as if reading my thoughts, Unknown speaks up."
    un "Like the new gun? I made that for her. Kirishima's pretty damn good at marksmanship, so I wanted to see if she could use the extra firepower."
    un "It's an autoloading 14 inch/50 caliber triple battery."
    i "Isn't that American technology?"
    un "Do I look Japanese to you?"#ngl best fuckin line
    i "Where'd you get the blueprints from?"
    un "I gotta keep some secrets."

    "Unknown shrugs with a suspicious smirk. I don't think I'm finding out any time soon."
    "Kirishima moves in position to fire. I dive behind the nearest form of cover, a tree."
    "Surprisingly, the gun doesn't explode on itself and actually puts out several shots precisely on target."
    "Suddenly, the fleet shifts into a diamond formation, and everyone looks skyward."
    "Tracers and a curtain of flak fill the sky as training drones are shot down. Akizuki in particular looks like she's doing the bulk of the work."

    scene ocean_exercises_sunset
    un "The eight minutes of death. They not only would've survived a nightmarish situation, but actually beat it back. Not bad."
    i "Eight minutes of death?"
    un "Our original benchmarks for this exercise wiped out everyone at eight minutes, give or take. But this fleet managed to run through it. So, what looked the best to you?"
    un "I need feedback, since I'm the armorer here."
    menu: #choice 2
        "I think the surface warfare part was great. Especially Kirishima's guns.": #plus Unknown points
            $ unknownPoints += 1
            un "Yeah, it took a long time getting that right. Minaturization is a pain in the ass with the budget we have."
            un "But it definitely was worth it. Now, time to go get feedback from Kirishima herself. See ya 'round, new girl.'"
            "Unknown excuses himself and jogs towards the docks."
        "I think the AA was the coolest part.": #plus Mayo point
            $ mayoPoint = True
            mb "If you think that was good, my wifey's a goddess at AA!"
            un "Where the hell did you come from?"
            mb "Dongcan."
            un "The hell does that even mean? Well, I'm gonna go get some feedback on the guns from Kirishima before Mayo's IQ rubs off on me."
            mb "Oi!"
            "Unknown sprints off as Mayo, still holding the hammer from the warehouse, chases after him. Mayo struggles to keep up with him."

    "I check my watch, and it's getting late. Who knew high explosives could take a few hours? I head back to my quarters."
    return
