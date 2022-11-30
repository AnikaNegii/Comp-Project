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


init python:
    def m_text(event, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/m_text.mp3")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def f_text(event, **kwargs):
        if event == "show_done":
                renpy.sound.play("audio/f_text.mp3")
        elif event == "slow_done" or event == "end":
                renpy.sound.stop()

image ctc_blink:
    "ctc.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

image ctc_blink_1:
    "ctc_1.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat


define t = Character("Tsubaki", callback = m_text, color = "#698a3f", ctc="ctc_blink", ctc_position="nestled")
define c = Character("Chaerii", callback = f_text, color = "#8a3f3f", ctc="ctc_blink", ctc_position="nestled")

define t1 = Character("Delinquent", callback = m_text, color = "#698a3f", ctc="ctc_blink_1", ctc_position="nestled")

define m = Character("[MC]", callback = m_text, color = "#ffffff", ctc="ctc_blink_1", ctc_position="nestled")
define me = Character("Me", callback = m_text, color = "#ffffff", ctc="ctc_blink_1", ctc_position="nestled")
define n = Character("", kind=nvl, callback = m_text, what_italic=True, what_color="#ffffff",  ctc="ctc_blink", ctc_position="nestled")
define i = Character(" ", callback = m_text, color = "#698a3f", ctc="ctc_blink_1", ctc_position="nestled")

label start:
    # ----MC intro----
    n "16 years. I've lived in Osaka for all my life until now. {w=0.5} I'm going to miss my hometown and my friends... not that I had any. {w=0.5} At least, it'll definitely feel weird waking up in a different room everyday."
    n "But honestly, the country life wasn't for me anyways... It's impossible to find any good merch in those run down corner shops and getting anything deilvered was a nightmare!"
    n "...But I shouldn't think too much about that.{w=0.5} Afterall, Mom finally got that promotion she was hoping for, and we made the big move to Tokyo."
    n "Well... City life, here I come!"

    play sound "audio/alarm.mp3"

    # ----MC wake up----
    i "Ngh..."
    i "J-Just... five more minutes..."
    i ". . ."

    play sound "audio/alarm.mp3"

    scene bedroom
    with Dissolve(2)

    scene black
    with dissolve

    scene bedroom
    with Dissolve(1)

    scene black
    with dissolve

    " " "What time is it?"

    scene bedroom
    with Dissolve(1)


    
    i "6:00 AM..."
    i "God, my head... I stayed up too late last night playing Leauge."
    i "Ahh, right... School. Damn."
    i "I'd better turn off the alarm clock. {w=0.5} It's only making my headache worse."

    i "{i}Preparing for the day you get ready.{/i}"
    i "{i}You walk into the living room to see no one there.{/i}"
    scene living_room with dissolve
    i "{i}As you prepare a quick breakfast you see a sticky note on the fridge.{/i}"

    nvl clear
    n "Good morning, Pumpkin!"
    n "I'm sorry I won't be able to see you off for your first day of school,{w=0.5} but I made you lunch!"
    n "It's your favorite, so make sure to not waste any of it. Especially since your darling, amazing, and most awesome mother made it!"
    n " - Your Beloved Mommy"

    i "I-"
    i "Damn it, I'm not a pre-schooler."

    i "{i}Your mother has always been a hardworking and strong willed person, and as a business woman she's always been busy.{/i}"
    i "{i}Her hopes for you have always been to have a carefree and fun life, but you know it's because she doesn't want you to live like her.{/i}"
    i "{i}And while you do have fun, you have no intention of becoming a worthless person, and so to support your mother you've made it into the top ranking high school in Japan.{/i}"
    i "{i}Lucky for you, it was also in Tokyo.{/i}"

    i "..."
    i "{i}You take your first step outside the door.{/i}"
    i "..."
    i "Ahhh... I just realized I have no idea how to get to school."


    # ----Mc leaves school for the first day, running to school----
    scene street with dissolve
    i "{i}After what seems like 15 minutes, you realize you are most definitely lost.{/i}"
    i "{i}Looking around, you notice that you've somehow ended up in a very shady part of Tokyo.{/i}"
    play sound "audio/punch.mp3"
    i "!?"
    me "Is someone there? I think I may be lost? I'm trying to find t-"
    play sound "audio/punch.mp3"
    i "{i}As you turn the corner you see quite the scene.{/i}"

    # ----Mc sees Sukeban in an alley on the way to school----
    t1 "You bastard! What do you think you're doing?"
    t1 "-Huh?"
    t1 "Thought you could get away with that, huh, Ahmed?"
    "Andy" "N-No.. I don't even know who you are! Or Ahmed! Who are you?! Who's Ahmed???? What's happening??????"
    "Andy" "I'm Andy!"
    t1 "Don't play with me right now, I know who you are!"

    me "Bruh, this early in the morning? It's like 7 AM, calm down."

    scene tsubaki_intro with dissolve
    t1 "Hah? What did you say!?"
    i "{i}Ah. Did I say that out loud?{/i}"
    i "{i}Dude, I knew this was a dark alley way, but why is there actually an abyss behind her...{/i}"

    t1 "Mind your own business, ok?!"
    me "Hey, you go to the same school as me, right?"
    t1 "..."
    me "I was wondering if you knew the directions?"
    t1 "Tch. I was wondering if you were bold or just dumb. Just use a GPS, idiot."
    i "Oh."
    me "Smart... Thanks."

    i "{i}You start to walk away as you put the address into Google Maps.{/i}"
    "Andy" "WAIT! Don't just leave me here!"

    menu:
        "Try to Help Him":
            me "Yo, as I said before we go to the same school. It starts in 30 minutes so if you don't want to be late then I suggest you get going."
            t1 "Who are you to tell me what to do? And I suggest YOU get going before I beat you up too."
            i "She steps forward menacingly."
            me "Okay, okay! I was just letting you know, sheesh."
            "Andy" "No... Don't leave me here!"
            me "Sorry man, I tried."
            "Andy" "W-Wait, lady, calm down!"
            
        "Leave Him":
            me "..."
            "Andy" "No... Don't leave me here!"
            me "Sorry man, it's not really my problem. I'm not looking for any fights either."
            "Andy" "W-Wait, lady, calm down!"

    play sound "audio/punch.mp3"


    # ----Continue walking----
    scene street with dissolve

    i "Is this what it's always like? City life is crazy, damn."
    i "So delinquents like that exist in real life too, huh? I guess things like the mafia and thugs do exist in real life."
    i "And I thought I was just playing too much Yakuza and watching a lot of Tokyo Revengers..."


    # ----Arriving at school----
    scene outside_school

    i "Hm... so this is Top Elite High School, huh?"
    i "It's not that bad."
    i "What was my first class again...? Something about a seminar?"
    i "..."
    i "Why is there huge crowd around the gate?"


    "Boy A" "Guys, look! She's coming, she's coming!"
    "Boy A" "The Rose of our school!"
    "Boy B" "Dude, didn't you have a crush on The Rose since like elementary school?"
    "Boy A" "Of course, man! Who wouldn't have a crush on The Rose? I still do!"
    "Boy A" "The Rose's the top of our grade and she hasn't missed a single day of school! She's kind and beautiful too! A true 10/10 woman."
    "Boy B" "Bro, what."

    i "???"
    i "...Is that a limo pulling up to the school?"


    # ----Mc sees ojou chan coming out of a limo----
    scene chaerri_intro

    "Butler" "We've arrived, my lady."
    "Rich Girl" "Oh, thank you."
    "Boy A" "Bro, AND she's polite too! Lady Rose is the best!"
    i "...Lady Rose? ...The Rose of the school? These guys say 'rose' a little too much... Tt's getting on my nerves."
    i "Aint no way..."
    i "Is that a red carpet. 'Skull emoji'"
    i "I just wanna get to school. Why is so much happening?"
    i "Class is starting in a minute, I'm actually gonna be late. Where is this class?"

    scene black with dissolve
    # ----Mc introduces themselves at school----
    " " "Damn it, I'm late to class... What was the classroom number again? M2-208? God, who built this school, it's actually a maze."
    " " "!"
    " " "Oh, I think it's here."

    scene classroom with dissolve
    
    "Guregu Sensei" "Okay, class, so we can all agree that the succesor of 0 is 1, and therefor-"
    " " "Ah... Excuse me, is this the computer science seminar?"
    "Guregu Sensei" "Oh, looks like we have a new face today! You must be..."
    "Guregu Sensei" "Uh..."
    "Guregu Sensei" "Why don't you introduce yourself to the class?"
    
    $ MC = renpy.input("My name is...")

    $ MC = MC.strip()

    if MC == "":
        $ player_name="Joe Mama"
        
    i "{i}As you stand up before the class you noticed that the room is filled with unique characters. {/i}"
    i "{i}The most noticable being 'The Rose' from before.{/i}"
    i "{i}You can already tell today is going to be a struggle...{/i}"

    "Guregu Sensei" "Okay, I'll be lenient since it's only your first day here, but please make sure to come on time in the future. Why don't you have a seat for now?"
    "Guregu Sensei" "Now, class, lets talk about the square root of 2-"

        # door opens sound

    show t_happytalkblood

    t1 "Yo, teach, I'm here! I made sure to come in this month."

    hide t_happytalkblood

    i "Ahhh... just great."
    "Guregu Sensei" "What? Are you trolling me right now?"
    "Guregu Sensei" "Unlike the new student, you should already know your way around the school, so I expect you to be here on time."
    "Guregu Sensei" "This is a learning environment, and we all need to be here for everyone to learn."
    "Guregu Sensei" "Please sit down, and I'll be continuing the lesson."
    "Guregu Sensei" "So, class-"

    scene black with dissolve
    i ". . ."
    i ". . ."
    i ". . ."
    
    

    # ----Free period time to pick who to talk to (Only one option)----
        # show "Free Period" text

    $ c_points = 0
    $ t_points = 0

    scene classroom with dissolve

    i "Free period, huh? It's still only my first day but I have so much work to do..."
    i "Hmm..."
    i "{i}You take a look around the room to see what the social structure of the class is like.{/i}"
    i "{i}The first thing you see is a crowd of people surrounding 'The Rose'. Everyone seems to be entranced by her. {/i}"
    i "{i}While you thought she'd be arrogant and sobbish, she seems to be getting along with everyone.{/i}"

    show t_neutralblood with dissolve
    i "{i}As you noticed before, the delinquent has blood smeared on her face and bat trying to wipe it off.{/i}"
    i "{i}That poor NPC who got beat up... {/i}"

    show t_confused with dissolve
    t1 "You got a crush on me or something? You keep staring."
    m "I'm staring 'cause you're bringing around a goofy ahh bat everywhere."

    show t_irritatedtalk with dissolve
    t1 "Huh? What did you say, punk?"

    i "{i}As she swings her bat to point at me, a bit of blood from the bat flys off.{/i}"

    "Girl 1" "GASP!!!"
    "Boys 1" "YOU DARE GET YOUR FILTY BLOOD ON 'THE ROSE', TSUBAKI?!?!11"
    c "..."


    t "Tch. If Ms. Little Princess can't handle a little blood, then that's not my problem."
    c "It's... It's okay everyone..."
    "Girl 2" "B-but, Lady Ro-"

    c "I'll be back...  I'm just going to the restroom to clean up a bit."
    t "Pathetic... Chaerii..."

    i "{i}As The Rose left, you begin to feel tention in the air. {/i}"

    "Girl 3" "Ugh, she's always like this."
    "Boy 2" "I know, honestly, it would be better if Tsubaki just didn't show up at all."
    "Boy 1" "After all she did, and she's still going after Rose."

    i "{i}You could hardly call this eavesdropping, they were talking so loud. {/i}"

    menu:
        "Mind Your Business":
            i "bruh"
          
        "Eavesdrop":
            i "BRUH"

        "Leave the Classroom":
            i "Bruh"
      


    
    show c_neutral

    m "That's the rich girl from this morning! Not only that crazy delinquent, but she's in my class too?"

    hide c_neutral

    m "Are all the weirdos in my class? Is this normal in the city? The city is really an exciting place, huh!"
    m "Maybe I'll talk with one of them. Neither of them seem too busy either..."
    
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
            m "I really want to know what was going on this morning..."
            m "She seems kind of dangerous, but we're in school now. Surely she wouldn't be bold enough to do anything here, in front of everyone?"
            m "She didn't seem to care about a random passerby like me seeing, though..."
            m ". . ."
            m "Yeah, I should still be careful."
            show t_neutral
            m ""
            hide t_neutral

    # Mc internal monolouge, he finds out he had cleaning duty with both of them
    m "blahblahblah"
    
    # Mc meets both of them during cleaning duty
    show c_neutral at left
    show t_neutral at right
    
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
