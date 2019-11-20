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

def go_direction(try_direction, current_room):
    attribute = try_direction + '_to'

    if hasattr(current_room, attribute):
        new_room = getattr(current_room, attribute)
        return  new_room
    else:
        print(f'This direction goes no where(yet)') 
        return current_room   

player_name = input('Please enter your name!')
player = Player(player_name, room['outside'])

player_input = ""

#print(f'{player.name.title()} is currently in {player.current_room}')
while player_input != 'q':
    print(f' \t {player.name.title()} is currently in {player.current_room}')
    player_input = input('Choose directions: n, s, e, w OR q to quit ')

    if player_input == 'n' or player_input == 's' or player_input == 'e' or player_input == 'w':
        player.current_room = go_direction(player_input, player.current_room)
    elif(player_input == 'q'):
        print(f'Thanks for playing {player_name}')
