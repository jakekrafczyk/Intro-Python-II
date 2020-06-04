from room import Room
from player import Player
from item import Item

# declare items

items = {'sword' : Item('Sword', 'This sword is very rusty.'),
        'armor' : Item('Armor', 'This armor consists of an old breastplate and a helmet.'),
        'hookshot' : Item('Hookshot', 'Use this to grapple across long distances.'),
        'bow' : Item('Bow', 'A strong bow, comes with a quiver full of BOmB arrows.'),
        'lua' : Item('Lua', "It's your cat! She must have beat you to the treasure."),
        'catnip' : Item('Catnip',' "....."')}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['sword','armor']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",['hookshot','bow']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",['lua','catnip']),
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

print("\n\n      | ***   Welcome to Hero's Adventure!   *** |      \n\n")


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
new_room = room[f'{hero.get_room()}']                       # this is the keyword, eg outside                                           
room_name = new_room.get_name()              # this is the Official name, eg Outside Cave Entrance
room_description = new_room.get_description()

print(f'\nYou are {name}, the greatest hero of your time! You have embarked upon a new adventure \
in the hope of finding a great treasure, but these lands are treacherous, so you must choose your \
path carefully.')

print(f'You start at the {room_name}. {room_description}!')



while on == 'start':

    next_input = input('\nWhat do you want to do? ').lower()

    next_input = next_input.split()
    
    next = " " 
    
    # return string   
    next = next.join(next_input)

    if len(next_input) == 2:
        room_items = new_room.get_items()
        if room_items == None:
            print('\nThere are no items in this area.')
        else:
            for x in room_items:
                if next == f'get {x.lower()}':
                    hero.add_item(x)
                    new_room.del_item(x)
                    print(f'\nYou have taken the {x} into your inventory!')
                    print(items[x]) #description here

                else:
                    pass

    else:

        if next == 'q':
            break

        elif next == 'north':
            if new_room.n_to == None:
                print('\nThere is nothing in that direction.')
            else:
                new_room = new_room.n_to
                print(hero.print_inv())
                print(new_room)
                if new_room.items == None:
                    pass
                else:
                    print(new_room.print_items())

        elif next == 'south':
            if new_room.s_to == None:
                print('\nThere is nothing in that direction.')
            else:
                new_room = new_room.s_to
                print(hero.print_inv())
                print(new_room)
                if new_room.items == None:
                    pass
                else:
                    print(new_room.print_items())

        elif next == 'east':
            if new_room.e_to == None:
                print('\nThere is nothing in that direction.')
            else:
                new_room = new_room.e_to
                print(hero.print_inv())
                print(new_room)
                if new_room.items == None:
                    pass
                else:
                    print(new_room.print_items())

        elif next == 'west':
            if new_room.w_to == None:
                print('\nThere is nothing in that direction.')
            else:
                new_room = new_room.w_to
                print(hero.print_inv())
                print(new_room)
                if new_room.items == None:
                    pass
                else:
                    print(new_room.print_items())

        else:
            print('\nError: You must input a cardinal direction to move(Eg. north) or a get "item" command')
