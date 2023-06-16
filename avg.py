# Write a program that asks the user for three numbers and print out the average of the three.

# Your program must handle floating point numbers.


a = float(input("first: "))
b = float(input("second: "))
c = float(input("third: "))

avg = ( a + b + c ) / 3

print("Average is " + str(avg))