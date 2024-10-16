#
print("HELLO OUR DEAR CUSTOMER")
print("You Are Most Welcome")
#
total_amount = float(input("Please ENTER your TOTAL AMOUNT of your order"))
how_much = float(input("How much Have you paid"))
delivery_cut = 0.005
d_amount = 100000
delivery_pay = total_amount*delivery_cut
print("",delivery_pay)
total = delivery_pay+total_amount
print("",total)
#
if total_amount<d_amount:
    print("Free Delivery:")
elif total_amount>total:
        print("Coming Right UP:")
elif total_amount>=total:
      print("Please Pay some More:")
