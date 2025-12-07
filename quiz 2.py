# Program for a small bus tour company

N = int(input("Enter number of tours: "))

TICKET_PRICE = 900
full_tours = 0

for i in range(1, N + 1):
    passengers = int(input(f"Enter passengers for tour {i}: "))
    revenue = passengers * TICKET_PRICE

    if passengers > 40:
        status = "Full Tour"
        full_tours += 1
    else:
        status = "Not Full"

    print(f"Tour {i} Revenue: {revenue} | {status}")

print(f"\nNumber of Full Tours: {full_tours}")