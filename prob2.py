'''
Write a program that reads a shorthand text description of a playing card and prints the longhand equivalent. The shorthand description is the card's rank (2 through 10, J, Q, K, or A) followed by its suit (C, D, H, or S). You should expand the shorthand into the form "Rank of Suit". You may assume that the user types valid input. Here are two sample executions:
'''

longhand = ""

shorthand = input("Enter a card: ")
value_list = shorthand.split(" ")
rank = value_list[0]
suit = value_list[1]

'''
if rank == "2":
  longhand += "Two of "
elif rank == "3":
  longhand += "Three of "
elif rank == "4":
  longhand += "Four of "
elif rank == "5":
  longhand += "Five of "
elif rank == "6":
  longhand += "Six of "
elif rank == "7":
  longhand += "Seven of "
elif rank == "8":
  longhand += "Eight of "
elif rank == "9":
  longhand += "Nine of "
elif rank == "10":
  longhand += "Ten of "
elif rank == "J":
  longhand += "Jack of "
elif rank == "Q":
  longhand += "Queen of "
elif rank == "K":
  longhand += "King of "
elif rank == "A":
  longhand += "Ace of "


if suit == "H":
  longhand += "Hearts"
elif suit == "C":
  longhand += "Clubs"
elif suit == "D":
  longhand += "Diamonds"
elif suit == "S":
  longhand += "Spades"
'''

# dictionary
ranksDictionary = { "2":"Two of ", "3":"Three of ", "4":"Four of ", "5":"Five of ", "6":"Six of ", "7":"Seven of ", "8":"Eight of ", "9":"Nine of ", "10":"Ten of ", "J":"Jack of ", "Q":"Queen of ", "K":"King of ", "A":"Ace of " }

suitsDictionary = {"H":"Hearts", "D":"Diamonds", "C":"Clubs", "S":"Spades"}

print(ranksDictionary[rank] + suitsDictionary[suit])