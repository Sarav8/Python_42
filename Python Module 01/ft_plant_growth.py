
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.days = age

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        name_c = self.name.capitalize()
        print(f"{name_c}: {self.height}cm, {self.days} days old")


rose = Plant("rose", 25, 30)
start = 1
end = 7
print("=== Day 1 ===")
rose.get_info()
while (start < end):
    rose.grow()
    rose.age()
    start += 1

print("=== Day 7 ===")
rose.get_info()
growth = rose.height - 25
print(f"Growth this week +{growth}cm")
