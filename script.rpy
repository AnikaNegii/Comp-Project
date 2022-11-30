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

    play sound "audio/alarm.wav"

    # ----MC wake up----
    "Ngh..."
    " " "J-Just... five more minutes..."
    " " ". . ."

    play sound "audio/alarm.wav"

    " " ". . ."
    " " "Agh..."
    " " "Huh...?"
    " " "! ! !"
    " " "The time! Oh damn it, I'm gonna be late!"


    # ----Mc leaves school for the first day, running to school----
    scene street 
    
    " " "I can't believe I'm gonna be late on the first day of school..! Day one and I'm already making a poor impression."
    " " "...I really need to hurry."
    " " ". . ."


    # ----Mc sees Sukeban in an alley on the way to school----
    " " ". . ."
    " " "! ?"
    " " "Someone's yelling? Bruh, this early in the morning? Y'all, it's like 7 am, calm down."
    " " "Is this what city mornings are always like?"

    play sound "audio/punch.mp3"

    "Delinquent" "You bastard! What do you think you're doing?"
    " " "-Huh?"
    "Delinquent" "Thought you could get away with that, huh, Ahmed?"
    "Andy" "N-No.. I don't even know who you are! Or Ahmed! Who are you?! Who's Ahmed???? What's happening???????"
    "Andy" "I'm Andy!"
    "Delinquent" "Don't play with me right now, I know who you are!"

    play sound "audio/punch.mp3"

    scene tsubaki_intro

    "Delinquent" "Hah? What do you think you're looking at!?"
    " " "Me?"
    "Delinquent" "Yeah, I'm talking to you. Why don't you mind your own business?"
    menu:
        "Try to Help Him":
            " " "Hey! What are you doing? Let go of him!"
            "Delinquent" "Who are you to tell me what to do? You don't even know what's going on, get out of here!"
            " " "She steps forward menacingly."
            " " "Okay, okay! I was just about to leave, sheesh."
            "Andy" "No... Don't leave me here!"
            "Andy" "W-Wait, lady, calm down!"
            
        "Leave Him":
            " " "Okay, okay! I was just about to leave, sheesh."
            "Andy" "No... Don't leave me here!"
            "Andy" "W-Wait, lady, calm down!"

    play sound "audio/punch.mp3"

    " " ". . ."


    # ----Continue walking----
    scene street

    " " "Is this what it's always like? City life is crazy, damn."
    " " "So delinquents like that exist in real life too, huh? I guess things like the yakuza and mafia do exist in real life."
    " " "I can't let these things distract me though. I'm gonna be late..!"


    # ----Arriving at school----
    scene outside_school

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


    # ----Mc sees ojou chan coming out of a limo----
    scene chaerri_intro

    "Butler" "We've arrived, my lady."
    "Rich Girl" "Oh, thank you."
    "Boy A" "Bro, AND she's polite too! Lady Rose is the best!"
    " " "...Lady Rose? ...The Rose of the school? These guys say 'rose' a little too much... Is this some kind of city slang I don't understand?"
    " " "And what's with the red carpet...?"
    " " "Bro, I just wanna get to school. Why is so much happening?"
    " " "Agh, class is starting in a minute, I'm actually gonna be late. Where is this class?"


    # ----Mc introduces themselves at school----
    " " "Damn it, I'm late to class... What was the classroom number again? M2-208? God, who built this school, it's actually a maze."
    " " "!"
    " " "Oh, I think it's here."

    scene classroom
    
    "Guregu Sensei" "Okay, class, so we can all agree that the succesor of 0 is 1, and therefor-"
    " " "Ah... Excuse me, is this the computer science seminar?"
    "Guregu Sensei" "Oh, looks like we have a new face today! You must be..."
    "Guregu Sensei" "Uh..."
    "Guregu Sensei" "Why don't you introduce yourself to the class?"
    
    $ MC = renpy.input("My name is...")

    $ MC = MC.strip()

    if MC == "":
        $ player_name="Joe Mama"
        
    "Guregu Sensei" "Okay, I'll be lenient since it's only your first day here, but please make sure to come on time in the future. Why don't you have a seat for now?"
    "Guregu Sensei" "Now, class, lets talk about the square root of 2-"

        # door opens sound

    show t_happytalkblood

    "Delinquent" "Yo, teach, I'm here! I made sure to come in this month."

    " " ". . !"
    " " "That..."
    " " "Isn't she the delinquent girl from the alleyway this morning?! She's in my class?"

    hide t_happytalkblood

    "Guregu Sensei" "What? Are you trolling me right now?"
    "Guregu Sensei" "This is a learning environment, and we all need to be here for everyone to learn."
    "Guregu Sensei" "Please sit down, and I'll be continuing the lesson."
    "Guregu Sensei" "So, class-"
    " " ". . ."
    " " ". . ."
    " " ". . ."
    
    

    # ----Free period time to pick who to talk to (Only one option)----
        # show "Free Period" text

    $ c_points = 0
    $ t_points = 0

    " " "Free period, huh? It's still only my first day so there isn't really any work to do... Maybe I'll just watch Youtube?"
    " " "Hmm..."
    " " "Glancing around the classroom, you suddenly notice something."
    " " ". . !"
    
    show c_neutral

    " " "That's the rich girl from this morning!"
    " " "I don't really get it but she's the 'Rose of the school,' or something like that, isn't she? She even had a whole limo and red carpet for her this morning..."
    " " "Not only that crazy delinquent, but someone like her is in my class too?"

    hide c_neutral

    " " "How come all these eccentric people are in my class? Is this normal in the city? The city is really an unusual place, huh."
    " " "Maybe I'll talk with one of them. Neither of them seem too busy either..."
    
    show c_neutral
    
    " " "The rich girl is studying by herself, but there are many eyes admiring her from a distance. She's focusing on her work, but I'm curious about this morning."
    
    hide c_neutral
    show t_neutralblood
    
    " " "The delinquent is pouting by herself at her desk. She's wiping off her bat. She seemed scary this morning, but she seems to have calmed down. Should I ask her about this morning?"

    menu:
        "Rich Girl":
            $ c_points += 1
            show c_neutral
            m "Hey."
            "Rich Girl" "O-oh! ...C-Carpet lady...?"
            hide c_neutral

        "Delinquent":
            $ t_points += 1
            " " "I really, really want to know what was going on this morning..."
            " " "She seemed pretty dangerous earlier, but we're in school now. Surely she wouldn't be bold enough to do anything here, in front of everyone?"
            " " "She didn't seem to care about a random passerby like me seeing, though..."
            " " ". . ."
            " " "Yeah, I should probably still be careful."
            show t_neutral
            m "H-Hello. You're the girl from this morning, aren't you? ...The one in the alleyway?"
            " " "What am I saying right now? This delinquent just finished wiping blood off her bat in front of me and now I'm asking about her crimes..."
            " " "I'm curious. I'm definitely really curious about what happened, but asking that out of nowhere is-!"
            show t_angrytalk
            "Delinquent" "Huh? Who are you? Interrupting my cleaning out of nowhere..."
            " " "...She's already angry."
            m "A-Ah, sorry. You don't remember me? You got all mad at me for looking into the alleyway. You were really mad at that Ahmed guy for some reason."
            " " "Ah, now I'm recounting her anger towards me? I'm kind of just asking for her to smash my head in at this point, aren't I?"
            show t_angry
            "Delinquent" ""

    # -----Mc internal monolouge, he finds out he had cleaning duty with both of them----
    " " "After Class"
    " " "Class is finally over..."
    " " "Since I joined in the middle of the year, there's still so much content I need to catch up on."
    "Guregu Sensei" "Oh, excuse me,"
    
    # Mc meets both of them during cleaning duty
    # internal thoughts about cleaning with the two girls
    
    show c_neutral at left
    show t_neutral at right

    if c_points == 1:
        t "Name's Tsubaki."
    if t_points == 1:
        c "Oh, I'm Chaerii."

    
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
    show c_neutral at right
    show t_neutral at left





  
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
