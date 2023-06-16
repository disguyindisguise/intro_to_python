
# Write a Python program that asks for your name and your friend's name.

# It should print the longer name (more characters in the name) and say "You Win" if your name is longer or "Your Friend Wins" if your friend's name is longer.

a = input("First name: ")
b = input("Second name: ")

if len(a) > len(b):
  print("str(a)" + " wins!")

if len(b) > len(a):
  print(str(b) + " wins!")