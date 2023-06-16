def dropThird(num_list):
  third = num_list[2]
  new_list = num_list.remove(third)
  return new_list

print(dropThird([10, 40, 100, 30, 80])) # should return [10, 40, 30, 80]
print(dropThird([50, 75, 25, 10, 5, 80, 100, 12])) # should return [50, 75, 10, 5, 80, 100, 12]