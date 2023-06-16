# Write a program that asks the user to enter their favorite quote, and then prints out the quote score. The quote score is simply the number of spaces in the quote.
# Note: You must use a for loop.

quote = input("Enter your favorite quote: ")
score = 0
for x in quote:
  if x == " ":
    score += 1

print("Your score is " + str(score) + ".")