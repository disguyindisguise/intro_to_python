cities = ["boston", "los angeles", "atlanta", "miami", "new york city"]

scores = [4.0, 4.5, 5, 4.5, 4.9]

reviews = ["great place for lobster", 
          "great weather!",
          "best place in the world",
          "fun place",
          "center of the world!"]

for x in range(5):
  print("For city " + cities[x] + " the score is " + str(scores[x]))

best_city = ""
best_score = 0
for city,score in zip(cities,scores):
  print("For city " + city + " the score is " + str(score))
  if score > best_score:
    best_score = score
    best_city = city
    
print("The best city is " + best_city + " and the score is " + str(best_score))

for city,score,review in zip(cities,scores,reviews):
  print(city, score, review)


