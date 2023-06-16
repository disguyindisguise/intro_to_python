# Write a Python program that calculates how many hours and days have past since you were born.
# For example, if you are 1 years old. It should print the following:
# You have lived: 8760 hours or 365 days

years = int(input("How old are you? "))
days = years * 365
hours = days * 24
print ("You have lived: " + str(hours) + " or " + str(days))