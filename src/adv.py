from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

hero = Player('UHTRED','outside')

# WELCOME MESSAGE

print("      | ***   Welcome to Hero's Adventure!   *** |      ")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

on = input("Type start to play: ").lower()

name = hero.get_name()
in_room = hero.get_room()                       # this is the keyword, eg outside
#print(in_room)
room_name = room[f'{in_room}'].get_name()       # this is the Official name, eg Outside Cave Entrance
room_description = room[f'{in_room}'].get_description()

print(f'\nYou are {name}, the greatest hero of your time! You have embarked upon a new adventure \
in the hope of finding a great treasure, but these lands are treacherous, so you must choose your \
path carefully.')

print(f'You start at the {room_name}. {room_description}!')



while on == 'start':

    next = input('\nWhat direction do you want to go? ').lower()

    if next == 'q':
        break

    elif next == 'north':
        new_room = room[f'{in_room}'].n_to
        hero.room = new_room
        #hero.room = room[f'{in_room}'].n_to
        #print('\n',new_room)
        if new_room == None:
            print('\nThere is nothing in that direction.')
        else:
            print(new_room)

    elif next == 'south':
        new_room = room[f'{in_room}'].s_to
        if new_room == None:
            print('\nThere is nothing in that direction.')
        else:
            hero.room = new_room

    elif next == 'east':
        new_room = room[f'{in_room}'].e_to
        if new_room == None:
            print('\nThere is nothing in that direction.')
        else:
            hero.room = new_room

    elif next == 'west':
        new_room = room[f'{in_room}'].w_to
        if new_room == None:
            print('\nThere is nothing in that direction.')
        else:
            hero.room = new_room
    else:
        print('\nError: You must input a cardinal direction. Eg. north')

        

#use dictionary to store events in rooms