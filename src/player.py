# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, items=None):
        self.name = name
        self.room = room
        self.items = items

    def get_name(self):
        return self.name

    def get_room(self):
        return self.room