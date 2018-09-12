from random import shuffle
class Deck:
    suits = ["Hearts","Diamonds", "Spades", "Clubs"]
    cardsinsuit = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
    
    def __init__(self):
        self.deck = []
        for suit in Deck.suits:
            for card in Deck.cardsinsuit:
                self.deck.append((suit,card)) 
    def shuffle(self):
        shuffle(self.deck)         
    def drawcard(self):
        return self.deck.pop()
    def __str__(self):
        return str(self.deck)
    def __len__(self):
        return len(self.deck)