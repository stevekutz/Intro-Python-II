from player import Player

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

    def on_take(self):
        return (f'\n {self.description}, The {self.name}  was picked up !! ')     

    def on_drop(self):
        return f'\n The {self.name} was dropped !'    

    def on_inspect(self):
        return f' Item: {self.name} \t Description: {self.description} \n'    