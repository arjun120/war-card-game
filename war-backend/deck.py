from card import Card
import random

class Deck:
    """
    This represents a set of cards commonly referred to as a deck. Each deck can be split evenly to 
    distribute among players. Since a deck consists of multiple cards, either a single card can be 
    removed from it to be put in play, or multiple cards can added to the deck. 
    """

    def __init__(self, cards):
        self.cards = cards

    def split(self):
        # A deck is made of multiple cards. To be split into halves, the cards in the deck are shuffled
        # and distributed evenly. 
        random.shuffle(self.cards)
        return (Deck(self.cards[:26]), Deck(self.cards[26:]))
    
    def pop(self):
        # This method removes the first card from the deck of cards.
        return self.cards.pop(0)
    
    def extend(self, cards):
        # This method adds a given number of cards at the end of the given deck of cards.
        self.cards.extend(cards)
    
    def display(self):
        # This method displays all the cards in the deck as a list of cards.
        cards = []
        for card in self.cards:
            cards.append(card.display())
        return cards

    def getDeckSize(self):
        # This method is used to get the current size of the deck
        return len(self.cards)