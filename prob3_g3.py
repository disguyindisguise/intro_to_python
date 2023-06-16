# Names: Ian Sinza, Purvi Shah

'''Write a program that prompts the user for a month and a day.

 

Assume that months are specified as an integer between 1 and 12 (1 for January, 2 for February, and so on) and that the day of the month is a number between 1 and 31.

 

If the date falls between 12/16 and 3/15, you should print "Winter". If the date falls between 3/16 and 6/15, you should print "Spring". If the date falls between 6/16 and 9/15, you should print "Summer". And if the date falls between 9/16 and 12/15, you should print "Fall".'''


date = input("What is the date (Month/Day)? ")
date_list = date.split("/")

month = int(date_list[0])
day = int(date_list[1])

if (month == 12 and day >= 16) or (month == 1 or month == 2) or (month == 3 and day <= 15):
  print("Winter")
elif (month == 3 and day >= 16) or (month == 4 or month == 5) or (month == 6 and day <= 15):
  print("Spring")
elif (month == 6 and day >= 16) or (month == 7 or month == 8) or (month == 9 and day <= 15):
  print("Summer")
else:
  print("Fall")


  