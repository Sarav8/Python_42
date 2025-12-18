class GardenError(Exception):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.level = water_level
        self.sun = sunlight_hours


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plants(self, plant):
        try:
            if plant.name == "":
                raise GardenError("Plant name cannot be empty\n")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Watering plants...")
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_health(self):
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant.level > 10:
                    raise GardenError(
                        f"Water level {plant.level} is too high (max 10)\n"
                    )
                print(f"{plant.name}: healthy (water: {plant.level}, "
                      f"sun: {plant.sun})")
            except GardenError as e:
                print(f"Error checking {plant.name}: {e}")

    def test_error_recovery(self):
        print("Testing error recovery...")
        try:
            raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        print("System recovered and continuing...\n")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    tomato = Plant("tomato", 5, 8)
    letucce = Plant("letucce", 15, 8)
    other = Plant("", 15, 8)
    manager = GardenManager()
    manager.add_plants(tomato)
    manager.add_plants(letucce)
    manager.add_plants(other)
    manager.water_plants()
    manager.check_health()
    manager.test_error_recovery()
    print("Garden management system test complete!")
