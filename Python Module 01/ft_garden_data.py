"""
A class to represent a plant.
Attributes:
name (str): name of the plant.
height (int): height of the plant in centimeters.
age (int): age of the plant in days.
Methods:
get_info(): Displays the plant's name, height, and age.
"""
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        name_c = self.name.capitalize()
        print(f"{name_c}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()
