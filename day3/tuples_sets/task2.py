#create product tuple:(name, price, quantity)
product = ("laptop", 1200.00, 5)

# Instead, we can create a new tuple with the updated price
product = (product[0], 1300.00, product[2])
print("updated product:", product)
