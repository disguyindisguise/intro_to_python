
def leapYear(year):
  if year % 4 == 0:
    return True
  elif year % 100 == 0 and year % 400 == 0:
    return True
  elif year % 100 == 0 and year % 400 != 0:
    return False
  else:
    return False


print(leapYear(3000))