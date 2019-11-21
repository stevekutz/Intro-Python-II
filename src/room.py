# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        #self.items = items
        
    # without this, it just returns Mags is currently in <room.Room object at 0x108cc2730>
    def __repr__(self):
        return f'the {self.name} room'    

    def __str__(self):
        return f'the {self.name} room'  

        # going to add item stuff here    