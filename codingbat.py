getsum

return sum(range(1,N+1))





def getSumOfSquares(N):
  squares = []

  for x in range(N+1):
    squares += [x**2]

  return sum(squares)

# or instead list comprehension

s = [ x**2 for x in range(1, N+1) ]
return sum(s)





def getSumOfOdds(N):
  series = []
  for x in range(1, N+1, 2):
    series += [x]
  return sum(series)

def getSumOfOdds(N):
  s = range(1, N+1, 2)
  return sum(s)

def getSumOfOdds(N):
  s = [ x for x in range(1, N+1) if x%2 ==1 ]
  return sum(s)