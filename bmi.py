# Write a simple program that calculates the Body Mass Index
# Formula: 
# BMI = weight X 703 / height^2

weight = int(input("What is your weight: "))
height = int(input("What is your height: "))


print("Your BMI is " + str(weight * 703 / height ** 2))