class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def __str__(self):
        # this will print out the name of the room
        # as well as any description that the room has 
        output = f"\n{self.description}\n"
        return output