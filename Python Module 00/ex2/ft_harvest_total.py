
def ft_harvest_total():
    total = 0
    for i in range(3):
        day = int(input(f"Day {i + 1} harvest: "))
        total += day
    print(f"Total harvest: {total}")
