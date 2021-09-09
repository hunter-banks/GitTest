import math

voltage = float(input("Please enter the voltage: "))
resistance = float(input("Please enter the resistance: "))

power = math.pow(voltage,2) / resistance
print("\nThe power is:", "{:.2f}".format(power))