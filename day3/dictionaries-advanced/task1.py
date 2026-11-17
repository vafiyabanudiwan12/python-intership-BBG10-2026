products = {"lapotop":50000,"mouse":500, "keyboard":1500,"pen":20, "mobile": 20000}

new_dict = {k: v for k, v in  products.items() if v > 100}

print(new_dict)
