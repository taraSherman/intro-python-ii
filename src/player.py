# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name}'

    def pickup_item(self, item):
        self.inventory.append(item)
        self.current_room.room_items.remove(item)

    def look(self):
        if self.current_room.room_items:
            print(f'You see {self.current_room.room_items}')
        else:
            print(f'There is nothing else here.')