
class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.type = "regular"
    
    def info(self):
        print(f"- {self.name.capitalize()}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str, blooming: bool):
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming
        self.type = "flowering"
    
    def info(self):
        print(f"- {self.name.capitalize()}: {self.height}cm, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, blooming: bool, prize_points: int):
        super().__init__(name, height, color, blooming)
        self.prize_points = prize_points
        self.type = "prize"

    def info(self):
        print(f"- {self.name.capitalize()}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize_points}\n")


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        self.plants_added = 0
        self.total_growth = 0

    def add_plants(self, plant):
        self.plants.append(plant)
        self.plants_added += 1
        name_c = plant.name.capitalize()
        print(f"Added {name_c} to {self.owner}'s garden")
    
    def grow_all_plants(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            self.total_growth += 1
            name_c = plant.name.capitalize()
            print(f"{name_c} grew 1cm")

            
    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.info()
        print(f"Plants added: {self.plants_added}, Total growth: {self.total_growth}cm")
        
    def plant_types(self):
        regular = 0
        flowering = 0
        prize = 0
        for plant in self.plants:
            if plant.type == "regular":
                regular += 1
            elif plant.type == "flowering":
                flowering += 1
            elif plant.type == "prize":
                prize += 1
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers\n")
    

class GardenManager:
    gardens_total = []

    def __init__(self, garden):
        self.gardens_total.append(garden)
        result = self.GardenStats.validate_heights(garden.plants)
        print(f"Height validation test: {result}")

    
    @classmethod
    def create_garden_network(cls):
        total_scores = {}
        for garden in cls.gardens_total:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if plant.type == "prize":
                    score += plant.prize_points
            total_scores[garden.owner] = score
        print("Garden scores - " + ", ".join(f"{owner.title()}: {score}" for owner, score in total_scores.items()))
        print(f"Total gardens managed: {len(cls.gardens_total)}\n")



    class GardenStats:
        @staticmethod
        def validate_heights(plants):
            for plant in plants:
                if plant.height < 0:
                    return False
            return True

if __name__ == "__main__":
    oak = Plant("oak tree", 100)
    rose = FloweringPlant("rose", 25, "red", True)
    sunflower = PrizeFlower("sunflower", 50, "yellow", True, 10)
    print("=== Garden Management System Demo ===\n")
    alice_garden = Garden("Alice")
    alice_garden.add_plants(oak)
    alice_garden.add_plants(rose)
    alice_garden.add_plants(sunflower)
    alice_garden.grow_all_plants()
    alice_garden.report()
    alice_garden.plant_types()
    GardenManager.GardenStats.validate_heights(alice_garden.plants)
    manager = GardenManager(alice_garden)
    bob_garden = Garden("Bob")
    bob_garden.plants.append(Plant("pine tree", 90))
    bob_garden.plants.append(FloweringPlant("tulip", 2, "yellow", True))
    manager = GardenManager(bob_garden)
    GardenManager.create_garden_network()


