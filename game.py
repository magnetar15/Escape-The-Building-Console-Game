import time
import sys
import random


# Project: Escape from the building
# You are trapped in a building
# To escape, you must explore the rooms, solve riddles, and discover the code for the exit door.
# - Present the story and the objective of the game at the beginning.

# The program must:

# - Allow players to choose which room to explore. The game must have at least four different rooms.
# - Include at least three clues to help players discover the door code. The clues must not reveal the code directly.
# - Include at least three riddles. Correct answers must provide clues or grant access to a room.
# - Allow players to try again after entering a wrong answer. After three wrong answers to the same riddle, the game ends with a defeat message.
# - Check the final code when the player tries to open the door. The correct code leads to victory; a wrong code uses up one attempt.
# - Respond clearly to invalid choices or answers without automatically counting them as wrong riddle answers.
# - Announce at the end whether the player escaped or lost, and offer the option to start a new game.
# You choose the story, objects, clues, riddles, and code, but all the clues must make it possible to discover the code. When you send me the complete program, I will evaluate it and give you a grade without deducting points for things that have not been taught.


CODE = random.randint(1000,9999)
CODE = str(CODE)

tries_left = 3

def intro():
    print("...")
    time.sleep(0.7)
    print("You open your eyes and see a man standing nearby.")
    time.sleep(0.7)
    print("He looks at you and asks:\n\n")
    while True:
        name = input("Daniel: What's your name, thief? ").strip().capitalize()
        if name == "":
            print("Have you lost your voice, thief? Answer me...")
            continue
        elif len(name) < 3:
            print("Stop lying, thief. Your name can't be that short.")
            continue
        elif name.isalpha() == False:
            print("Have you lost your mind, thief? I asked for your name!")
            continue
        else:
            print("Daniel: All right,", name)
            break
    time.sleep(0.7)
    print(name + ":", "Who are you, and why am I here?")
    time.sleep(0.5)
    print("\n Daniel: You don't remember?")
    time.sleep(0.7)
    print(name + ":", "I remember playing a video game where I was trying to rob someone.")
    time.sleep(0.5)
    print("....")
    time.sleep(0.7)
    print(name + ":", "Then something hit me on the head... and now I'm here...")
    time.sleep(0.6)
    print("Daniel: Now it makes sense. They must have drugged you.")
    time.sleep(0.5)
    print("Daniel: I was about to kill you.")
    time.sleep(0.7)
    print(name + ":", "But why?")
    time.sleep(0.7)
    print("Daniel: You robbed me!")
    time.sleep(0.3)
    print("Daniel: There was no video game.")
    time.sleep(0.5)
    print("Daniel: I was minding my own business when you suddenly took my bag.")
    time.sleep(0.5)
    print("Daniel: Then I started chasing you.")
    time.sleep(0.8)
    print(name + ":", "That makes no sense... I'm a good person.")
    time.sleep(0.3)
    print(name + ":", "I would never do that.")
    time.sleep(0.8)
    print(".....")
    print("Daniel: They must have drugged you with angel's trumpet.")
    time.sleep(0.5)
    print("Daniel: But that doesn't matter right now... we're stuck.")
    time.sleep(0.5)
    print(name + ":", "Where are we?")
    time.sleep(0.5)
    print("Daniel: After you stole my bag, I chased you, and you ran into this building.")
    time.sleep(0.5)
    print("Daniel: As soon as I got inside, someone closed the door behind me.")
    time.sleep(0.7)
    print(
        "Daniel: We're stuck here. There's a keypad on the door, but I can't figure out the code.")
    time.sleep(0.7)
    print("Daniel: I've been trying for 15 minutes with no luck.")
    time.sleep(0.7)
    print(name + ":", "Maybe the people who drugged me locked us in here...")
    time.sleep(0.5)
    print(name + ":", "Let me try to call for help on my phone.")
    time.sleep(0.8)
    print("Daniel: There's no point. There's no signal.")
    time.sleep(0.5)
    print(name + ":", "I'll try to figure something out.")
    time.sleep(0.5)
    print("Daniel: All right,, if you find out a way, wake me up.. i'll sleep for a bit.")
    time.sleep(0.5)
    print(name + ":", "Okay...")
    time.sleep(2)
    print("You explore the building. There are four rooms, a restroom, and a hallway.")
    print("Find a way out.")
    return(name)

def wake_daniel1(code):
    global tries_left
    print(name + ":", "Wake up, Daniel!")
    time.sleep(0.7)
    print(name + ":", "I found the code!")
    time.sleep(0.7)
    print("Daniel: ...")
    time.sleep(0.7)
    print("Daniel: Amazing! Tell me the code. Let's get out of here.")
    time.sleep(0.7)
    print(name + ":", code)
    time.sleep(0.7)
    print("Daniel walks to the door and enters the code.")
    if code == CODE:
        tries_left -= 1
        print("Daniel: You got it right! This is the code! We're saved.")
        time.sleep(0.5)
        print("The door opens...")
        return(True, 0)
    else:
        tries_left -= 1
        print("Daniel: This code isn't working!")
        time.sleep(0.7)
        print("Daniel: I'll go back to sleep.")
        time.sleep(0.7)
        print("Daniel: I'm already angry because I'm here because of you...")
        time.sleep(0.7)
        print("Daniel: If you wake me up again and the code doesn't work, you'll be in trouble.")
        return (False, 0)

def wake_daniel2(code):
    global tries_left
    print(name + ":", "Wake up, Daniel!")
    time.sleep(0.7)
    print(name + ":", "I found the code! - This time the right one")
    time.sleep(0.7)
    print("Daniel: It had better be the right one this time...")
    if code == CODE:
        tries_left -= 1
        print("Daniel: Good news, it's the right code.")
        time.sleep(0.7)
        print("Daniel: Let's get out of here.")
        print("The door opens...")
        return(True, 0)
    else:
        tries_left -= 1
        print("Daniel: This code is not the right one !")
        time.sleep(0.7)
        print("Daniel: I'm tired. I'm angry.")
        time.sleep(0.7)
        print("Daniel: You keep waking me up for no reason...")
        time.sleep(0.7)
        print("Daniel: If you wake me up again for no reason, you're dead.")
        return (False, 0)

def wake_daniel3(code):
    global tries_left
    print(name + ":", "Daniel! Wake up!")
    time.sleep(0.7)
    print(name + ":", "Try this code.")
    time.sleep(0.7)
    print("Daniel: I swear to God, if this isn't the right one, you're dead.")
    if code == CODE:
        tries_left -= 1
        print("Daniel: It's the right code.")
        time.sleep(0.7)
        print("Daniel: Let's get out of here.")
        print("The door opens...")
        return(True, 0)
    else:
        tries_left -= 1
        print("Daniel: This code is not the right one !")
        time.sleep(0.7)
        print("DANIEL IS STRONGER THAN YOU!")
        print("Daniel: I'll kill you.")
        time.sleep(0.7)
        print("Daniel slams you to the ground and starts punching you.")
        time.sleep(0.7)
        return (False, 1)



name = intro()
victory = False
player_status = 0
has_symbols = False
SYMBOLS = "!@#$%^&*()_-+=<>,./?'\"|\\"
while True:
    print("""
    1. Wake Daniel up - Tell him you've found the code
    2. Explore the building
    3. Quit
    """)
    choice = input("Choose an option: ")
    if choice == "1":
        code = input("Enter the code: ").strip()
        for i in SYMBOLS:
            if i in code:
                has_symbols = True
        if len(code) > 4:
            print("The code is too long.")
            has_symbols = False
            continue
        elif len(code) < 4:
            print("The code is too short.")
            has_symbols = False
            continue
        elif code.isalpha():
            print("The code must contain only digits.")
            has_symbols = False
            continue
        elif has_symbols:
            print("The code must contain only digits.")
            has_symbols = False
            continue
        elif code.isdigit() == False:
            print("The code must contain only digits.")
            has_symbols = False
            continue
        if tries_left == 3:
            victory, player_status = wake_daniel1(code)
        elif tries_left == 2:
            victory, player_status = wake_daniel2(code)
        elif tries_left == 1:
            victory, player_status = wake_daniel3(code)
        if victory:
            print("You figured out the code in", end=" ")
            print(3 - tries_left, "Tries")
            tries_left = 3
            victory = False
            choice = input("Do you want to play again? Y/n").upper()
            if choice == "Y":
                CODE = random.randint(1000, 9999)
                CODE = str(CODE)
                name = intro()
                continue
            else:
                sys.exit("See you soon!")
        elif player_status == 1:
            print("You died, Daniel ended your life")
            print("The code was: ", CODE)
            tries_left = 3
            victory = False
            choice = input("Do you want to play again? Y/n").upper()
            if choice == "Y":
                CODE = random.randint(1000, 9999)
                CODE = str(CODE)
                name = intro()
                continue
            else:
                sys.exit("See you soon!")



    elif choice == "2":
        while True:
            print("""
            1. Explore Room 1
            2. Explore Room 2
            3. Explore Room 3
            4. Explore Room 4
            5. Explore the Hallway
            6. Explore the Restroom
            7. Return to the main menu
            """)
            choice = input("Choose an option: ").strip()
            if choice == "1":
                print("Room 1")
                print("There is a large, round red couch with the number",(CODE[0:1]),"on it.")
                continue
            if choice == "2":
                print("Room 2")
                print("There is a number written on the green carpet:", (CODE[3:4]))
                continue
            elif choice == "3":
                print("Room 3")
                print("There's nothing interesting to see.")
                print("Except for the purple light on the ceiling and the number", (CODE[2:3]))
                continue
            elif choice == "4":
                print("Room 4")
                print("There's a key on the table and a note that says: 'olleh'.")
                continue
            elif choice == "5":
                print("Hallway")
                print("There is a blue umbrella on a shelf, shaped like the number", CODE[1:2])
                continue
            elif choice == "6":
                print("The toilet paper has this color pattern:")
                print("Green - Purple - Blue - Red")
                continue
            elif choice == "7":
                break
            else:
                print("Invalid choice.")
                continue

    elif choice == "3":
        sys.exit("See you soon!")

    else:
        print("Invalid choice.")
        continue

# EXAM 
# FINAL_SCORE = 7.5
