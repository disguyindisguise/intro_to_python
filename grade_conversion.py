# Write a program that prompts the user for their grade as a percentage, and prints out the corresponding letter grade. Assume A>=90, B>=80, C>=70, D>=60, otherwise F.

'''
grade = float(input("Enter percent grade: "))

if grade >= 90:
  print("An " + str(grade) + " is a A.")
if grade >= 80 and grade < 90:
  print("An " + str(grade) + " is a B.")
if grade >= 70 and grade < 80:
  print("An " + str(grade) + " is a C.")
if grade >= 60 and grade < 70:
  print("An " + str(grade) + " is a D.")
if grade < 60:
  print("An " + str(grade) + " is a F.")
'''

grade = float(input("Enter percent grade: "))

if grade > 0 and grade < 101:
  if grade >= 90:
    print("An " + str(grade) + " is a A.")
  elif grade >= 80:
    print("An " + str(grade) + " is a B.")
  elif grade >= 70:
    print("An " + str(grade) + " is a C.")
  elif grade >= 60:
    print("An " + str(grade) + " is a D.")
  else:
    print("An " + str(grade) + " is a F.")
else:
  print("Grade needs to be between 0 and 100!")