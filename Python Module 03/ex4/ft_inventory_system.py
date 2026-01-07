data = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {
            "type": "weapon",
            "value": 150,
            "rarity": "common",
        },
        "quantum_ring": {
            "type": "accessory",
            "value": 500,
            "rarity": "rare",
        },
        "health_byte": {
            "type": "consumable",
            "value": 25,
            "rarity": "common",
        },
        "data_crystal": {
            "type": "material",
            "value": 1000,
            "rarity": "legendary",
        },
        "code_bow": {
            "type": "weapon",
            "value": 200,
            "rarity": "uncommon",
        },
    },
}


def ft_inventory_system():
    print("=== Player Inventory System ===\n")

    player_name = "alice"
    player_data = data["players"].get(player_name)

    print(f"=== {player_name.capitalize()}'s Inventory ===")

    items = player_data["items"]
    total_inventory_value = 0
    total_items = 0

    for item_name, qty in items.items():
        item_info = data["catalog"][item_name]
        type = item_info["type"]
        value = item_info["value"]
        rarity = item_info["rarity"]
        total_value = qty * value
        total_items += qty
        total_inventory_value += total_value

        print(
            f"{item_name} ({type}, {rarity}): "
            f"{qty}x @ {value} gold each = {total_value} gold"
        )

    print(f"\nInventory value: {total_inventory_value} gold")
    print(f"Item count: {total_items} items")

    categories = {}
    for item_name, qty in items.items():
        item_info = data["catalog"][item_name]
        type = item_info["type"]
        categories[type] = categories.get(type, 0)

    print("Categories:", end=" ")
    i = 0
    for cat, qty in items.items():
        if i > 0:
            print(", ", end="")
        print(f"{cat}({qty})", end="")
        i += 1
    print()

    giver = "alice"
    receiver = "bob"
    obj = "health_byte"
    qty_obj = 1

    giver_items = data["players"][giver]["items"]
    receiver_items = data["players"][receiver]["items"]

    if giver_items.get(obj, 0) >= qty_obj:
        giver_items[obj] -= qty_obj
        receiver_items[obj] = receiver_items.get(obj, 0) + qty_obj
        print(
            f"\n=== Transaction: {giver.capitalize()} gives "
            f"{receiver.capitalize()} {qty_obj} {obj} ==="
        )
        print("Transaction successful!")
    else:
        print("Transaction unsuccessful!")

    print("\n=== Updated Inventories ===")
    print(f"{giver} {obj}: {giver_items.get(obj)}")
    print(f"{receiver} {obj}: {receiver_items.get(obj)} ")

    most_valuable_name = None
    most_valuable_value = 0
    most_items_name = None
    most_items_count = 0

    for pname, pdata in data["players"].items():
        if pdata["total_value"] > most_valuable_value:
            most_valuable_value = pdata["total_value"]
            most_valuable_name = pname
        if pdata["item_count"] > most_items_count:
            most_items_count = pdata["item_count"]
            most_items_name = pname

    print("\n=== Inventory Analytics ===")
    print(
        f"Most valuable player: "
        f"{most_valuable_name.capitalize()} ({most_valuable_value} gold)"
    )
    print(
        f"Most items: "
        f"{most_items_name.capitalize()} ({most_items_count} items)"
    )

    item_counts = {}
    for pdata in data["players"].values():
        for item in pdata["items"]:
            item_counts[item] = item_counts.get(item, 0) + 1

    rarest = []
    for item, count in item_counts.items():
        if count == 1:
            rarest.append(item)

    print("Rarest items:", end=" ")
    i = 0
    for item in rarest:
        if i > 0:
            print(", ", end="")
        print(item, end="")
        i += 1
    print()


if __name__ == "__main__":
    ft_inventory_system()
