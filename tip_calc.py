# Write a program that prompts the user for the price of a meal (at a restaurant) and a tip p. The program then prints the total cost of the meal.


meal_price = float(input("Enter meal price: "))
tip_percent = float(input("Enter a tip percent: "))

print("Total cost: " + str(meal_price * tip_percent / 100 + meal_price))