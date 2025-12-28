inventory_alice = {
    "swor" : {
        "category" : "weapon",
        "rarity" : "rare",
        "quantity": "1",
        "value": "500"

    },

    "potion" : {
        "category" : "consumable",
        "rarity" : "common",
        "quantity": "5",
        "value": "50"
    },

    "shield" : {
        "category" : "armor",
        "rarity" : "uncommon",
        "quantity": "1",
        "value": "200"
    }
}

def ft_inventory_system():
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    while i < len(keys):
    item_name = keys[i]
    data = inventory_alice[item_name]

    qty = int(data['quantity'])
    val = int(data['value'])
    category = data['category']
    rarity = data['rarity']
    total_item_value = qty * val
    total_value += total_item_value

    print(f"{item_name} ({category}, {rarity}): {qty}x @ {val} gold each = {total_item_value} gold")
    i += 1

    print(f"Inventory value: {total_value} gold")

