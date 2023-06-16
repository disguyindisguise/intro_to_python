mkdir# program that will me which number are divisible when a list is entered

'''a = [1, 2, 3]
b = [7, 8, 9]
c = [ x+y for x in a for y in b]
print(c)'''

list_1 = input("Enter first space-separated numbers: ")
list_2 = input("Enter second space-separated numbers: ")


a = list_1.split()

b = list_2.split()
print("First list is " + str(a))
print("Second list is " + str(a))

c = [ int(x) % int(y) for x in b for y in a]
# print(c) if you need to see the modulus
count = 0
for x in c:
  if x == 0:
    count += 1
print("There are " + str(count) + " divisibles numbers.")


d = [ int(x) % int(y) for x in b for y in a]
  print(x)
  print(y)

'''
d = []

for x in b and for y in a:
  e = int(x) % int(y)
  if e == 0:
    d += x,y
print(d)
  '''