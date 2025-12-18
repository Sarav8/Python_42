def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!\n")
    elif water_level < 1:
        raise ValueError(f"Error: Water level "
                         f"{water_level} is too low (min 1)\n")
    elif water_level > 10:
        raise ValueError(f"Error: Water level "
                         f"{water_level} is too high (max 10)\n")
    elif sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)\n"
        )
    elif sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)\n"
        )
    else:
        print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    print("Testing good values...")
    try:
        check_plant_health("tomato", 8, 8)
    except ValueError as e:
        print(e)

    print("Testing empty plant name...")
    try:
        check_plant_health("", 8, 8)
    except ValueError as e:
        print(e)

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(e)

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 8, 0)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")
