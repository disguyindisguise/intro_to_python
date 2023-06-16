import math

def heron(a,b,c):
  s = (a+b+c)/2.0
  return math.sqrt(s*(s-a)*(s-b)*(s-c))


print(heron(3,4,5))