import playsound
import pygame
from pygame import mixer
import cmd
import textwrap
import sys
import os
import time
import random




pygame.init()
soundObj = mixer.Sound('SawTheme.ogg')
soundObj.play()
pygame.mixer.music.load('SawTheme.ogg')
pygame.mixer.music.play(-1)

# define rooms and items

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

outside = {
  "name": "outside"
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}
key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}



bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

door_d = {
    "name": "door d",
    "type": "door",
}
key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}
living_room = {
    "name": "living room",
    "type": "room",
}

#
all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "outside": [door_a],
    "door a": [game_room, bedroom_1],
    "bedroom 1":[queen_bed, door_b, door_c,door_a],
    "queen bed":[key_b],
    "door b":[bedroom_1, bedroom_2],
    "bedroom 2":[double_bed,dresser, door_b],
    "double bed":[key_c],
    "door c":[bedroom_1, living_room],
    "dresser":[key_d],
    "living room": [dining_table, door_d, door_c],
    "door d": [living_room, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

### Generating Funtions ###


### TEXT DELAY ###
def waiting(t):
    time.sleep(t)
    print('.')
    print()
    time.sleep(t)
    print('.')
    print()
    time.sleep(t)
    print('.')
    print()


def talk_speed(dialog, speed):
    sys.stdout.write(dialog)
    sys.stdout.flush()
    time.sleep(speed)

### GAME SEQUENCE###
def start_game():
    
    waiting(0.25)
    print("You wake up on a couch and find yourself in a concrete room with no windows. You see that your arm is chained to the wall.")
    print("You don't remember why you are here and what happened before you awoke. You see a small tv infront of you.")
    print()
    play_action()

def play_action():
    print('What do you do?')
    print('Options-> Turn on tv or panic!')
    action = input('>   ')
    if action.lower() == ('panic'):
            print("You panic")
            waiting(0.5)
            print("Nothing happens")
            start_game()
    if action.lower() == ("turn on tv"):
            intro_tv()
    while action.lower() not in ["panic", "turn on tv"]:
        print("You're chained to a couch, so you dont have a lot of options (enter a valid input)")
        action = input('>   ')
        if action.lower() == ('panic'):
                print("You panic")
                waiting(0.5)
                print("Nothing happens")
        if action.lower() == ("turn on tv"):
            intro_tv()

 ### Dialogue ###   
def intro_tv():
    waiting(0.3)
    print("You turn on the tv to see a puppet staring back at you, motionless.")
    talk1 = "Hello friend, you've been asleep for a long time\n"
    for character in talk1:
        talk_speed(character, 0.05)
    question1 = "Before we go on, please tell me your name\n"
    talk_speed(question1, 0.05)
    player_name = input(">   ")
    player1name = player_name
    waiting(0.3)
    talk2 = player1name + " hmm what a nice name for a dead person now...\n"
    for character in talk2:
        talk_speed(character, 0.05)
    question2 = "Please tell me how you're feeling\n"
    for character in question2:
        talk_speed(character, 0.05)
    vibe = input("How are you feeling \n"+ "\n>   ")
    player1_emotion = vibe.lower()

#Creates the adjective vocabulary for the player's feeling.

    good_adj = ['good', 'great', 'rohit', 'happy', 'aight', 'understanding', 'great', 'alright', 'calm', 'confident', 'not bad', 'courageous', 'peaceful', 'reliable', 'joyous', 'energetic', 'at', 'ease', 'easy', 'lucky', 'k', 'comfortable', 'amazed', 'fortunate', 'optimistic', 'pleased', 'free', 'delighted', 'swag', 'encouraged', 'ok', 'overjoyed', 'impulsive', 'clever', 'interested', 'gleeful', 'free', 'surprised', 'satisfied', 'thankful', 'frisky', 'content', 'receptive', 'important', 'animated', 'quiet', 'okay', 'festive', 'spirited', 'certain', 'kind', 'ecstatic', 'thrilled', 'relaxed', 'satisfied', 'wonderful', 'serene', 'glad', 'free', 'and', 'easy', 'cheerful', 'bright', 'sunny', 'blessed', 'merry', 'reassured', 'elated', '1738', 'love', 'interested', 'positive', 'strong', 'loving']
    hmm_adj = ['idk', 'concerned', 'lakshya', 'eager', 'impulsive', 'considerate', 'affected', 'keen', 'free', 'affectionate', 'fascinated', 'earnest', 'sure', 'sensitive', 'intrigued', 'intent', 'certain', 'tender', 'absorbed', 'anxious', 'rebellious', 'devoted', 'inquisitive', 'inspired', 'unique', 'attracted', 'nosy', 'determined', 'dynamic', 'passionate', 'snoopy', 'excited', 'tenacious', 'admiration', 'engrossed', 'enthusiastic', 'hardy', 'warm', 'curious', 'bold', 'secure', 'touched', 'brave', 'sympathy', 'daring', 'close', 'challenged', 'loved', 'optimistic', 'comforted', 're', 'enforced', 'drawn', 'toward', 'confident', 'hopeful', 'difficult']
    bad_adj = ['bad', 'meh', 'sad', 'hungry', 'unpleasant', 'feelings', 'angry', 'depressed', 'confused', 'helpless', 'irritated', 'lousy', 'upset', 'incapable', 'enraged', 'disappointed', 'doubtful', 'alone', 'hostile', 'discouraged', 'uncertain', 'paralyzed', 'insulting', 'ashamed', 'indecisive', 'fatigued', 'sore', 'powerless', 'perplexed', 'useless', 'annoyed', 'diminished', 'embarrassed', 'inferior', 'upset', 'guilty', 'hesitant', 'vulnerable', 'hateful', 'dissatisfied', 'shy', 'empty', 'unpleasant', 'miserable', 'stupefied', 'forced', 'offensive', 'detestable', 'disillusioned', 'hesitant', 'bitter', 'repugnant', 'unbelieving', 'despair', 'aggressive', 'despicable', 'skeptical', 'frustrated', 'resentful', 'disgusting', 'distrustful', 'distressed', 'inflamed', 'abominable', 'misgiving', 'woeful', 'provoked', 'terrible', 'lost', 'pathetic', 'incensed', 'in', 'despair', 'unsure', 'tragic', 'infuriated', 'sulky', 'uneasy', 'cross', 'bad', 'pessimistic', 'dominated', 'worked', 'up', 'a', 'sense', 'of', 'loss', 'tense', 'boiling', 'fuming', 'indignant', 'indifferent', 'afraid', 'hurt', 'sad', 'insensitive', 'fearful', 'crushed', 'tearful', 'dull', 'terrified', 'tormented', 'sorrowful', 'nonchalant', 'suspicious', 'deprived', 'pained', 'neutral', 'anxious', 'pained', 'grief', 'reserved', 'alarmed', 'tortured', 'anguish', 'weary', 'panic', 'dejected', 'desolate', 'bored', 'nervous', 'rejected', 'desperate', 'preoccupied', 'scared', 'injured', 'pessimistic', 'cold', 'worried', 'offended', 'unhappy', 'disinterested', 'frightened', 'afflicted', 'lonely', 'lifeless', 'timid', 'aching', 'grieved', 'shaky', 'victimized', 'mournful', 'restless', 'heartbroken', 'dismayed', 'doubtful', 'agonized', 'threatened', 'appalled', 'cowardly', 'humiliated', 'quaking', 'wronged', 'menaced', 'alienated', 'wary']
### Defining the feelings the player has ####
    if player1_emotion in good_adj:
        response_string = "thats good to hear that you feel"
    elif player1_emotion in bad_adj:
        response_string = "im sorry to hear that you feel "
    elif player1_emotion in hmm_adj: 
        response_string = "thats interesting that you feel"
    else:
        response_string = "I'm a puppet and I can't really feel"
    
    talk3 = "Well then, " + player1name + ", " + response_string + " " + player1_emotion + ".\n"
    for character in talk3:
        talk_speed(character, 0.05)
    waiting(0.5)
    talk4 = "Now, enough time wasting. You are stuck in here and you must get out alive. I have laid out a series of tests for you. Figure them out and maybe you'll live, and if you mess up well... \n"
    for character in talk4:
        talk_speed(character, 0.05)
    talk5 = "YOU WILL DIE. \n"
    for character in talk5:
        talk_speed(character, 0.25)
    play_stage1()

 
##### BEGIN GAME #######
def play_stage1():
    """
   This is the opening sequence

    """
   
    print("################################")
    print("#      NOW BEGINS THE GAME     #")
    print("#                               ")
    print("#  WILL YOU BE ABLE TO SURVIVE #")
    print("################################\n")
    print("You are now left alone in the cold concrete room.\n Your arm that's chained to the wall is numb,\n you must have been unconcious for a long time\n 'DAMNIT I KNEW I SHOULDN'T HAVE FALLEN ASLEEP DURING THE PANDAS LESSON' you think to yourself \n if what the puppet said was true you need to get going or you'll end up on the news as just another dead body \n infront of you, you see a handsaw on a coffee table")
    waiting(0.5)
    play_room(game_state["current_room"])


### Title Screen ###
def title_screen_selection():
    option = input('>   ')
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("quit"):
        sys.exit
    while option.lower() not in ["play", "quit"]:
        print("Please enter a valid input if you'd like to keep on living")
        option = input('>   ')
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("quit"):
            sys.exit

def title_screen():
    os.system('clear')
    print()
    print()
    print()
    print('########################################')
    print('####### WELCOME TO OUR SAW GAME ########')
    print('########################################')
    print('##### WILL YOU MAKE IT OUT ALIVE #######')
    print('               -PLAY-                   ')
    print('               -QUIT-                   ')
    print('       Copyright 2022 Ironhack          ')
    title_screen_selection()




def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        pygame.mixer.music.stop()
        soundObj.stop()
        playsound('alive.mp3')
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?")
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Ener 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)

game_state = INIT_GAME_STATE.copy()

title_screen()
