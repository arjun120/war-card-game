class Card:
    """
    The Card class is used to instantiate objects which are essentially cards part of the game.
    Each card has faceValue, that is seen on the card, placeValue or the value used for comparisons 
    and finally the suit it belongs to.
    """

    def __init__(self, faceValue:str, placeValue:int, suit:str):
        self.faceValue = faceValue
        self.placeValue = placeValue
        self.suit = suit

    def compare(self, card):
        # This is a method to compare values on two cards. The place values of the cards need to
        # be compared to move forward in the game.
        if self.placeValue > card.placeValue:
            return 1
        elif self.placeValue < card.placeValue:
            return -1
        return 0
    
    def display(self):
        # This method just returns a formatted string which indicates the face value of the card.
        return self.faceValue + " of " + self.suit
    





