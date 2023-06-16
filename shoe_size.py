size = float(input("Enter your shoe size: "))

if size >= 10:
  print("You should buy large sized socks.")
elif size >= 5 and size < 10:
  print("You should buy medium sized socks.")
elif size >= 0 and size < 5:
    print("You should buy small sized socks.")
