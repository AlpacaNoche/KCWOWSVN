# Character definitions plus some other thingies.

define i = Character("Ibuki")
define sm = Character("Smol Man") #scoots before introduction to ibuki
define smk = Character("Sleeping Man") #kosena before introduction to Ibuki

define sc = Character("Scoots")
define dm = Character("Daishomaru")
define bi = Character("Bike")
define mm = Character("Monkey Looking Guy")#mayo before introduction
define mb = Character("Maya_Bae")
define usn = Character("USN Guy") #unknown before introduction, kinda mixed on the label tho
define un = Character("LT Unknown")

define ks = Character("Kosena")
define ap = Character("Alpaca")
define smi = Character("Small Girl and Ibuki") #used for when Ibuki and Alpaca slam into each other.
define sg = Character("Small Girl") #used for Alpaca prior to introduction
define ab = Character("Aobaka")
define bhg = Character("Blue Haired Girl")#used for Suzuya prior to introduction
define brg = Character("Brown Haired Girl")#used for Kumano prior to introduction
define shg = Character("Short Haired Girl")#used for Mogami prior to introduction
define ku = Character("Kumano")
define sz = Character("Suzuya")
define mg = Character("Mogami")
define mk = Character("Mikuma")
define g1 = Character("Girl 1")#used for Atago in baseline_1
define g2 = Character("Girl 2")#used for Ashigara in baseline_1

define tm = Character("Tall Man")#used for wororg before introduction
define wg = Character("Wororg")
define sa = Character("Saxon")
define as = Character("Astraph")

default scootsPoint = False
default scPrefix = "Admiral"
default aobaInvest = False
default unknownPoints = 0
default mayoPoint = False
default woggyYes = False

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
sm "I'm Captain Scoots. I manage the tech side of things around here."
menu:
    "How should I respond?"
    "Tech? What do you work on?":
        $ scootsPoint = True
        i "That sounds cool, what technology do you work on?"
        sc "Oh, I just manage the information and other communications around the base."
        sc "You're a shipgirl right? I can get you registered into the system."
        i "Thank you."
    "Neat.":
        i "Neat."
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
"A few more minutes pass by without much going on."
sc "Heavy cruiser, right. Charlie, alpha, oh-"
"Scoots' phone starts buzzing. He picks it up and answers the call."
sc "Wait one, Ibuki. Hey, Tan. You get the approval request? Good. We got a new shipgirl here, Ibuki."
sc "Alright, thank you. Back to where I was at."
"Beep. He puts away his phone and gets back to tapping away."
sc "There we go. You're in the system now, everything is squared away."
i "Thank you. Anything else I should know?"
sc "Your room number is one-six of the cruiser building. You'll be sharing with carr-, wait, cruiser division seven. Cru-div-seven."
sc "Clerk in the building should hand you the key there."
i "Got it. 16."
sc "Other than that, no. The system doesn't really like me right now, so I wasn't able to get your squadron. Though, that means you'll be able to choose!"
i "Oh, sweet."
sc "Though, Ooyodo will probably call you up and assign you one if you manage to break the system like that."
i "I'll try not to break it then."
sc "Anyways, you're free to go. Get yourself accustomed to the place, this'll be one hell of a ride. Welcome to Wagyu."

if scootsPoint:
    i "Thank you, uh, Admiral."
    sc "I'm a captain, not an admiral. Army, too."
    $ scPrefix = "Captain"
    i "Ah, I see. Wait, what is an army officer doing at a naval base?"
    sc "Hell if I know. Maybe they needed a signal officer?"
    "As if this base was already not making any sense."
i "I'll be seeing you, then."

if scootsPoint:
    sc "Hooah, you too."
    "What..? I'll just get going." #dunno if I should include this bit Kapp
else:
    sc "You too."

scene hallway
"I get up and head into the hallway. Probably should check out the room and get my things sorted in there."

"..."
"Wait, where exactly is the dormitories?"

"I turn around and yell over to the [scPrefix]."
i "HEEEY! SCOOOTS! DO YOU KNOW WHERE THE WAY TO THE DORMS IS?"
"He quickly runs over to me, and points down the hallway."
sc "First left. Take the second right and the exit should be down the hallway. Building is first on the left."
sc "If you need anything else, I'll be in my office."
"Scoots then turns right back around and dashes back into his office. I yell a 'thank you' back to him and continue on my way." #bit mixed on this line

scene dorm building
"After a bit, I make it there. It seems to be somewhat quie-"
"Suddenly, a gorilla-like roar sounds from inside."
i "What the hell?"
"This base is already crazy enough it seems like-- can it get any worse?"
"I still decide to head inside, hopefully I won't bump into whatever {i}that{/i} was."

scene dorm frontdesk
"Wait, is there any clerk here like Scoots mentioned?"
"With second glance throughout the room, I actually spot the clerk.."#I'm debating on keeping this part or not, with Kosena sleeping. Might not match his character.
show kosena sleepy
with easeinbottom

"...except he's passed out on the desk."
smk "..mm...paint thinnerrr...."
"What?"
i "Uh, hello?"
hide kosena sleepy
show kosena surprised

smk "..oh! Ah, hello!"
"A quick look at his nametag tells me his name-- Kosena. Weird."
hide kosena surprised
show kosena
i "Hi, I'm the newest ship posted here, Ibuki."
ks "Ibuki-san? Alright, give me a moment."

"He quickly goes to typing on his computer on the desk, before shifting around in its drawer. He then pulls out a key, and hands me it."
ks "Here you go. Room one-six, it's on the second floor, A wing."
i "Thank you, make sure to grab some more sleep tonight."
"Kosena blushes in embarassment before returning to a straight face."
ks "Alright, alright. Ring me up if you need anything sorted out related to your room."

"I quickly go up the flight of stairs to my right."
scene dorm hallway
"Hm, wing A, right? Should be right ther-"
#insert slamming noise
scene blank
smi "AH!"
scene alpaca trippedover
"It appears that I have slammed into a small woman." #this line is like half of a joke
smi "I am so sorry, that was my fault.."
"She scrambles to grab the papers she dropped everywhere."

menu: #Alpaca choice #1
    "What should I do?"
    "Help her out.":
        jump alpaca_route_1
    "Keep moving.":
        jump baseline_1

return
