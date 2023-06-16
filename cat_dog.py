question = input("Do you prefer cats or dogs? ")

while not (question == "cats" or question == "dogs"):
  question = input("Invalid, please enter cats or dogs: ")

if question == "cats":
  print("Lazy animals for lazy people!")
elif question == "dogs":
  print("Hope you like walking!")