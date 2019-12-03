from room import Room
from player import Player
from item import Item
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

#print(room['foyer'])

items = {    # CANNOT use advCoin as name
    'dagger': Item('dagger', 'you got a weapon!'),
    'advcoin': Item('advcoin', 'you an buy stuff with these !'),
    'shield': Item('shield', 'you can block against attacks !'),
    'scroll': Item('scroll', 'useful info here(if you can read it)'),
    'water': Item('water', 'you can use to replenish health !')
}

# Link items to specific rooms
room['foyer'].items = [items['dagger']]
room['treasure'].items = [items['advcoin']]
room['narrow'].items = [items['water'], items['scroll']]
room['overlook'].items = [items['shield'], items['water'], items['advcoin']]

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
        return getattr(current_room, attribute)
    else:
        print(f' Oops!! This direction goes no where(yet)') 
        return current_room   

player_name = input('Please enter your name!  ')
player = Player(player_name, room['outside'])

print(f'SANITY: player.name is {player.name}')
player_input = ""

#print(f'{player.name.title()} is currently in {player.current_room}')
while player_input != 'q':
   # print(f' \t {player.name.title()} is currently in {player.current_room}')
    player_prompt = "\t\t\t North is n, South is s, East is e, West is w \n"
    player_prompt += "\t\t For items, take(name) OR  drop(name) OR inspect(name) \n"
    player_prompt += "\t\t\t\t Inventory is i \n"
    player_prompt += "\t\t\t\t Choose q to quit \n"
    player_prompt += "Please choose directions? : n, s, e, w "
    #print(f' \t {player.name.title()} is currently in {player.room_name(player.current_room)}')
    # print(f" {player.name} is currently in {player.current_room}")
    player_input = input(player_prompt).lower()

    if player_input == 'n' or player_input == 's' or player_input == 'e' or player_input == 'w':
        player.current_room = go_direction(player_input, player.current_room)
        # print(f"  currently in {player.current_room}")
        # print(f" {player.name} is currently in {player.current_room}")
        print('room name is: ', player.current_room)
        # print(player.name + ' is now in the ' + str(player.current_room))
    elif('take' in player_input or 'drop' in player_input or 'inspect' in player_input):
        complex_action = player_input.split()
        verb = complex_action[0]
        item_name = complex_action[1]

        try:
            item = items[item_name]

            if verb == 'take':
                if item in player.current_room.items:
                    player.current_room.remove_item(items[item_name])
                    player.take_item(items[item_name])
                    print('Items are now: ', items[item_name].on_take())
                else:
                    print(' that item not in this room')

            elif verb == 'drop':
                if item in player.items:
                    player.current_room.add_item(items[item_name])
                    player.drop_item(items[item_name])
                    print ('Items are now: ', items[item_name].on_drop())
                else:
                    print(' This is not in your inventory') 

            elif verb == 'inspect':
                if item in player.items:
                    print(item.on_inspect())
                else:
                    print('NOT in inventory, go look for it ! ')        

        except KeyError:
            print('ERROR: not an item !!')   

        print(f'{player.name} has items: ', player.items)                                    

    elif (player_input == 'i'):
        print(f'\n Your items are: {player.items}')

    elif(player_input == 'q'):
        print(f'Thanks for playing {player_name}')
    else: 
        print('ERROR!  enter a valid letter choice: n, s, e, w, or q ')    
