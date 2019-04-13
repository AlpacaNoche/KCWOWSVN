label baseline_1:
scene dorm hallway
"I keep moving forward. It's her problem, not mine."
"After a bit more time, I finally arrive to my dorm."
scene dorm door
"16, he said."
"Well... this is it."
"I gently open the door."

scene crudiv7room
show suzuya
with easeinbottom
show kumano
with easeinbottom

"Two girls, both sitting at a table. They look like they were talking but their gaze is on me now.."#not feelin this line
i "Hello-"
"Before I can continue my sentence, one's already jumped up and right next to me."
bhg "Ooh, ooh, new girl! I haven't seen you around here."
brg "Oh, I thought it was Mogamin and Mikuma."

"The other girl seems much more... calm. Are they sisters?"
i "I-I'm Ibuki. I was just posted here. I was told I'd be with cruiser division 7?"
bhg "You're in the right place then! I'm Suzuya!"
"She steps back for a moment and extends her hand for a shake. I accept."
brg "And I'm Kumano. Welcome to the Wagyu Naval Base."
i "Thank you both."

"Kumano waves me over to the table, offering a seat at another cushion."
"Suzuya quickly returns to her seat. I lay my backpack next to the table and join them."
ku "So, how are you liking the base so far?"
i "It's... alright. I'm sure everyone here is nice, though."
sz "Sounds good! I bet you'll find this place lovely!"
"I look around the room. There's four other doors, all with their own names. I wonder who they belong to?"
i "Are there more people in this cruiser division?"
sz "Yep! Mogami and Mikuma are out right now."
ku "They should be training with their squadron at the moment. I think they'll be back soon."
i "I see."

ku "Have you met any of our admirals yet?"
sz "Most of them are cool, though Flat is {i}mine.{/i}"
i "I've only met [scPrefix] Scoots, though that one woman I ran into earlier didn't seem like a shipgirl."
i "Oh, and I've heard what who I've been told is Daisho."
ku "There are plenty more, maybe you'll find one you like. Who have you been assigned to?"
i "I actually haven't been assigned to any unit yet. The [scPrefix] said that the system wasn't working."
ku "That's weird... You can hang with us for the time being if need be."
sz "Ufu, Akashi and Yuubari are going to have a field day."

#thinking about putting more dialogue here, but for now I'll just hop straight to Mogamin's & Mikuma's arrival.

"Just as Suzuya finishes her sentences, the door starts fidgeting, like someone is unlocking it." #change Suzuya to whoever finishes the previous sentence
ku "That must be Mogamin and Mikuma."
"The door flies open, revealing two other girls. Both are wearing matching uniforms."
shg "HEEEEEEeeey!..?"
shg "Oh, who's this?"#owo
"I get up and bow, introducing myself."
i "I'm Ibuki, I was just stationed here."
shg "Well then, I'm Mogami. And this here is Mikuma."
"Mikuma pops out from her side and says a little 'hi'. The two move over to the table and sit down."
mk "Wait, you just arrived here? Shouldn't you be with your ship class?"
mg "Yeah, I don't remember an Ibuki within the Mogami class..."
i "I'm actually the only one in my class... I was told by [scPrefix] Scoots that I'd be with CruDiv 7 for the time being."

mg "I don't think we have any more rooms in here... But you can have mine! I'll just bunk with Kumarinko from now on."
mk "Waitwaitwaitwai-"
mg "There's not much stuff in my room so it should be fine!"
"I doubt Mikuma is consenting to this."
mk "We don't even have actual bunks! How are we supposed to do that?"
mg "I can always pull up a sleeping bag. Or, you know~"
sz "We can always just ask Yuubari, Akashi, or Ooyodo for a bunkbed in your room."
mk "But-but.."
mg "We gotta be nice to the newface, alright?"
mk "Fiiiine."
mg "There we go! I'll get my stuff moved over really quickly."
"She quickly runs off into her room. There's a lot of crashing noises and other various worrying sounds coming from it."
i "Is she okay in there?"
mk "Mogamin's a bit clumsy, but I think she's fine."
"Moments later Mogami exits her room, albeit with a bunch of scratches. She still stands strong, backpack in tow."
mg "Alright, I'm good now! Ibuki, you're good to move in now. Now, if you excuse me-"
"She quickly runs into Mikuma's room, only for Mikuma to chase right behind her."
i "I guess I'll take my leave now."

"I get up to check out the room, but as I do, some yelling reverberates through the door."
i "Who was that?"
ku "Must be some other cruisers. Certain classes don't mix well with others."
menu:
    "Should I check the commotion or go back to setting up my room?"
    "Check out the argument.":
        $ aobaInvest = True
        jump aobaka_route_1
    "Go back to unpacking.":
        i "Ah, I see."
"Who would've thought that this base still has its arguments?"
"Doesn't seem too bad from what I've seen."
"Suzuya and Kumano go back to their previous conversation as I head over to my new room."
scene dorm room empty
"Welp, time to get to business."
return
