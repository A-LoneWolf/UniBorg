"""COMMAND : `.runs` , `.metoo` , `.rape` , `.insult` , `.pro` , `.maaki` , `.gey`, `.abuse` , `.abusehin`
Other emoticons commands
`.abusewaving`, `.abusewtf`, `.abuselove`, `.abuseconfused`, `.abusedead`, `.abusesad`, `.abusedog`
`.abuse` <any word>

"""

from telethon import events
import random, re
from uniborg.util import admin_cmd

METOOSTR = [
    "`Me too thanks`",
    "`Haha yes, me too`",
    "`Same lol`",
    "`Me irl`",
    "`Same here`",
    "`Haha yes`",
    "`Same pinch bsdk`",
]
RUNSREACTS = [
    "`Runs to Thanos`",
    "`Runs to Modiji For Achey Din`",
    "`Runs far, far away from earth`",
    "`Running faster than usian bolt coz I'mma Bot`",
    "`Runs to Marie`",
    "`This Group is too cancerous to deal with.`",
    "`Cya bois`",
    "`I am a mad person. Plox Ban me.`",
    "`I go away`",
    "`I am just walking off, coz me is too fat.`",
    "`I Fugged off!`",
]
RAPE_STRINGS = [
     "`Rape Done Drink The Cum`",
     "`The user has been successfully raped`",
     "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari`",
     "`Relax your Rear, ders nothing to fear,The Rape train is finally here`",
     "`Rape coming... Raped! haha 😆`",
     "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
] 
ABUSE_STRINGS = [
       "`Madharchod`",
	   "`Gaandu`",
	   "`Chutiya he rah jaye ga`",
	   "`Ja be Gaandu`",
	   "`Ma ka Bhodsa madharchod`",
	   "`mml`",
	   "`You MotherFukcer`",
           "`You Betichod`",
           "`you are lodu no.1`"
	   "`Muh Me Lega Bhosdike ?`"
]
GEY_STRINGS = [
     "`you gey bsdk`",
     "`you gey`",
     "`you gey in the house`",
     "`you chakka`",
     "`you gey gey gey gey gey gey gey gey`",
     "`you gey go away`",
]
PRO_STRINGS = [
     "`This gey is pro as phack.`",
     "`Pros here -_- Time to Leave`",
]
INSULT_STRINGS = [ 
    "`Owww ... Such a stupid idiot.`",
    "`BC.. Gaand na fulao, maa chod denge tumhari`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 544 section 9 prevents me from replying to stupid humans like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",
]
# ===========================================
                          

@borg.on(admin_cmd("runs ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd("metoo ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(METOOSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = METOOSTR[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd("rape ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RAPE_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RAPE_STRINGS[bro]
    await event.edit(reply_text)
			  
                          
@borg.on(admin_cmd("insult ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(INSULT_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = INSULT_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("pro ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(PRO_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = PRO_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("maaki ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(ABUSE_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = ABUSE_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("gey ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(GEY_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = GEY_STRINGS[bro]
    await event.edit(reply_text)



@borg.on(events.NewMessage(pattern=r"\.abuse(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "hin":
        emoticons = [
            "Maderchod- MOTHERFUCKER",
            "Bhosadike-BORN FROM A ROTTEN PUSSY",
            "Bhen chod-Sister fucker",
            "Bhadhava- Pimp",
            "Bhadhava- Pimp",
            "Chodu- Fucker",
            "Chutiya- Fucker, bastard",
            "Gaand- ASS",
            "Gaandu-Asshole",
"Gadha, Bakland- Idiot",
"Lauda, Lund- Penis, dick, cock",
"Hijra- Gay, Transsexual",
"Kuttiya- Bitch",
"Paad- FART",
"Randi- HOOKER",
"Saala kutta- Bloody dog",
"Saali kutti- Bloody bitch",
"Tatti- Shit",
"Kamina- bastard",
"Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
"Chut ke dhakkan- Pussy lid",
"Chut ke gulam- Pussy whipped",
"Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
"Choot marani ka- Pussy whipped",
"Choot ka baal- Hair of vagina",
"Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
"Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
"Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
"Chipkali ke chut ke pasine- Sweat of reptiles cunt",
"Chipkali ki bhigi chut- Wet pussy of a wall lizard",
"Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
"Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
"Cuntmama- Vaginal uncle",
"Chhed- Vagina,Hole",
"Apni gaand mein muthi daal- Put your fist up your ass",
"Apni lund choos- Go and suck your own dick",
"Apni ma ko ja choos- Go suck your mom",
"Bhen ke laude- Sister’s dick",
"Bhen ke takke: Go and suck your sister’s balls",
"Abla naari tera buble bhaari-  woman, your tits are huge",
"Bhonsri-Waalaa- You fucker",
"Bhadwe ka awlat- Son of a pimp",
"Bhains ki aulad- Son of a buffalo",
"Buddha Khoosat- Old fart",
"Bol teri gand kaise maru- let me know how to fuck you in the ass",
"Bur ki chatani- Ketchup of cunt",
"Chunni- Clit",
"Chinaal- Whore",
"Chudai khana- Whore house",
"Chudan chuda- Fucking games",
"Chut ka pujari- pussy worshipper",
"Chut ka bhoot- Vaginal Ghost",
"Gaand ka makhan- Butter from the ass",
"Gaand main lassan- Garlic in ass",
"Gaand main danda- Stick in ass",
"Gaand main keera- Bug up your ass",
"Gaand mein bambu- A bambooup your ass",
"Gaandfat- Busted ass",
"Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
"Hazaar lund teri gaand main-Thousand dicks in your ass",
"Jhat ke baal- Pubic hair",
"Jhaant ke pissu- Bug of pubic hair",
"Kadak Mall- Sexy Girl",
"Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
"Khotey ki aulda- Son of donkey",
"Kutte ka awlat- Son of a dog",
"Kutte ki jat- Breed of dog",
"Kutte ke tatte- Dog’s balls",
"Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
"Lavde ke bal- Hair on your penis",
"muh mei lele: Suck my dick",
"Lund Chus: Suck dick",
"Lund Ke Pasine- Sweat of dick",
"Meri Gand Ka Khatmal: Bug of my Ass",
"Moot, Mootna- Piss off",
"Najayaz paidaish- Illegitimately born",
"Randi khana- whore house",
"Sadi hui gaand- Stinking ass",
"Teri gaand main kute ka lund- A dog’s dick in your ass",
"Teri maa ka bhosda- Your mother’s breasts",
"Teri maa ki chut- Your mother’s pussy",
"Tere gaand mein keede paday- May worms infest your ass-hole",
"Ullu ke pathe- Idiot",
        ]
    
    elif input_str in "waving":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "love":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confused":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:    
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀ Ĺ̯▀   )",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)
