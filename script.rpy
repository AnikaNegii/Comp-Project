transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ timer_range = 5
    $ timer_jump = 5


define t = Character("Tsubaki")
define c = Character("Chaerii")
define m = Character("[MC]")
define n = Character("", kind=nvl, what_italic=True, what_color="#ffffff",  ctc="ctc_blink", ctc_position="nestled")


label start:
    # ----MC intro----
    n "16 years. I've lived in Osaka for all my life until now. I'm going to miss my hometown and my friends. It'll definitely feel weird waking up in a different room everyday."
    n "...But I shouldn't think too much about that. Focus on the positives! Dad finally got the big promotion he was hoping for, and he's never been happier."
    n "The city seems scary and I'm worried about adapting to city life... But I'll try my best."

        # alarm rings

    # ----MC wake up----
    " " "Ngh..."
    " " "J-Just... five more minutes..."
    " " ". . ."

        # alarm rings again

    " " ". . ."
    " " "Agh..."
    " " "Huh...?"
    " " "!!!"
    " " "The time! Oh damn it, I'm gonna be late!"

    # ----Mc leaves school for the first day, running to school----
    " " "I can't believe I'm gonna be late on the first day of school..! Day one and I'm already making a poor impression."
    " " "...I really need to hurry."
    " " ". . ."

    # ----Mc sees Sukeban in an alley on the way to school----
    " " ". . ."
    " " "! ?"
    " " "Someone's yelling? Bruh, this early in the morning? Y'all, it's like 7 am, calm down."
    " " "Is this what city mornings are always like?"

        # insert thud sound

    t "You bastard! What do you think you're doing?"
    " " "--Huh?"
    t "Thought you could get away with that, huh, Ahmed?"
    "Andy" "N-No.. I don't even know who you are! Or Ahmed! Who are you?! Who's Ahmed???? What's happening???????"
    "Andy" "I'm Andy!"
    t "Don't play with me right now, I know who you are!"

        # insert thud sound

        # tsubaki first cg

    t "Hah? What do you think you're looking at!?"
    m "Me?"
    t "Yeah, I'm talking to you. Why don't you mind your own business?"
    m "Okay, okay! I was just about to leave, sheesh."
    "Andy" "No... Don't leave me here!"
    "Andy" "W-Wait, lady, calm down!"

        # insert thud sound

    # ----Continue walking----
        # insert street png
    " " "Is this what it's always like? City life is crazy, damn."
    " " "So delinquents like that exist in real life too, huh? I guess things like the yakuza and mafia do exist in real life."
    " " "I can't let these things distract me though. I'm gonna be late..!"

    # ----Arriving at school----
        # insert school png
    " " "...I made it! Barely on time, though, and I still need to get to class..."
    " " "What was my first class again...? Something about a seminar?"
    " " ". . ."

    "Boy A" "Guys, look! She's coming, she's coming!"
    "Boy A" "The Rose of our school!"
    "Boy B" "Dude, didn't you have a crush on The Rose since like elementary school?"
    "Boy A" "Of course, man! Who wouldn't have a crush on The Rose? I still do!"
    "Boy A" "The Rose's the top of our grade and she hasn't missed a single day of school! She's kind and beautiful too! A true 10/10 woman."
    "Boy B" "Bro, what."

    " " "? ?"
    " " "...Is that a limo pulling up to the school?"

    # Mc sees ojou chan coming out of a limo
        # chaerii first cg
    "Butler" "We've arrived, my lady."
    c "Oh, thank you."
    "Boy A" "Bro, AND she's polite too! Lady Rose is the best!"
    " " "...Lady Rose? ...The Rose of the school? These guys say 'rose' a little too much... Is this some kind of city slang I don't understand?"
    " " "And what's with the red carpet...?"
    " " "Bro, I just wanna get to school. Why is so much happening?"
    " " "Agh, class is starting in a minute, I'm actually gonna be late. Where is this class?"

    # Mc introduces themselves at school
    " " "Damn it, I'm late to class... What was classroom number again? M2-208? God who built this school it's actually a maze."
    scene classroom
    
    "Guregu Sensei" "Ok Class so we can all agree that the succesor of 0 is 1, and therefor-
    "m" "Ah.. excuse me, is this the computer science seminar?"
    "Guregu Sensei "Oh looks like we have a new face today! You must be..."
    "Guregu Sensei" "Uh.............................................................................................."
    "Guregu Sensei" "Why don't you introduce your self to the class?"
    
    $ MC = renpy.input("My name is...")

    $ MC = MC.strip()

    if MC == "":
        $ player_name="Joe Mama"
        
    "???" "What kinda bozo name is that? L "
    "Guregu Sensei" "Ok why don't you have a seat..."
    "Guregu Sensei" "Now class lets talk about the square root of 2"
    
    
    

    # Free period time to pick who to talk to (Only one option)
    $ c_points = 0
    $ t_points = 0

    menu:

        "Rich Girl":
            $ c_points += 1
            show c
            m "omg the carpet lady from this morning"
            c "O-oh! ...C-Carpet lady...?"

        "Delinquent":
            $ t_points += 1
            show t
            m "I saw you this morning..."
            t "Tch!"

    # Mc internal monolouge, he finds out he had cleaning duty with both of them
    m "blahblahblah"
    
    # Mc meets both of them during cleaning duty
    show c at left
    show t at right
    
    c "Moew meow meow meoew meowejwemwoekwoewei"
    t "Barksabalr bark bakr barck barkijefwiefj"

    c "(╥ω╥)"
    t "┌∩┐(◣_◢)┌∩┐"

    m "Damn, who am I gonna go after"

    # Mc picks 


    $ time = 2.5
    $ timer_range = 2.5
    $ timer_jump = 'menu1_slow'
    show screen countdown

    menu:

        "Rich Girl":
            hide screen countdown
            $ c_points += 1
            show c
            m "Daijoubu!!! ^^"
            c " 0////0 "

        "Delinquent":
            hide screen countdown
            $ t_points += 1
            show t
            m "Whats wrong bby girl"
            t "Hmph!"
    
    # Every one meets up in the class room
    show c at right
    show t at left





  
# ______________________________________________________________________________________________________
    # s "Heheheheheheheheeheh"
    # s "blahblahblahblah"
    # m "Jajajajaajaj"

    # show n at right

    # jump timed
    # n "Omg are you cheating on me??!?!?!!?"
    # n "Prove your love by a test!"
    # n "what do you like more milfs or difls"

    # $ sans_points = 0
    # $ nagito_points = 0

    # menu:

    #     "I like mommy dommys":
    #         $ sans_points += 1
    #         s "Yooooo same fr"

    #     "I like daddy waddy":
    #         $ nagito_points += 1
    #         n "Factual"


    # n "Ok 2nd question"
    # n "WHats your favorite icecream?"

    # menu:

    #     "vanilla":
    #         $ sans_points += 1
    #         "Yeah going vanilla is best"

    #     "Chocolate":
    #         $ nagito_points += 1
    #         "POg"

    # s "Ok last question... who do you like the most"

    # menu:

    #     "sans":
    #         $ sans_points += 1
    #         "Yes Bby girl same"

    #     "nagito":
    #         $ nagito_points += 1
    #         "I knew you always loved me UWU!!!"

    # n "Now its time to see whose heart you won!!"

    # if sans_points == 3:
    #     scene epic:
    #         xzoom 0.5 yzoom 0.5
    #     show s
    #     "Yessss queen lets get married in the underground periodt!"

    # else:
    #     scene bruh:
    #         xzoom 0.5 yzoom 0.5
    #     show n
    #     "Purrrrr its giving children fr"

    # label timed:

    #     n "Bruh moment"
    #     $ time = 2.5
    #     $ timer_range = 2.5
    #     $ timer_jump = 'menu1_slow'
    #     show screen countdown
    #     menu:
    #         "Choice 1":
    #             hide screen countdown
    #             e "You chose 'Choice 1'"
    #             jump menu1_end
    #         "Choice 2":
    #             hide screen countdown
    #             e "You chose 'Choice 2'"
    #             jump menu1_end
    
    # label menu1_slow:
    #     n "You didn't choose anything."
        
    # label menu1_end:
    #     n "Anyway, let's do something else."

    # return
