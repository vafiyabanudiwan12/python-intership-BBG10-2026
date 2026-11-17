inventory = {"pen": 50, "book": 30, "pencil": 40}

inventory["pen"]
product = "book"
quantity = 5

if product in inventory:
    if inventory[product] >= quantity:
        inventory[product] -= quantity
        print("sales successful")
    else:
        print("not enough stock")
else:
    print("product not found")
    print(inventory)
    