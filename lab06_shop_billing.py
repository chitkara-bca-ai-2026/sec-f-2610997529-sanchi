print("================================")
print("     CLOTHING STORE BILLING SYSTEM")
print("================================")

name = input("Enter Customer Name: ")
garment = input("Enter Garment Name: ")

price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

total = price * quantity

print("\n================================")
print("              BILL")
print("================================")

print("Customer Name :", name)
print("Garment Name  :", garment)
print("Price per Unit: Rs.", price)
print("Quantity      :", quantity)
print("Total Amount  : Rs.", total)

print("================================")