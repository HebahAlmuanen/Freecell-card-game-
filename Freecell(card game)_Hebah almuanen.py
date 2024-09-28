import random

# Define the suits and ranks of a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Define a class for a card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

# Define a class for a deck of cards
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

# Define a class for a Freecell game
class Freecell:
    def __init__(self):
        self.deck = Deck()
        self.columns = [[] for _ in range(8)]
        self.freecells = [[] for _ in range(4)]
        self.foundation_piles = [[] for _ in range(4)]

        # Deal the cards to the columns
        for i in range(8):
            for _ in range(6):
                self.columns[i].append(self.deck.draw())

    def display(self):
        print("Columns:")
        for i, column in enumerate(self.columns):
            print(f"{i+1}: {', '.join(str(card) for card in column)}")

        print("\nFreecells:")
        for i, freecell in enumerate(self.freecells):
            print(f"{i+1}: {', '.join(str(card) for card in freecell)}")

        print("\nFoundation Piles:")
        for i, pile in enumerate(self.foundation_piles):
            print(f"{i+1}: {', '.join(str(card) for card in pile)}")

    def move(self, source, destination):
        # Move a card from one column to another
        if source < 8 and destination < 8:
            card = self.columns[source].pop()
            self.columns[destination].append(card)
        # Move a card from a column to a freecell
        elif source < 8 and destination < 12:
            card = self.columns[source].pop()
            self.freecells[destination-8].append(card)
        # Move a card from a freecell to a column
        elif source < 12 and destination < 8:
            card = self.freecells[source-8].pop()
            self.columns[destination].append(card)
        # Move a card from a column to a foundation pile
        elif source < 8 and destination < 16:
            card = self.columns[source].pop()
            self.foundation_piles[destination-12].append(card)

def main():
    game = Freecell()
    while True:
        game.display()
        source = int(input("Enter the source column/freecell (1-12): ")) - 1
        destination = int(input("Enter the destination column/freecell (1-16): ")) - 1
        game.move(source, destination)

if __name__ == "__main__":
    main()