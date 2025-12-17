"""
A class to represent a plant.
Attributes:
name (str): Plant's name.
height (int): Plant's height in centimeters.
days (int): Plant's age in days.
Methods:
__init__(name, height, age): Initializes a new plant with the given name, height, and age.
grow(): Increases height by 1 cm.
age(): Increases age by 1 day.
get_info(): Displays the plant's name, height, and age.
"""
class Plant:
    count = 0

    def __init__(self, name: str, starting_height: int, starting_age: int):
        """
        Initializes the plant with the specified name, height, and age.
        """
        self.name = name
        self.height = starting_height
        self.age = starting_age
        Plant.count += 1

    def create(self):
        name_c = self.name.capitalize()
        print(f"Create: {name_c} ({self.height}cm, {self.age} days)")
        

if __name__ == "__main__":
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
    print("")
    print(f"Total plants created: {Plant.count}")
