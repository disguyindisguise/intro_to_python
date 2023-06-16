'''
Prompt the user to enter a string and print whether the entered string is a palindrome (i.e., reads the same forwards as it does backwards, like "abba" or "racecar").
'''

word = input("Enter word: ")

backwards = ""
for x in word:
  backwards = x + backwards

if backwards == word:
  print("palindrome!")
else:
  print("not a palindrome!")