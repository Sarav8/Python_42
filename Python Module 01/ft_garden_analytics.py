
class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str, blooming: bool):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, blooming: bool, prize_points: int):
        super().__init__(name, height, color, blooming)
        self.prize_points = prize_points


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []

    def add_plants(self, plant):
        self.plants.append(plant)
        name_c = plant.name.capitalize()
        print(f"Added {name_c} to {self.owner}'s garden")
    
    def grow_all_plants(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            name_c = plant.name.capitalize()
            print(f"{name_c} grew 1cm")


if __name__ == "__main__":
    oak = Plant("oak tree", 100)
    rose = FloweringPlant("rose", 25, "red", True)
    sunflower = PrizeFlower("sunflower", 50, "yellow", True, 10)
    print("=== Garden Management System Demo ===")
    alice_garden = Garden("Alice")
    alice_garden.add_plants(oak)
    alice_garden.add_plants(rose)
    alice_garden.add_plants(sunflower)
    print("")
    alice_garden.grow_all_plants()
    print("")
    print(f"=== {alice_garden.owner}'s Garden Report ===")
