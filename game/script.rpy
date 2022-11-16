# I'm sorry

define r = Character("Rune")
define m = Character("Morten")
define n = Character("Noah")
define k = Character("Kristiyan")

default points = 0
default morten = False
default noah = False
default kristiyan = False
default rune = False

label splashscreen:

    $ renpy.movie_cutscene('op.webm')

    return

label before_main_menu:

    play music "music/menu.ogg" noloop

    return

label start:

    scene b mcd
    
    play music "music/out.ogg"

    show r happy

    voice "voice/1.wav"
    r "Welcome to McDonald's!"

    show r shy

    voice "voice/2.wav"
    r "Ah, you must be our new worker... "

    voice "voice/3.wav"    
    r "Uhh, what was your name again?"

    $ p = renpy.input("(Enter your name)")

    $ p = p.strip()

    if p == "":

        $ p = "Yunus"

    show r happy

    voice "voice/4.wav"
    r "Ah, %(p)s, That's right."

    voice "voice/5.wav"
    r "Nice to meet you, I am Rune the brune, the manager of this fine place."

    voice "voice/6.wav"
    p "Nice to meet you too."

    voice "voice/7.wav"
    r "Come this way, I'll introduce you to the kitchen."

label part1:

    scene b kitchen

    play music "music/bgm.ogg"

    show r neutral

    voice "voice/8.wav"
    r "Everyone, let me introduce you to our new worker, %(p)s."

    hide r neutral
    show k neutral

    voice "voice/9.wav"
    k "Yo."

    hide k neutral
    show n neutral

    voice "voice/10.wav"
    n "Sup."

    hide n neutral
    show m neutral

    voice "voice/11.wav"
    m "Hello."

    hide m neutral

    voice "voice/12.wav"
    p "Nice to meet you guys."

    show r neutral

    voice "voice/13.wav"
    r "Today you'll be working on either making burgers, fries or nuggets."

    voice "voice/14.wav"
    r "For now, let's start with fries. Morten will introduce you to the job."

    scene b fries

    play music "music/morten.ogg"

    show m happy

    voice "voice/15.wav"
    m "Hey, I'm Morten."

    show m neutral

    voice "voice/16.wav"
    m "I'll start off by turning on the machine..."

    "*Machine turning on*"

    voice "voice/17.wav"
    m "The machine is on."

    p "......"

    voice "voice/18.wav"
    m "Now you just wait for the oil to boil."

    voice "voice/19.wav"
    p "Okay"

    p "......"

    voice "voice/20.wav"
    m "It is important to set the temperature to 169 degrees."

    voice "voice/21.wav"
    m "You got that?"

    voice "voice/22.wav"
    p "Yeah."

    voice "voice/23.wav"
    m "Now that the oil is boiling, go ahead and put the fries in."

    voice "voice/24.wav"
    p "Okay..."

    "*Fries are being fried ig?*"

    show m smile

    voice "voice/25.wav"
    m "Okay, they should be done now."

    voice "voice/26.wav"
    m "Now you just grab the thingy and throw the fries in the other thingy."

    voice "voice/27.wav"
    m "Then with this thingy you put the special sauce on top in a spiral gesture."

    voice "voice/28.wav"
    m "Then you mix it up and it's done."

    voice "voice/29.wav"
    p "Okay..."

    voice "voice/30.wav"
    m "You use this to pick up the fries and put them in the package. Then leave them here."

    voice "voice/31.wav"
    p "Got it."

    show m happy

    voice "voice/32.wav"
    m "Good, now you try,"

    hide m happy

    "Okay, first thing first..."

    "I need to set the temperature to..."

    menu p1:

        "10C":
            
            jump p1choice1

        "169C":

            jump p1choice2

        "420C":

            jump p1choice3

label p1choice1:

    "You set the temperature to 10C"

    "Then after some time, you take the fries out of the oil."

    show m food n
    
    voice "voice/33.wav"
    m "WHAT THE FUCK IS THIS SHIT?"

    voice "voice/34.wav"
    m "THE FRIES ARE UNDERCOOKED!"

    voice "voice/35.wav"
    p "I'm sorry..."

    show m mad

    voice "voice/36.wav"
    m "I can't believe this."

    voice "voice/37.wav"
    m "You better not fuck this up again."

    hide m mad

    "You got a strike, 3 strikes and you're out"

    jump part2

label p1choice2:

    "You set the temperature to 169C"

    "Then after some time, you take the fries out of the oil."

    show m food y

    voice "voice/38.wav"
    m "Whoa, these fries look so crisp and tasty."

    voice "voice/39.wav"
    m "Good job, you're good at this 'mcdonalds' thing"

    voice "voice/40.wav"
    p "Thank you."

    show m happy

    voice "voice/41.wav"
    m "By the way, just so you know, between you and me..."

    show m shy

    voice "voice/42.wav"
    m "You're cute."

    voice "voice/43.wav"
    p "What?"

    show m happy

    voice "voice/44.wav"
    m "I said that my favourite food is fries. With more fries."

    "I must've misheard."

    voice "voice/45.wav"
    p "Okay, good to know."

    $ points += 1
    $ morten = True

    jump part2

label p1choice3:
        
    "You set the temperature to 420C"

    "Then after some time, you take the fries out of the oil."

    show m food n

    voice "voice/46.wav"
    m "WHAT THE ABSOLUTE FUCK??"

    voice "voice/47.wav"
    m "The fries are all black."

    voice "voice/48.wav"
    p "There's nothing wrong about being bla-"

    show m mad

    voice "voice/49.wav"
    m "Are you shitting me? They are overcooked."

    voice "voice/50.wav"
    m "I was expecting better."

    voice "voice/51.wav"
    p "I'm sorry."
    
    voice "voice/52.wav"
    m "I can't believe this."

    voice "voice/53.wav"
    m "You better not fuck this up again."

    hide m mad

    "You got a strike, 3 strikes and you're out"

    jump part2

label part2:

    scene b kitchen

    play music "music/bgm.ogg"

    "After finishing the fries, you get assigned to burgers."

    show n happy

    voice "voice/54.wav"
    n "Yo, I'm Noah, but you can call me #1GhostFan"

    voice "voice/55.wav"
    p "I'll stick with Noah."

    show n neutral

    voice "voice/56.wav"
    n "Listen up, we gonna make burgers, alright?"

    voice "voice/57.wav"
    n "Burgers are very delicate. They feed people. That's it."

    voice "voice/58.wav"
    p "Yeah..."

    voice "voice/59.wav"
    n "Alrightm that's enough chatting around. Let's get to it, halla halla."

    scene b burgers

    play music "music/noah.ogg"

    show n smile

    voice "voice/60.wav"
    n "Alright, it's pretty simple. You just take two buns from here, and put it on the table."

    voice "voice/61.wav"
    n "Then depending on the burger you put this and that, tatata, some ketchup..."

    show n shy
    
    voice "voice/62.wav"
    n "We can't use *that* ingredient during November..."

    show n smile

    voice "voice/63.wav"
    n "Cheese, patty, salad, and..."

    voice "voice/64.wav"
    n "Done, you got yourself a big mac."

    voice "voice/65.wav"
    p "That was fast."

    show n mad

    voice "voice/66.wav"
    n "You gotta be fast to be good, kid."

    voice "voice/67.wav"
    p "Okay..."

    show n smile

    voice "voice/68.wav"
    n "But remember all the ingredients! If you miss one, it won't be legendary!"

    voice "voice/69.wav"
    p "Alright."

    voice "voice/70.wav"
    n "Go ahead and give it a try."

    hide n smile

    "You start making the burger, you put this and that, tatata, ketchup..."

    "Cheese, patty and..."

    "And..."

    menu p2:

        "Zaza":
            
            jump p2choice1

        "Salad":

            jump p2choice3

        "Cum":

            jump p2choice2

label p2choice1:

    "You put in Zaza inside."

    show n food n

    voice "voice/71.wav"
    p "Wait, what?"

    voice "voice/72.wav"
    n "What the fuck?"

    show n sad

    voice "voice/73.wav"
    p "Uh..."

    voice "voice/74.wav"
    p "Zaza."

    show n happy

    voice "voice/75.wav"
    n "Zaza."

    voice "voice/76.wav"
    p "Zzzazzza."

    voice "voice/77.wav"
    n "Zazazazaza."

    voice "voice/78.wav"
    p "Zazzzzza."

    voice "voice/79.wav"
    n "Zaaaazaaaa."
     
    hide n happy

    "You got a strike, 3 strikes and you're out"

    jump part3

label p2choice2:

    "You take off your pants and start-"

    show n food n

    voice "voice/80.wav"
    n "WAIT WAIT WAIT!"

    show n mad

    voice "voice/81.wav"
    n "I told you dude, we can't use that ingredient during November."

    show n smile

    voice "voice/82.wav"
    n "Otherwise that's fine."

    voice "voice/83.wav"
    p "Oh, okay..."

    hide n smile

    "You got a strike, 3 strikes and you're out"

    jump part3

label p2choice3:

    "You put in the salad."

    show n food y

    "Overall the burger turns out pretty good."

    voice "voice/84.wav"
    n "Oh my god you're so sexy."

    voice "voice/85.wav"
    p "What?"

    show n shy

    voice "voice/86.wav"
    n "I said the burger is so sexy."

    show n smile

    voice "voice/87.wav"
    n "I love burgers, my favourite food is burgers."

    voice "voice/88.wav"
    n "Big macs, the bigger, the better."

    $ points += 1
    $ noah = True

    jump part3

label part3:

    scene b kitchen

    play music "music/bgm.ogg"

    "After working on burgers, the final job today is nuggets"

    show k happy

    voice "voice/89.wav"
    k "Sup, I'm Kristiyan the closet weeb."

    show k shy

    voice "voice/90.wav"
    k "(By the way, just between you and me, I am a discord admin.)"

    show k sad

    voice "voice/91.wav"
    k "I'll be helping you with the nuggets. Even tho I'm kinda vegetarian, oh well..."

    show k neutral

    voice "voice/92.wav"
    k "You already know how to make fries, right?"

    voice "voice/93.wav"
    k "Well they're made mostly the same way."

    voice "voice/94.wav"
    k "The person who designed the game is dumb in the head and fucked up this part, so whatever."

    voice "voice/95.wav"
    p "Oh..."

    scene b fries

    play music "music/kristiyan.ogg"

    show k neutral

    voice "voice/96.wav"
    k "Uhh just don't fuck up the temperature, which should be exactly......"

    voice "voice/97.wav"
    k "100C."

    voice "voice/98.wav"
    p "Okay, that's easy to remember."

    voice "voice/99.wav"
    k "So uhh you do this and this."

    voice "voice/100.wav"
    k "I'm sorry if this is kinda rushed, it's late and I'm bored writing all this text."
    
    voice "voice/101.wav"
    p "Wow, another breaking of the 4th wall."

    show k smile

    voice "voice/102.wav"
    k "Got all that?"

    voice "voice/103.wav"
    k "Cool."

    voice "voice/104.wav"
    k "You go ahead."

    voice "voice/105.wav"
    p "Uhh sure..."

    hide k smile

    "You start making the nuggets."

    "But oh no! What was the temperature supposed to be??"

    menu p3:

        "99":
            
            jump p3choice1

        "100":

            jump p3choice2

        "101":

            jump p3choice3

label p3choice1:

    "You make the nuggets, they turn out pretty good."

    "Kristiyan goes by and has a taste test (even tho he's vegetarian)..."

    show k food n

    voice "voice/106.wav"
    k "WHAT THE FUCK!"

    voice "voice/107.wav"
    k "These are shit, the absolute shittiest shit shit I've ever put in my mouth."

    voice "voice/108.wav"
    p "But they taste good..."

    show k mad
    
    voice "voice/109.wav"
    k "I can feel they're a bit undercooked."

    voice "voice/110.wav"
    k "Hmm..."

    voice "voice/111.wav"
    k "One degree off..."

    voice "voice/112.wav"
    p "I'm sorry."

    show k sad

    voice "voice/113.wav"
    k "You dissappoint me son."

    hide k sad

    "You got a strike, 3 strikes and you're out"

    jump part4

label p3choice2:

    "You make the nuggets, they turn out pretty good."

    "Kristiyan goes by and has a taste test (even tho he's vegetarian)..."

    show k food y

    voice "voice/114.wav"
    k "MMMMMMMM."

    voice "voice/115.wav"
    k "These taste soo goooood~"

    voice "voice/116.wav"
    k "Ahhh~"

    show k happy
    
    voice "voice/117.wav"
    k "You did good, I commend you son."

    show k shy

    voice "voice/118.wav"
    k "You know, I would't mind kissing you right here."

    voice "voice/119.wav"
    p "What?"

    show k smile

    voice "voice/120.wav"
    k "I said that my favourite food is chilli cheese tops."

    voice "voice/121.wav"
    k "They're made the same way as nuggets. (I think)"

    voice "voice/122.wav"
    p "Good to know."

    $ points += 1
    $ kristiyan = True

    jump part4


label p3choice3:

    "You make the nuggets, they turn out pretty good."

    "Kristiyan goes by and has a taste test (even tho he's vegetarian)..."

    show k food n

    voice "voice/123.wav"
    k "WHAT THE FUCK!"

    voice "voice/124.wav"
    k "These are shit, the absolute shittiest shit shit I've ever put in my mouth."

    voice "voice/125.wav"
    p "But they taste good..."

    show k mad
    
    voice "voice/126.wav"
    k "I can feel they're a bit overcooked."

    voice "voice/127.wav"
    k "Hmm..."

    voice "voice/128.wav"
    k "One degree off..."

    voice "voice/129.wav"
    p "I'm sorry."

    show k sad

    voice "voice/130.wav"
    k "You dissappoint me son."

    hide k sad

    "You got a strike, 3 strikes and you're out"

    jump part4

label part4:

    scene b kitchen

    play music "music/bgm.ogg"

    "The day is finally over."

    show r neutral

    "The dear leader, Rune (manager), has gathered you all."

    voice "voice/131.wav"
    r "Now, to announce how our new worker %(p)s did today..."

    if points == 3:

        show r happy

        voice "voice/132.wav"
        r "%(p)s did AMAZINGLY!!!"
        
        voice "voice/133.wav"
        r "You are our best employee."

        show r shy

        voice "voice/134.wav"
        r "To be frank, I love you."

        voice "voice/135.wav"
        p "What?"

        show r happy

        voice "voice/136.wav"
        r "Uh, I said my fav food is all of the guys' fav food combined."

        voice "voice/137.wav"
        r "I spend 15000kr at McDonald's every month, because I get one of everything."

        voice "voice/138.wav"
        r "Because I love McDonald's!!!"

        hide r happy
        show n mad

        voice "voice/139.wav"
        n "LEGEND!"

        hide n mad
        show k happy

        voice "voice/140.wav"
        k "Rune is the true McD legend."

        hide k happy
        show m smile

        voice "voice/141.wav"
        m "That's why he's our manager."

        hide m smile
        show r happy

        voice "voice/142.wav"
        r "Now, as a reward for the good work, feel free to make whatever you want."

        hide r happy

        $ rune = True

        jump p5

    elif points == 2:
    
        show r happy

        voice "voice/143.wav"
        r "%(p)s did good."

        show r neutral

        voice "voice/144.wav"
        r "Bit rough around the edges, but not bad."

        hide r neutral
        show k smile

        voice "voice/145.wav"
        k "Yey!"

        hide k smile
        show m smile

        voice "voice/146.wav"
        m "Woo!"

        hide m smile
        show n smile

        voice "voice/147.wav"
        n "Goated!"

        hide n smile
        show r neutral

        voice "voice/148.wav"
        r "Now, as a reward for the good work, feel free to make whatever you want."

        hide r neutral

        jump p5

    elif points == 1:

        show r mad

        voice "voice/149.wav"
        r "%(p)s did bad."

        hide r mad
        show k sad
        
        voice "voice/150.wav"
        k "Smh."

        hide k sad
        show n shy

        voice "voice/151.wav"
        n "Lol."

        hide n shy
        show m sad

        voice "voice/152.wav"
        m "Bruh."

        hide m sad
        show r neutral

        voice "voice/153.wav"
        r "Now, as a reward for the good work, feel free to make whatever you want."

        hide r neutral

        jump p5

    elif points == 0:

        show r mad

        voice "voice/154.wav"
        r "%(p)s did TERRIBLE!"

        voice "voice/155.wav"
        r "THE ABSOLUTE WORST!"

        show r sad

        voice "voice/156.wav"
        r "I can't believe I managed a bad employee like them."

        hide r sad
        show m sad

        voice "voice/157.wav"
        m "Disgusting."

        hide m sad
        show k sad

        voice "voice/158.wav"
        k "How unfortunate."

        hide k sad
        show n sad

        voice "voice/159.wav"
        n "lol hest"

        hide n sad
        show r mad

        voice "voice/160.wav"
        r "You..."

        voice "voice/161.wav"
        r "Are..."

        voice "voice/162.wav"
        r "FIRED!!!"

        hide r mad

        scene black

        play music "music/mads.ogg"

        pause(5)

        show mads with Dissolve(10)

        voice "voice/163.wav"
        "Mads" "You dissappoint me child."

        return

label part5:

    "Now you can choose what to make (or who to make it for wink wink)"

    menu p5:

        "Fries (lots and lots of fries)" if morten:

            play music "music/morten.ogg"

            show m smile
            
            voice "voice/164.wav"
            m "For me?"

            voice "voice/165.wav"
            p "Yes."

            show m food y

            voice "voice/166.wav"
            m "Oh my god you're so kind!"

            show m shy
            
            voice "voice/167.wav"
            m "I love that side of you!"

            voice "voice/168.wav"
            m "No..."

            show m happy

            voice "voice/169.wav"
            m "I LOVE YOU!"

            voice "voice/170.wav"
            p "OH ME TOO!"

            voice "voice/171.wav"
            m "LET'S GET MARRIED!"

            voice "voice/172.wav"
            p "YES!"

            hide m happy

            "And so, %(p)s and Morten lived happily ever after."

            jump credits

        "Big mac (biggest mac evaaa)" if noah:

            play music "music/noah.ogg"

            show n smile

            voice "voice/173.wav"
            n "Whoa, that's the biggest mac evaaa!"

            voice "voice/174.wav"
            p "I thought you'd like it."

            show n food y

            voice "voice/175.wav"
            n "GOATED!"

            show n happy

            voice "voice/176.wav"
            n "You are a true legend."

            voice "voice/177.wav"
            n "My legend."

            voice "voice/178.wav"
            p "You are my legend too."

            show n shy

            voice "voice/179.wav"
            n "Hey..."

            voice "voice/180.wav"
            n "You wanna... share this burger?"
            
            voice "voice/181.wav"
            p "Thanks."

            show n shy

            voice "voice/182.wav"
            n "Oh no, I don't mean this burger..."

            voice "voice/183.wav"
            p "Oh. Oooooh..."

            voice "voice/184.wav"
            p "Ohohohoho..."

            voice "voice/185.wav"
            n "Ehehehehe..."

            hide n shy

            "And so, %(p)s and Noah lived happily ever after."

            jump credits

        "(EXTRA) Chilli cheese tops" if kristiyan:

            play music "music/kristiyan.ogg"

            show k happy

            voice "voice/186.wav"
            k "Whoa, are these for me?"

            voice "voice/187.wav"
            k "Thanks, yo."

            show k food y

            voice "voice/189.wav"
            k "I love how chilli they are."

            voice "voice/190.wav"
            p "Ah, you're getting kinda hot..."

            show k shy

            voice "voice/191.wav"
            k "You're hot too."

            voice "voice/192.wav"
            p "I don't mean like- wait, really?"

            show k happy

            voice "voice/193.wav"
            k "Yeah. Totally."

            voice "voice/194.wav"
            p "T-T-Then... Do you want to..."

            show k shy

            voice "voice/195.wav"
            k "Fuck your brains? Totally."

            hide k shy

            "And so, %(p)s and Kristiyan lived happily ever after."

            jump credits

        "EVERYTHING" if rune:

            play music "music/rune.ogg"

            show r shy

            voice "voice/196.wav"
            r "No way..."

            hide r shy
            show k neutral

            voice "voice/197.wav"
            k "They's making... Everything... At once..."

            hide k neutral
            show n smile

            voice "voice/198.wav"
            n "What a legend..."

            hide n smile
            show m shy

            voice "voice/199.wav"
            m "They's so skilled..."

            hide m shy

            "You make everything McDonald's has to offer and give it to Rune."

            show r happy

            voice "voice/200.wav"
            r "Oh my god thanks."

            show r food a

            voice "voice/201.wav"
            r "Nom nom nom nom nom"

            "And he eats everything in under 5 minutes."

            show r happy

            voice "voice/202.wav"
            r "I didn't expect you'd make everything, you are one in a kind."

            voice "voice/203.wav"
            r "To be honest, I wish you'd cook for me every day!"

            voice "voice/204.wav"
            p "We can make this work out."

            hide r happy
            show n shy

            voice "voice/205.wav"
            n "You know he's a legend, right?"

            hide n shy
            show r shy

            voice "voice/206.wav"
            p "Yes. But every legend needs a legend."

            voice "voice/207.wav"
            p "I'll be his legend."

            "And then you look each other in the eyes."

            scene black

            "In the span of 13 minutes, you share a passionate kiss."

            show m sad

            voice "voice/208.wav"
            m "..."

            hide m sad
            show k sad

            voice "voice/209.wav"
            k "I'm going home."

            hide k sad
            show n smile

            voice "voice/210.wav"
            n "Same!"

            hide n smile

            "This is the best kiss you've ever had."

            "It tasted like McDonald's, but that's what you'd expect..."

            "From a McDonald's legend."

            jump credits

label credits:

    play music "music/credits.ogg" noloop

    $ ui.pausebehavior(10)

    image white = "#fff"
    scene white with Dissolve(20)

    show credits at top
    pause(.1)
    show credits at center with MoveTransition(117)

    return