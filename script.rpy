# Character definitions.

define i = Character("Ibuki")
define sm = Character("Smol Man") #scoots before introduction to ibuki
define smK = Character("Sleeping Man") #kosena before introduction to Ibuki
define sc = Character("Scoots")
define dm = Character("Daishomaru")
define bi = Character("Bike")
define mb = Character("Maya_Bae")
define ab = Character("Aobaka")
define ap = Character("Alpaca")
define un = Character("LT Unknown")
define wg = Character("Wororg")
define sa = Character("Saxon")
define ks = Character("Kosena")

# The hell begins here.

label start:

scene waterside

"A light breeze passes as I step out of the taxi."
"Today, my destiny marches onward."

scene officebuilding
"Ahead of me lies Wagyu Naval Base, the home of the Joint Anti-Abyssal Staff, my new family."
"However, just as I try to enter the building, a small man in an American uniform bumps into me on his way out."

show scoots
with easeinbottom

sm "Oh, hello! Didn't see ya there."
sm "Haven't seen ya around here, what's your name?"
i "I'm Ibuki. I was posted here today."
sm "I'm Admiral Scoots. I manage the tech side of things around here."
menu:
    "How should I respond?"
    "Neat.": #this option will probably give +1 to scoots
        i "Neat."
    "Okay then.": #will probably just be a plain neutral
        i "Okay then."
sc "You're a shipgirl, eh? Lemme sign you into the system and get you on your way."
i "Thank you."
"He opens the door again and leads the way."

scene hallway
"After a bit of walking, we arrive to his office."
scene scootsoffice
show scoots
"He takes a seat in his office chair and prepares to type. I pull up my own seat and lay my backpack next to it."
sc "Alright, so you're Ibuki, yes?"
i "Correct."
"We converse for a bit, with not much going on other than him typing." #I'm not really sure about this line
"Suddenly, we both hear maniacal laugh in the distance. Scoots sighs and shakes his head."#it's daisho, y'all!
sc "Oh for fucks sake."
i "Hm? What was that?"
sc "It was fucking Daisho again."
"More laughter echos throughout the hallways."
i "Who's Daisho?"
sc "He's the base's idiot. I don't know why he's even here."
menu:
    "This sounds somewhat interesting. What should I do?"
    "Investigate!": #begins Daisho's route
        jump act1_daisho
    "Stay here.": #continues main route
        i "Sounds like a lunatic."
sc "About right, yeah."
"After a few more questions back and forth, he picks up his phone and dials a number." #I honestly dislike this line, but I don't know what to replace it with.
sc "Ah, Tan, you got a moment? New girl here, gotta get your approval through the system. Ibuki, yeah. Alright, alright, thank you." #tan = xandre tan = mayo
"Beep. He puts away his phone and gets back to tapping away."
sc "There we go. You're in the system now, everything is squared away."
i "Thank you. Anything else I should know?"
sc "Your room number is forty-two of the cruiser building. You're sharing with Suzuya and Kumano. Clerk in the building should hand you the key there."
i "Got it."
sc "Other than that, no. The system doesn't really like me right now, so I wasn't able to get your platoon. Though, that means you'll be able to choose!"
i "Oh, sweet."
sc "Though, Ooyodo will probably call you up and assign you one if you manage to break the system like that."
i "I'll try not to break it then."
sc "Anyways, you're free to go. Get yourself accustomed to the place, this'll be one hell of a ride."
i "I'll be seeing you, then."
sc "You too."
scene hallway
"I get up and head into the hallway. I wonder where should I head out first?"
"I can check out my room, and meet the two people the admiral was talking about."
"But I've heard the harbor has a nice view. Probably would be nice this time of year. It'd be also nice to check out where I'd work." #note: it should be may-ish
"Or, I could visit the shipyards. I'd be there often as well, probably could meet some other people there too."
menu: #BUCKLE UP, BUCKAROO. THE RIDE TRULY BEGINS HERE.
    "Where to go?"
    "My room.": #act 1, option 1
        jump a1_b1_room
    "The harbor.": #act 1, option 2
        jump a1_b2_harbor
    "The shipyards.": #act 1, option 3
        jump a1_b3_shipyards

return
