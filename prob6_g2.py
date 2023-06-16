# name Purvi Shah

'''
Write a complete program named CollegeAdmit that uses a raw_input() to read user input for a student's grade point average and SAT exam score, and uses these values to decide whether the student is admitted to the college. A GPA below 1.8 will cause the student to be rejected; an SAT score below 900 will also cause a rejection. Otherwise the student is accepted. If both the GPA and the SAT score are too low, print the message about the GPA being too low. Your output should match the following examples:
College admission program
What is your GPA? 3.2
What is your SAT score? 1280
You were accepted!

College admission program
What is your GPA? 3.95
What is your SAT score? 860
Your SAT score is too low.

College admission program
What is your GPA? 1.4
What is your SAT score? 1590
Your GPA is too low.
'''

gpa = float(input("What is Yout GPA: "))
sat = float(input ("What is Your SAT Score? "))

if gpa <= 1.8:
  print("Your GPA is too low.")
if sat  <= 900:
  print("Your SAT score is too low.")
else:
  print("You were accepted!")

'''


