# Write a class to hold player information, e.g. what room they are in
# currently.


class playerStats:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def __str__(self):
        return f"Player: {self.name} is in the {self.currentRoom.name}. \n {self.currentRoom.description}"

    def move_direction(self, direction):
        if direction == 'n':
            if self.currentRoom.n_to == None:
                return print("Movement isn't allowed")
            self.currentRoom = self.currentRoom.n_to
        elif direction == 's':
            if self.currentRoom.s_to == None:
                return print("Movement isn't allowed")
            self.currentRoom = self.currentRoom.s_to
        elif direction == 'w':
            if self.currentRoom.w_to == None:
                return print("Movement isn't allowed")
            self.currentRoom = self.currentRoom.w_to
        elif direction == 'e':
            if self.currentRoom.e_to == None:
                return print("Movement isn't allowed")
            self.currentRoom = self.currentRoom.e_to
        else:
            return print("Invalid direction")
        return self.currentRoom