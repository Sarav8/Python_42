"""
A class to represent a plant.
Attributes:
name (str): Plant's name.
height (int): Plant's height in cm.
days (int): Plant's age in days.
Methods:
grow(), age(), get_info().
"""
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.days = age

    def grow(self):
        """Increases height by 1 cm."""
        self.height += 1

    def age(self):
        """Increases age by 1 day."""
        self.days += 1

    def get_info(self):
        """Prints the plant's name, height, and age."""
        name_c = self.name.capitalize()
        print(f"{name_c}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    start = 1
    end = 7
    print("=== Day 1 ===")
    rose.get_info()
    while (start < end):
        rose.grow()
        rose.age()
        start += 1

    print("=== Day 7 ===")
    rose.get_info()
    growth = rose.height - 25
    print(f"Growth this week: +{growth}cm")
