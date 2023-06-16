# Part 3 
# It should calculate the total cost of an order. Use both the fruit list and price list from parts 1 and 2 to prompt the vendor for quantities of each fruit type, and then print out the total. Note each prompt should show both the fruit name and price.


fruits = []
prices = []

print()
print("***Fruit Inventory***")
fruit_question = input("Enter a fruit name (or done): ")
while fruit_question != "done":
  fruits += [fruit_question]
  fruit_question = input("Enter a fruit name (or done): ")

print()
print("***Price List***")
for x in fruits:
  price = float(input("Enter the price for " + str(x) + ": "))
  prices += [price]
print()
print("Your fruit list is: " + str(fruits))
print("Your price list is: " + str(prices))

print()
print("***Shopping***")
total = 0
for x,y in zip(fruits,prices):
  qty = float(input("Enter the quantity of " + str(x) + " at $" + str(y) + " each: "))
  total += qty * y

round(total, 2)

print("The shopping total is: $" + str(total))