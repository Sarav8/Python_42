
def garden_operations(type_error: str):
    if (type_error == "ValueError"):
        int("sara")
    elif (type_error == "ZeroDivisionError"):
        1 / 0
    elif (type_error == "FileNotFoundError"):
        open("missing.txt")
    elif (type_error == "KeyError"):
        my_dict = {}
        my_dict["missing_plant"]


def test_error_types():
    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError as e:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    try: 
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: No such file 'missing.txt\n")
    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except KeyError as e:
        print("Caught KeyError: 'missing\_plant'\n")
    try:
        print("Testing multiple errors together...")
        int("abcd")
        1 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")
