
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def ft_garden_data(self):
        name_c = self.name.capitalize()
        print(f"{name_c}: {self.height}cm, {self.age} days old")


rose = Plant("rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("cactus", 15, 120)

print("=== Garden Plant Registry ===")
rose.ft_garden_data()
sunflower.ft_garden_data()
cactus.ft_garden_data()
