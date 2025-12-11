
class Plant:
    count = 0

    def __init__(self, name: str, starting_height: int, starting_age: int):
        self.name = name
        self.height = starting_height
        self.age = starting_age
        Plant.count += 1

    def create(self):
        name_c = self.name.capitalize()
        print(f"Create: {name_c} ({self.height}cm, {self.age}days)")


rose = Plant("rose", 25, 30)
oak = Plant("oak", 200, 365)
cactus = Plant("cactus", 5, 90)
sunflower = Plant("sunflower", 80, 45)
fern = Plant("fern", 15, 120)
print("=== Plant Factory Output ===")
rose.create()
oak.create()
cactus.create()
sunflower.create()
fern.create()
print(f"Total plants created: {Plant.count}")
