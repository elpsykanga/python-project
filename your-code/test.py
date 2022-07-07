import cmd
import textwrap
import sys
import os
import time
import random



screen_width = 100

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





### GAME START###
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
            print('ok for now')
    while action.lower() not in ["panic", "turn on tv"]:
        print("you're chained to a couch, so you dont have a lot of options (enter a valid input)")
        action = input('>   ')
        if action.lower() == ('panic'):
                print("You panic")
                waiting(0.5)
                print("Nothing happens")
        if action.lower() == ("turn on tv"):
            print('ok for now')
    
        

def start_game():
    """
    Start the game
    """
    waiting(0.25)
    print("You wake up on a couch and find yourself in a concrete room with no windows. You see that your arm is chained to the wall.")
    print("You don't remember why you are here and what happened before you awoke. You see a small tv infront of you.")
    print()
    play_action()
    
       


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

title_screen()