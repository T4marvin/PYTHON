#number 1
def convert_to_euros():
    ugx_amount = 200000
    euro_amount = 4000
    convert_rate = ugx_amount/euro_amount
    return convert_rate
convert_to_euros()
print("the exchange rate is",convert_to_euros())
#number2
def distance_travelled():
    speed_km = 60
    time_hrs = 3
    distance = speed_km*time_hrs
    return distance
distance_travelled()
print("the distance travelled is",distance_travelled())
#NUMBER 3
def generate_receipt():
    items = {"Maize": 2000, "Beans": 3000, "Rice": 2500}
    total_cost = sum(items.values())
    print("Receipt:")
    for item, price in items.items():
        print(f"{item}: {price} UGX")
    print(f"Total: {total_cost} UGX")

# Example usage:
generate_receipt()
