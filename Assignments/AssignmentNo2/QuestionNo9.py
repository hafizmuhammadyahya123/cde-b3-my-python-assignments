# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user

quantity = int(input("Enter the quantity: "))

unit_price = 100

total_cost = quantity * unit_price

if total_cost > 1000:
    discount = total_cost * 0.10  # 10% discount
    total_cost -= discount  #Assignment/Advance  operator --> (Augment statement -=)

print(f"Total cost: {total_cost}")
