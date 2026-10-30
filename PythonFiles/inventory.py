inventory = [ # Gumawa ng listahan para sa imbentaryo ng mga supply.
    {"name": "Noodles", "quantity": 20, "reorder_level": 5},
    {"name": "Soup base", "quantity": 3, "reorder_level": 5},
] # Ang listahan na ito ay naglalaman ng mga dictionary na kumakatawan sa bawat item sa imbentaryo, kasama ang pangalan ng item, dami nito, at ang antas ng muling pag-order..
for item in inventory: # I-loop sa bawat item sa imbentaryo.
    print(f"Item: {item['name']}, Quantity: {item['quantity']}, Reorder Level: {item['reorder_level']}") # I-print ang pangalan ng item, dami, at antas ng muling pag-order para sa bawat item.