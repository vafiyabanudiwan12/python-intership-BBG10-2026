cart = [ ["keyboard", 800],["Mouse",400],["usb cable", 200]]
total = 0
for item in cart:
    total += item[1]
    #Incorrect assignmet operator(=)
    if total >= 1000:
        disconut = total*10/100
    else:
        disconut = 0
        final_amount = total-disconut
        print("Total:", total)
        print("Discount:",disconut)
        print("Final Amount:",final_amount)