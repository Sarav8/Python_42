"""
This program defines different plant types in a garden.
It uses classes and inheritance to show their behavior.
"""
"""super() allows child classes to reuse the parent class attributes."""


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        name_c = self.name.capitalize()
        print(f"{name_c} is blooming beautifully!\n")

    def get_info(self):
        name_c = self.name.capitalize()
        print(
            f"{name_c} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        name_c = self.name.capitalize()
        height_m = self.height / 100
        shade = int(3.14 * height_m ** 2)
        print(f"{name_c} provides {shade} square meters of shade\n")

    def get_info(self):
        name_c = self.name.capitalize()
        print(
            f"{name_c} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_info(self):
        name_c = self.name.capitalize()
        print(f"{name_c} is rich in {self.nutritional_value}")

    def get_info(self):
        name_c = self.name.capitalize()
        print(
            f"{name_c} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )


if __name__ == "__main__":
    flower1 = Flower("rose", 25, 30, "red")
    flower2 = Flower("rose2", 78, 38, "blue")
    oak1 = Tree("Oak", 500, 1825, 50)
    oak2 = Tree("Oak2", 50, 25, 3)
    tomato1 = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
    tomato2 = Vegetable("Tomato2", 100, 60, "winter", "vitamin c")

    print("=== Garden Plant Types ===\n")

    flower1.get_info()
    flower1.bloom()
    oak1.get_info()
    oak1.produce_shade()
    tomato1.get_info()
    tomato1.nutritional_info()
