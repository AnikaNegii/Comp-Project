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
    # MC wakes up
    n "16 years. I've lived in Osaka for all my life until now. I'm going to miss my hometown and my friends. It'll definitely feel weird waking up in a different room everyday."
    n "...But I shouldn't think too much about that. Focus on the positives! Dad finally got the big promotion he was hoping for, and he's never been happier."
    n "The city seems scary and I'm worried about adapting to city life... But I'll try my best."
 
    # alarm rings
 
    # MC wake up scene
    " " "Ngh..."
    " " "J-Just... five more minutes..."
    " " ". . ."
 
    # alarm rings again
 
    " " ". . ."
    " " "Agh..."
    " " "Huh...?"
    " " "!!!"
    " " "The time! Oh damn it, I'm gonna be late!"
 
    # Mc leaves school for the first day, running to school
    " " "I can't believe I'm gonna be late on the first day of school..! Day one and I'm already making a poor impression."
    " " "...I really need to hurry."
    " " ". . ."
 
    # Mc sees Sukeban in an alley on the way to school
    " " ". . ."
    " " "! ?"
    " " ""
 
 
    # Mc sees ojou chan coming out of a limo
    " " "Damn, Who's that rich chick?"
 
    # Mc introduces themselves at school
    scene classroom
 
    $ MC = renpy.input("My name is...")
 
    $ MC = MC.strip()
 
    if MC == "":
        $ player_name="Joe Mama"
 
    # Free period time to pick who to talk to (Only one option)
    $ c_points = 0
    $ t_points = 0
 
    menu:
 
        "Rich Girl":
            $ c_points += 1
            show c
            m "Are you rich or something?"
            c "O-oh!"
 
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
 

