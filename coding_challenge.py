# 1. Gumawa ng inventory na may Noodles at Soup base. Bawat supply ay may name, quantity, at reorder_level.

inventory = [
    {"name": "Noodles", "quantity": 20, "reorder_level": 5},
    {"name": "Soup base", "quantity": 3, "reorder_level": 5}
]

# 2. Ipakita ang laman ng inventory sa simula ng program.

print("Current Inventory:")
for item in inventory:
    print(f"{item['name']}: {item['quantity']} units (Reorder level: {item['reorder_level']})")

# 3. Humingi ng input mula sa user para sa supply na ginamit at ang dami nito.

item_name = input("Which supply was used? ").strip()
item_quantity = int(input("How many units were used? "))

# 4. Hanapin ang supply at ibawas ang nagamit na quantity. Gumagana ang paghahanap kahit uppercase o lowercase ang pangalan.

found_item = False
for item in inventory:
    if item["name"].lower() == item_name.lower():
        found_item = True
        if item["quantity"] >= item_quantity:
            item["quantity"] -= item_quantity
            print(f"{item_quantity} units of {item['name']} have been used. Remaining quantity: {item['quantity']}.")
            if item["quantity"] < item["reorder_level"]:
                needed = item["reorder_level"] - item["quantity"]
                print(f"Warning: {item['name']} is below the reorder level. Please reorder {needed} more units.")
            elif item["quantity"] == item["reorder_level"]:
                print(f"{item['name']} is at the reorder level. Consider reordering soon.")
            else:
                print(f"{item['name']} is sufficiently stocked.")
        else:
            print(f"Error: Not enough {item['name']} in inventory. Current quantity: {item['quantity']}.")
        break

# 5. Ipakita ang error message kung hindi natagpuan ang supply sa inventory.

if not found_item:
    print(f"Error: {item_name} not found in inventory.")