from project.room import Room
class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [room for room in self.rooms if room.number == room_number][0]
        room.take_room(people)



    def free_room(self, room_number: int):
        room = [room for room in self.rooms if room.number == room_number][0]
        guests_count = room.guests
        room.free_room()


    def status(self):
        free_rooms = [room for room in self.rooms if not room.is_taken]
        taken_rooms = [room for room in self.rooms if room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(room.number) for room in free_rooms])}\n" \
               f"Taken rooms: {', '.join([str(room.number) for room in taken_rooms])}"


