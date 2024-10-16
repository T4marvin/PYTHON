#current temperature
temperature_in_entebbe = float(input("Enter the current temperature"))
#
if temperature_in_entebbe > 30:
    print("Hot")
elif temperature_in_entebbe >= 20:
    print("Warm")
elif temperature_in_entebbe < 20:
    print("Cool")
    