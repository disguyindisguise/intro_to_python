# Write a python program that prompts a PowerShell user for the number of people eating and outputs the following recipe for soup with the ingredients adjusted for the number of people eating. Ingredients for 1 person are:

''' 
8 ounces of broth
3 chopped celery sticks
2 chopped carrots 

party_size = int(input("How many people are eating? "))

broth = 8
celery  = 3
carrots = 2

print("Ingredients are: ")
print(str(broth * party_size) + " ounces of broth")
print(str(celery * party_size) + " chopped celery sticks")
print(str(carrots * party_size) + " chopped carrots")
'''


widget = int(input("How many widgets are you building? "))

things = 3
doohickies  = 2
nails = 4

print("You will need: ")
print(str(things * widget) + " thing-ama-bobs")
print(str(doohickies * widget) + " doohickies")
print(str(nails * widget) + " nails")