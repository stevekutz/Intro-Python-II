# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    # def __repr__(self):
    #     return f' Player called as: {self.name}, self'  

    def take_item(self, item):
        self.items.append(item)    

    def drop_item(self, item):
        self.items.remove(item)      

    # def room_name(self, current_room):
    #     return f'{self.name} is in the {self.current_room} room'      