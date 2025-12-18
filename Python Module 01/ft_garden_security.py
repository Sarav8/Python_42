"""
A secure plant class that protects its data (height, age) and allows controlled access.

Methods:
set_height(new_height) - Updates height if valid, rejects negatives.
set_age(new_age) - Updates age if valid, rejects negatives.
get_height() - Returns current height.
get_age() - Returns current age.
get_info() - Prints plant information.
"""
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name.capitalize()}")
        

    def set_height(self, new_height: int):
        if new_height < 0:
            print(
                f"Invalid operation attempted: height "
                f"{new_height}cm [REJECTED]"
                )
            print("Security: Negative height rejected\n")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")


    def set_age(self, new_age: int):
        if new_age < 0: 
            print(f"Invalid operation attempted: age {new_age}cm [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]\n")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age
    
    def get_info(self):
        name_c = self.name.capitalize()
        print(f"Current plant: {name_c} ({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 20, 30)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.get_info()
