
year = int(input("Enter year: "))

if year <= 0:
    print("Error: Enter a positive year")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
            reason = "Century year divisible by 400"
        else:
            leap = False
            reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        leap = True
        reason = "Divisible by 4 and not a century year"
    else:
        leap = False
        reason = "Not divisible by 4"

    print("\nCALENDAR VERIFICATION SYSTEM")
    print("Year:", year)

    if leap:
        print("Status: LEAP YEAR")
        print("Days in Year: 366 days")
        print("Days in February: 29 days")
    else:
        print("Status: COMMON YEAR")
        print("Days in Year: 365 days")
        print("Days in February: 28 days")

    print("Reason:", reason)