
import math

value = float(input("Enter a numerical value: "))
exponent = int(input("Enter an exponent: "))
measurement = float(input("Enter a decimal measurement: "))

power = pow(value, exponent)
square_root = math.sqrt(value)

ceil_value = math.ceil(measurement)
floor_value = math.floor(measurement)

print("\n==============================")
print("  ENGINEERING CALCULATION TOOL")
print("==============================")

print("\n--- Results ---")
print("Value          :", value)
print("Exponent       :", exponent)
print("Power (pow)    :", power)
print("Square Root    :", round(square_root, 4))
print("Decimal Value  :", measurement)
print("Ceil Value     :", ceil_value)
print("Floor Value    :", floor_value)

print("==============================")