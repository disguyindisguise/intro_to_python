# Write a program that asks the user to enter the number of push-ups they can do. The program should force the user to enter a valid number by repeating the question until a number between 0 and 500 is entered. Once a valid answer is provided, the program should print out: “Wimp!! I can do X.” where X is one more that what the user entered.


push_ups = int(input("How many push-ups can you do? "))

while not (push_ups >= 0 and push_ups <= 500):
  push_ups = int(input("Liar, please enter a number between 0 and 500: "))

else:
  print("Wimp!! I can do " + str(push_ups + 1) + ".")
  