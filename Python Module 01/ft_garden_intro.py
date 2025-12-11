
def ft_garden_intro(plant: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant.capitalize()}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("rose", 25, 30)
