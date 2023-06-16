num = input("Enter Number: ")

count = 0

for x in num:
  if int(x) >= 4:
    count += 1

print("That number has " + str(count) + " digits greater than 4.")
  