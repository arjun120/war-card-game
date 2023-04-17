from deck import Deck

class Player:
    """
    The Player class is used to instantiate players who end up playing the game. Each player gets
    a deck of cards to which they can add or remove cards as they seem fit.
    """

    def __init__(self, name:str, deck:Deck):
        self.deck = deck
        self.name = name
    
    def play(self):
        # This method removes the first card from the players deck and puts it in play.
        return self.deck.pop()
    
    def addToDeck(self, cards):
        # This method is used to add a set of cards to the player's deck of cards.
        self.deck.extend(cards)

    def getDeckSize(self):
        # This method returns the count of number of cards in the player's deck.
        return self.deck.getDeckSize()