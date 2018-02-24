# Create and shuffle a deck of cards
import random
#
deckOfCards = []
suits       = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
valueList   = ['Ace', '2', '3', '4', '5', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
#
# deckOfCards = ['Ace of Spades', "10 of Hearts", "Jack of Diamonds"]
for suit in suits:

    for value in valueList:
        deckOfCards.append(value + " " + suit)

print "*** Printing the new deck of cards ***"
for card in deckOfCards:
    print card




# shuffle the deck test
# testDeck = ['aaa','bbb', 'ccc']
# random.shuffle(testDeck)
# for card in testDeck:
#     print(card)
# # Shuffle the deck
# print " Size of Deck of cards: ", len(testDeck)


print "*** Printing the shuffled deck of cards ***"
random.shuffle(deckOfCards)
for card in deckOfCards:
    print card






