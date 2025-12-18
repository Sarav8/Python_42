def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            print("Watering " + plant)
        print("Watering completed successfully")
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system():
    print("Testing normal watering...")
    list1 = ["tomato", "lettuce", "carrots"]
    water_plants(list1)
    print("Testing with error...")
    list2 = ["tomato", None, "carrots"]
    water_plants(list2)


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
