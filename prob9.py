# Please enter your full name: Sammy Davis
# Your name in reverse order is Davis, Sammy

name = input("Please enter your full name: ")
name_list = name.split(" ")
print("Your name in reverse order is " + name_list[1] + ", " + name_list[0])

print(f"Your name in reverse order is {name_list[1]}, {name_list[0]}")