def apply_discount(price, perrcent=10):
    disccont = price * perrcent /100
    final_price = price - disccont
    return final_price
print(apply_discount(1000))
print(apply_discount(1000, perrcent=20))
