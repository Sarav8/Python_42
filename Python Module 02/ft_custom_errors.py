
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(height: int):
    if height < 0:
        raise PlantError("The tomato plant is wilting!")


def check_water(water: int):
    if water < 0:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        check_plant(-3)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        check_water(-9)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    try:
        print("Testing catching all garden errors...")
        check_plant(-8)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(-9)
    except GardenError as e:     
        print(f"Caught GardenError: {e}\n")
    print("All custom error types work correctly!")
