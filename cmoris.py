from os import system
import random

cmoristxt = [ "Better start coding for android mike.",
 "Almost an exact copy of iPhone 6",
 "Debating whether or not to move 25% of my shares to microsoft",
 "Ahead of the mobile launches and iPhone 6 disaster",
 "Their market share is abysmal",
 "Pretty soon WP will overtake iPhone outside USA",
 "Or google will just eat it all up",
 "I feel like iPhone 3 and 4 were amazing",
 "2 and 5 are like... Okay rly?",
 "I think 6 will be like, uhhhhmmm what?",
 "Lets be honest. They followed up Palm V in color",
 "The screen sizes on iPhone are basically unusable",
 "Its like meant for a 14 yr old girl",
 "IPhone is the only phone that consistently has cracked screens",
 "I do not even have a clue how the fuck I could crack a screen besides a sledgehammer tbh",
 "Ill probably get an iPhone 6 As a burner. Maybe work phone or something",
 "I have not realized it since 2006. Considering nothings changed besides the leather calendar, what makes you think ill change my mind now",
 "Normal iPhone user",
 "It has ONE button... ONE",
 "And with that one button you can do everything",
 "IOS8 is a gamechanger",
 "The surface 2 is undeniably better hardware than the iPad air",
 "B T W Is it me or does the I watch look thick as fuck like iPhone 1",
 "IPhone 6 competitor. Window phone 4.7 from Yezz Billy. Take that Steve!",
 "Why would you buy an iphone",
 "Worst ui ever",
 "I would buy an iPhone if I could install windows phone on it. Cept I wouldnt because $845 is a RIDICULOUS price for that",
 "Wtf are you on crack? You can buy a surface pro 3 for less than that",
 "I would buy a mac book and do the dual boot thing tho. That makes sense",
 "Cept id just get a surface pro 3 again in that case since its better software and better hardware",
 "Plus you could claim innocence back then. The alternatives are so much better now though... ",
 "The biggest change is they got rid of the leather calendar. Its still a grid of dumb fucking buttons",
 "A grid of fucking buttons",
 "At least google lets you customize shit",
 "Irs a grid of buttons you can not customize",
 "Let me go get some Symbian brb",
 "Palm V order up"]

line = random.choice(cmoristxt);
print(line)
system('say ' + line)
