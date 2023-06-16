
# fibonnacci number
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 
# 1/1 , 2/1, 3/2,  5/3, 8/5, 13/8, 87/54, ...

first = 1
second = 1

n = 3
target = 20
while n <= target:
  current = first + second
  print("The " + str(n) + " th fibonnacci number is " + str(current))
  first = second
  second = current
  n += 1

