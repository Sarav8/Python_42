
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    i = 1

    def recursive(days: int, i: int):
        print(f"Day {i}")
        if days == 1:
            return
        i += 1
        recursive(days - 1, i)
    recursive(days, i)
    print("Harvest time!")