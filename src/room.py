# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap
wrapper = textwrap.TextWrapper()

class Room():
    def __init__(self, room, description, items = []):
        self.room = room
        self.description = description
        self.items = items
        
    # without this, it just returns Mags is currently in <room.Room object at 0x108cc2730>
    def __repr__(self):
        items = ''
        if len(self.items) > 0:
            for(index, item) in enumerate(self.items):
                items += f'{item.name} '
        else:    
            items: 'none'                  

        print(f'The {self.room} room \n')
        descript = wrapper.wrap(self.description)    
        items = wrapper.wrap(items)

        string = '\n'
        for line in descript:
            string += line + '\n'
        string += 'In this room, we have: '
        for line in items:
            string += line + '\n'

        return string + '\n'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)        

    # def __str__(self):
    #         return f'the {self.room} room'   
   #  going to add item stuff here    
