def printTriangleType(a,b,c):
  if a == b and b == c and c == a:
    print("equilateral")
  elif a != b and b != c and c != a:
    print("scalene")
  else:
    print("isoceles")


printTriangleType(5, 7, 7)
printTriangleType(6, 6, 6)
printTriangleType(5, 7, 8)
printTriangleType(12, 18, 12)