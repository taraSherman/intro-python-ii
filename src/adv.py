# Add a REPL parser to `adv.py` that accepts directional commands to move the player
from item import Item
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

# Add items to rooms
room['foyer'].room_items.append('a rusty iron key')
room['narrow'].room_items.append('a small, dim lamp')
room['treasure'].room_items.append('an empty chest')

# Cardinal directions
directions = ['n', 's', 'e', 'w']

# Make a new player object that is currently in the 'outside' room.
player = Player('Player1', room['outside'])

# Write a loop that:
while True:
    # Prints the current room name
    print(player.current_room)
    # Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    
    # Waits for user input and decides what to do.
    user_input = input('Which direction do you want to go:\n (n), (s), (e), or (w)?\nHint: You can [l]ook around and [p]ickup any items that might be useful. Or press (q) to quit.')
    
    def invalid_input_message():
        print(f'Sorry. You cannot do that.\n{user_input}')

    # If the user enters a cardinal direction, attempt to move to the room there.
    if user_input == 'n':
        if hasattr(player.current_room, 'n_to'):
            print('Move North.')
            player.current_room = player.current_room.n_to
        else:
            # Print an error message if the movement isn't allowed.
            invalid_input_message()
    elif user_input == 's':
        if hasattr(player.current_room, 's_to'):
            print('Move South.')
            player.current_room = player.current_room.s_to
        else:
            invalid_input_message()
    elif user_input == 'e':
        if hasattr(player.current_room, 'e_to'):
            print('Move East.')
            player.current_room = player.current_room.e_to
        else:
            invalid_input_message()
    elif user_input == 'w':
        if hasattr(player.current_room, 'w_to'):
            print('Move West.')
            player.current_room = player.current_room.w_to
    # If the user enters "q", quit the game.
    elif user_input == 'q':
        print('Good-bye.')
        quit()
    elif user_input == 'p':
        player.current_room.pickup_item()
        print(
            f'You picked up {player.room.item} and added it to your inventory.')
        player.current_room.remove_item()
    elif user_input == 'l':
        print(f'{player.current_room.room_items}')
    else:
        invalid_input_message()
"""
hasattr() method
    Syntax : hasattr(obj, key)

    Parameters :
    obj : The object whose which attribute has to be checked.
    key : Attribute which needs to be checked.

    Returns : Returns True, if attribute is present else returns False.
"""
