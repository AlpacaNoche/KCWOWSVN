label a1_b1_room:
"I should check out the room and get my things sorted in there."

"..."
"Wait, where exactly is the dormitories?"

"I turn around and yell over to the Admiral."
i "{b}HEEEY! SCOOOTS! DO YOU KNOW WHERE THE WAY TO THE DORMS IS?{/b}"
"He quickly runs over to me, and points down the hallway."
s "First left. Take the second right and the exit should be down the hallway. Building is first on the left."
"Scoots then turns right back around and dashes back into his office. I yell a 'thank you' back to him and continue on my way." #bit mixed on this line

scene dormbuilding
"After a bit, I make it there. It seems to be somewhat quie-"
"Suddenly, a gorilla-like roar sounds from inside."
i "What the hell?"
"This base is already crazy enough it seems like-- can it get any worse?"
"I still decide to head inside, hopefully I won't bump into whatever *that* was."

scene dormfrontdesk
"Wait, is there any clerk here like Scoots mentioned?"
"With second glance throughout the room, I actually spot the clerk.."#I'm debating on keeping this part or not, with Kosena sleeping. Might not match his character.
show KosenaSleepy
"...except he's passed out on the desk."
smk "{i}..mm...paint thinnerrr....{/i}"
"What?"
i "Uh, hello?"
show KosenaSurprised
smk "..oh! Ah, hello!"
show Kosena
"A quick look at his nametag tells me his name-- Kosena. Weird."
i "Hi, I'm the newest ship posted here, Ibuki."
ks "Ibuki-san? Alright, give me a moment."
"He quickly goes to typing on his computer on the desk, before shifting around in its drawer. He then pulls out a key, and hands me it."
ks "Here you go. Room forty-two, it's on the second floor, A wing."
i "Thank you, make sure to grab some more sleep tonight."
"Kosena blushes in embarassment before returning to a straight face."
ks "Alright, alright. Ring me up if you need anything sorted out related to your room."

"I quickly go up the flight of stairs to my right."
show dormHallway
"Hm, wing A, right? Should be right ther-"
#insert slamming noise
smi "AH!"
scene blank
scene alpacaTrippedOver
"It appears that I have slammed into a small woman." #this line is like half of a joke
smi "{i}I am so sorry, that was my fault..{/i}"
"She scrambles to grab the papers she dropped everywhere."

menu: #Alpaca choice #1
    "What should I do?"
    "Help her out.":
        $ alpaca_status = "yes"
        jump a1_b1_alpaca
    "Keep moving.":
        "She should've been watching where she was going."
        scene dormHallway
"I keep moving along, ignoring her."


label a1_b1_continued:
"I arrive to my room, after a little bit of walking."
scene door42
"Moving in to open the door, I suddenly hear some rather loud discussion from within."
"Two voices, both girls. It must be Suzuya and Kumano, the people Scoots mentioned."
"I gently open the door."
scene dormDoorPeek
return
