# Write a program that asks the user to enter their phone number without area code but with a dash. The program should then do the math by subtracting the second part of the number from the first. For example, if the user's number is 919-1235 then the program should print out "-316" because 919 - 1235 equals -316.
# Note: You will need string slicing, the str() and int() functions.

phone = input("what is your phone number (###-####): ")

x = int(phone[0:3])
y = int(phone[-4:])

print("Your phone math equals " + str(x - y))