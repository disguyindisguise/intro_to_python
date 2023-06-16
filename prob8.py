
def pay(rate,hours):
  if hours <= 8:
    return rate * hours
  else: 
    return (rate * 8) + (rate*1.5 * (hours - 8))


print(pay(100,10))
print(pay(25,7))

