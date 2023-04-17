from deck import Deck
from player import Player
from card import Card

class War:
    """
    This class is used to instantiate a war game between two players. Each player receives a deck
    of cards they get to play with.
    """

    def __init__(self):
        # This method is used to initialize the deck of cards with 52 playing cards.
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        faceValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace', 'J', 'Q','K']
        placeValues = [placeValue for placeValue in range(1, 14)]
        valuesDict = dict(zip(faceValues, placeValues))
        deck = [Card(faceValue, valuesDict[faceValue], suit) for faceValue in faceValues for suit in suits]
        self.gameDeck = Deck(deck)
    
    def simulate(self, playerName1, playerName2):
        # This method simulates the game of war. The deck is first split among the two players playing 
        # the game.
        deck1, deck2 = self.gameDeck.split()

        self.player1 = Player(playerName1, deck1)
        self.player2 = Player(playerName2, deck2)
        
        # The backlog stores the pile of cards set aside during the war phase.
        backlog = []
        finalResults = []

        # There is a possibility of the game proceeding to be played infinitely. To avoid this,
        # there is check to see if the number of cards in alternate rounds for a player remains
        # the same for a threshold number of rounds. In this case the game is declared to be a draw.
        # The threshold is arbitrarily initialized to 1000.
        player1PreviousDeckCount = 26
        player2PreviousDeckCount = 26
        toggleCount = 0
        iteration = 0
        round = 1
        while True:

            if iteration % 2 == 0:
                if player1PreviousDeckCount == self.player1.getDeckSize() and player2PreviousDeckCount == self.player2.getDeckSize():
                    toggleCount += 1
                else:
                    toggleCount = 0
                
                player1PreviousDeckCount = self.player1.getDeckSize()
                player2PreviousDeckCount = self.player2.getDeckSize()

            if self.player1.getDeckSize() == 0 or self.player2.getDeckSize() == 0:
                    return finalResults, (playerName1 + " won", 0) if self.player1.getDeckSize() != 0 else (playerName2 + " won", 1)
            if toggleCount >= 1000:
                return finalResults, ("The game resulted in a draw", -1)
        
            card1 = self.player1.play()
            card2 = self.player2.play()

            comparison = card1.compare(card2)

            finalResults.append({"comparison": comparison, "round": round, "player1CardsCount": str(self.player1.getDeckSize()),"player2CardsCount": str(self.player2.getDeckSize()), "player1Card": card1.display(), "player2Card": card2.display()})

            if comparison == 1:
                
                backlog.extend([card1, card2])
                self.player1.addToDeck(backlog)
                round += 1
                backlog = []
            elif comparison == -1:
                backlog.extend([card1, card2])
                self.player2.addToDeck(backlog)
                round += 1
                backlog = []
            else:
                if self.player1.getDeckSize() == 0 or self.player2.getDeckSize() == 0:
                    return finalResults, (playerName1 + " won", 0) if self.player1.getDeckSize() != 0 else (playerName2 + " won", 1)
                if toggleCount >= 1000:
                    return finalResults, ("The game resulted in a draw", -1)
                
                foldedCard1 = self.player1.play()
                foldedCard2 = self.player2.play()

                finalResults.append({"comparison": comparison, "round": round, "player1CardsCount": str(self.player1.getDeckSize()),"player2CardsCount": str(self.player2.getDeckSize()), "player1Card": "Folded Card", "player2Card": "Folded Card"})
                backlog.extend([card1, card2, foldedCard1, foldedCard2])

            iteration += 1

        