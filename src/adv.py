# Add a REPL parser to `adv.py` that accepts directional commands to move the player

from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mouth beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
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

# Cardinal directions
directions = ['n', 's', 'e', 'w']

# Make a new player object that is currently in the 'outside' room.
player = Player('Player1', room['outside'])

# Write a loop that:
while True:
    # Prints the current room name
    print(player.room)
    # Prints the current description (the textwrap module might be useful here).
    print(player.room.description)
    
    # Waits for user input and decides what to do.
    user_input = input('Which direction do you want to go:\n (n), (s), (e), or (w)?\n Or press (q) to quit.')

    # If the user enters a cardinal direction, attempt to move to the room there.
    if user_input == 'n':
        if hasattr(player.room, 'n_to'):
            print('Move North.')
            player.room = player.room.n_to
        else:
            # Print an error message if the movement isn't allowed.
            print('You cannot go that way. Please try again.\n Which direction do you want to go:\n (n), (s), (e), or (w)?\n Or press (q) to quit.')
    elif user_input == 's':
        if hasattr(player.room, 's_to'):
            print('Move South.')
            player.room = player.room.s_to
        else:
            print('You cannot go that way. Please try again.\n Which direction do you want to go:\n (n), (s), (e), or (w)?\n Or press (q) to quit.')
    elif user_input == 'e':
        if hasattr(player.room, 'e_to'):
            print('Move East.')
            player.room = player.room.e_to
        else:
            print('You cannot go that way. Please try again.\n Which direction do you want to go:\n (n), (s), (e), or (w)?\n Or press (q) to quit.')
    elif user_input == 'w':
        if hasattr(player.room, 'w_to'):
            print('Move West.')
            player.room = player.room.w_to
        else:
            print('You cannot go that way. Please try again.\n Which direction do you want to go:\n (n), (s), (e), or (w)?\n Or press (q) to quit.')
    # If the user enters "q", quit the game.
    elif user_input == 'q':
        print('Good-bye.')
        quit()

"""
hasattr() method
    Syntax : hasattr(obj, key)

    Parameters :
    obj : The object whose which attribute has to be checked.
    key : Attribute which needs to be checked.

    Returns : Returns True, if attribute is present else returns False.
"""
