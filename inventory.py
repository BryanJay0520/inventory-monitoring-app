inventory = [ # Gumawa ng listahan para sa imbentaryo ng mga supply.
    {"name": "Noodles", "quantity": 20, "reorder_level": 5},
    {"name": "Soup base", "quantity": 3, "reorder_level": 5},
] # Ang listahan na ito ay naglalaman ng mga dictionary na kumakatawan sa bawat item sa imbentaryo, kasama ang pangalan ng item, dami nito, at ang antas ng muling pag-order..
item_name = input("Which supply was used?").strip() # Humingi ng input mula sa user para sa pangalan ng supply na ginamit at alisin ang anumang labis na puwang.
used_amount = int(input("How many units were used? ")) # Humingi ng input mula sa user para sa dami ng ginamit na supply at i-convert ito sa integer.
found_item = False # Magtakda ng flag na nagpapahiwatig kung natagpuan ang item sa imbentaryo.
for item in inventory: # I-loop sa bawat item sa imbentaryo.
    if item["name"].lower() == item_name.lower(): # Kung ang pangalan ng item sa imbentaryo ay tumutugma sa input ng user (case-insensitive).
        found_item = True # Itakda ang flag na natagpuan ang item.
        if item["quantity"] >= used_amount: # Kung sapat ang dami ng item para sa ginamit na halaga.
            item["quantity"] -= used_amount # Bawasan ang dami ng item sa imbentaryo.
            print(f"{used_amount} units of {item['name']} have been used. Remaining quantity: {item['quantity']}.") # Ipakita ang natitirang dami.
            if item["quantity"] < item["reorder_level"]: # Kung ang natitirang dami ay mas mababa sa antas ng muling pag-order.
                print(f"Warning: {item['name']} is below the reorder level. Please reorder soon.") # Magbigay ng babala para sa muling pag-order.
        else: # Kung hindi sapat ang dami ng item para sa ginamit na halaga.
            print(f"Error: Not enough {item['name']} in inventory. Current quantity: {item['quantity']}.") # Ipakita ang error message.
        break # Lumabas sa loop pagkatapos matagpuan at maproseso ang item.
if not found_item: # Kung hindi natagpuan ang item sa imbentaryo.
    print(f"Error: {item_name} not found in inventory.") # Ipakita ang error message na hindi natagpuan ang item.