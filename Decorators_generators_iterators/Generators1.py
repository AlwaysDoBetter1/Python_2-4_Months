'''
Implement a generator function card_deck() that takes one argument:

suit - one of four card suits: spades, clubs, diamonds, hearts
The function should return a generator that cyclically generates a deck of playing cards without suit. Each card must
be a string in the following format:

<value> <suit>
For example, 7 of spades, jack of clubs, queen of diamonds, king of hearts, ace of spades.

Note 1. Cards generated by the iterator must be arranged first by suit, then by value.

Note 2. Seniority of suits in ascending order: spades, clubs, diamonds, hearts. The seniority of cards in
suit in ascending order: two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace.
'''

def card_deck(suit):
    suits = ["spades", "clubs", "diamonds", "hearts"]
    suits.remove(suit)
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    while True:
        for s in suits:
            for r in ranks:
                yield f"{r} of {s}"

# check
generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)

# output:
# 2 of spades, 3 of spades, 4 of spades, 5 of spades, 6 of spades, 7 of spades, 8 of spades, 9 of spades, 10 of spades,
# Jack of spades, Queen of spades, King of spades, Ace of spades, 2 of clubs, 3 of clubs, 4 of clubs, 5 of clubs,
# 6 of clubs, 7 of clubs, 8 of clubs, 9 of clubs, 10 of clubs, Jack of clubs, Queen of clubs, King of clubs,
# Ace of clubs, 2 of diamonds, 3 of diamonds, 4 of diamonds, 5 of diamonds, 6 of diamonds, 7 of diamonds, 8 of diamonds,
# 9 of diamonds, 10 of diamonds, Jack of diamonds, Queen of diamonds, King of diamonds, Ace of diamonds, 2 of hearts
