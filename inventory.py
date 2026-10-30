inventory = [  # Gumagawa ng listahan para paglagyan ng supplies.
    {"name": "Noodles", "quantity": 20, "reorder_level": 5},  # Nagtatala ng stock at reorder level ng noodles.
    {"name": "Soup base", "quantity": 3, "reorder_level": 5},  # Nagtatala ng stock at reorder level ng soup base.
]  # Tinatapos ang listahan ng supplies.
print("Current Inventory:")  # Nagpapakita ng heading bago ilista ang inventory.
for item in inventory:  # Dumadaan sa bawat supply sa listahan.
    print(f"{item['name']}: {item['quantity']} units (Reorder level: {item['reorder_level']})")  # Ipinapakita ang pangalan, stock, at reorder level ng supply.
item_name = input("Which supply was used? ").strip()  # Kinukuha ang pangalan at inaalis ang sobrang space sa simula at dulo.
item_quantity = int(input("How many units were used? "))  # Kinukuha ang dami at ginagawang whole number.
found_item = False  # Nagtatala na wala pang supply na nahanap.
for item in inventory:  # Hinahanap ang supply sa bawat record ng listahan.
    if item["name"].lower() == item_name.lower():  # Ikinukumpara ang pangalan kahit magkaiba ang uppercase at lowercase.
        found_item = True  # Itinatala na nahanap ang supply.
        if item["quantity"] >= item_quantity:  # Tinitingnan kung sapat ang stock para sa daming nagamit.
            item["quantity"] -= item_quantity  # Ibinabawas ang nagamit na units sa stock.
            print(f"{item_quantity} units of {item['name']} have been used. Remaining quantity: {item['quantity']}.")  # Ipinapakita ang daming nagamit at natirang stock.
            if item["quantity"] < item["reorder_level"]:  # Tinitingnan kung mas mababa na sa reorder level ang bagong stock.
                needed = item["reorder_level"] - item["quantity"]  # Kinukuwenta ang kulang para umabot sa reorder level.
                print(f"Warning: {item['name']} is below the reorder level. Please reorder {needed} more units.")  # Nagpapakita ng warning at daming kailangang idagdag.
            elif item["quantity"] == item["reorder_level"]:  # Tinitingnan kung eksaktong kapantay ng reorder level ang stock.
                print(f"{item['name']} is at the reorder level. Consider reordering soon.")  # Nagbibigay ng paalala nang hindi nagsasabing zero units ang kailangan.
            else:  # Tumatakbo ito kapag mas mataas sa reorder level ang stock.
                print(f"{item['name']} is sufficiently stocked.")  # Ipinapakitang sapat pa ang stock.
        else:  # Tumatakbo ito kapag mas marami ang gustong gamitin kaysa sa available na stock.
            print(f"Error: Not enough {item['name']} in inventory. Current quantity: {item['quantity']}.")  # Nagpapakita ng error at kasalukuyang stock.
        break  # Itinitigil ang paghahanap dahil nahanap na ang supply.
if not found_item:  # Sinusuri kung walang pangalan sa listahan na tumugma sa input.
    print(f"Error: {item_name} not found in inventory.")  # Ipinapaalam na wala sa inventory ang supply.