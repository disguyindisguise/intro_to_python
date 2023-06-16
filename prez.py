# how many D prez and R prez

file = open("prez.txt")
text = file.read()
lines = text.split("\n")

d = 0
r = 0
length_list = []
longest_name = ""

for line in lines:
  line_list = line.split(":")
  party = line_list[1]
  name = len(line_list[0])
  if party == "D":
    d += 1
  if party == "R":
    r += 1
  length_list += [name]

for line in lines:
  line_list = line.split(":")
  name = len(line_list[0])
  if name == max(length_list):
    longest_name = line_list[0]

print("Democrats: " + str(d))
print("Republicans: " + str(r))
print("The longest name is " + str(max(length_list)) + " characters, which is president " + longest_name)
