'''N = 10
series = []
series_sum = []
for x in range(N+1):
  series += [x]

mean = sum(series)/N
for x in series:
  inner_sum = (x - mean)**2
  series_sum += [inner_sum]
print(mean)
print(sum(series_sum))
print(series)
print(series_sum)'''

def sumrange(num):
  series = []
  for x in range(num):
    series += [x+1]
  return str(sum(series)) + "\n" + str(series)

print(sumrange(15))


  

