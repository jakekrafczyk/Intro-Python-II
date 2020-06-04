# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None


    def __str__(self):
        # this will print out the name of the room
        # as well as any description that the room has 
        output = f"\nYou are at the {self.name}. {self.description}\n"
        return output

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_n_to(self):
        return self.n_to

    