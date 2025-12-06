n = int(input("Enter number of parcels: "))

total_charges = 0

for i in range(1, n + 1):
    days = int(input(f"Enter storage days for parcel {i}: "))

    if days <= 2:
        charge = 0
    else:
        extra_days = days - 2
        charge = extra_days * 40

    if charge > 300:
        print(f"Parcel {i}: Long Storage")
    else:
        print(f"Parcel {i} Charge: {charge}")

    total_charges += min(charge, 300) 

print("Total Charges:", total_charges)