label a1_b3_shipyards:
"I should check out the shipyards."

scene shipyards
"There's several people here, probably all from muster."
"As I see them walk into one warehouse, deafening explosions come from another."

scene warehouse1
show unknown
with easeinbottom

"The man speaks into a recorder."
un "R&D Notes. Attempt 15: failed. It doesn't seem to be the fuzes.":
un "Returning to launch device. Powder bags are a no go."

menu: #choice 1
    "I probably shouldn't be here, it's dangerous!":
        i: "I should go."
        "I turn away to leave, but accidentally bump into someone."
    "I probably should help put out the fire he just made.":
        i: "Need help in there?"
        un "Yes, please."
        "I grab a fire extinguisher and help him snuff out the fires."

show Maya_Bae
with easeinbottom

mb: "What's up nerd, start another fire?"
un "...maybe. "
mb "Who's the new girl?"
un "I don't know. I though it was you cheating on Maya again."
mb "Oi!"
"Maya's apparent boyfriend picks up a hammer from a nearby table and raises it."
"His face also morphs into a frog's. The explosives guy doesn't seem to care."
un "So, new girl. What's your name?"
i "I'm Ibuki. I'm a new shipgirl who got stationed here."
un "Welcome to hell. I'm Unknown, the R&D and MP guy."
un "That AA obsessed monkey over there is Maya_Bae, but we just call him Mayo."
un "He's der fuhrer around these parts."
return
