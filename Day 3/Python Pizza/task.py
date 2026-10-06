print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

final_bill = 0

# Pizza size
if size == "s" or size == "S":
    final_bill += 15

    if pepperoni == "y" or pepperoni == "Y":
        final_bill += 2

elif size == "m" or size == "M":
    final_bill += 20

    if pepperoni == "y" or pepperoni == "Y":
        final_bill += 3

elif size == "l" or size == "L":
    final_bill += 25

    if pepperoni == "y" or pepperoni == "Y":
        final_bill += 3

# Extra cheese
if extra_cheese == "y" or extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")