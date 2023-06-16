def changeVowels(word):
  if word.isupper() == True:
    word = word.casefold()
      
  for x in range(len(word)):
    if word[x] != 'a' or word[x] != 'e' or word[x] != 'i' or word[x] != 'o' or word[x] != 'u':
      word[x] = 'x'  
  
  return word

print(changeVowels('pythagoras'))