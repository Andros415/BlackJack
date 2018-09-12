class Hand:
    def __init__(self,deck):
        self.hand = []
        self.hand.append(deck.drawcard())
        self.hand.append(deck.drawcard())
        self.value = 0
    def hit(self,card):
        self.hand.append(card)
    def getvalue(self):
        self.value = 0
        for (a,b) in self.hand:
            if b == "Jack" or b == "Queen" or b == "King":
                self.value += 10
            elif b == "Ace":
                if (self.value + 11) > 21 :
                    self.value += 1
                else:
                    self.value += 11
            else:    
                self.value += int(b)
        return self.value  
    def checkbust(self):
        return self.value > 21
    def printone(self):
        print(f"The dealer has a(n) {self.hand[0][1]} of {self.hand[0][0]} and one face down card")
    def printdealer(self):
        s = f"The dealer has {len(self.hand)} cards in his/her hand. The cards he/she has are: \n"
        for (a,b) in self.hand:
            s += f"The {b} of {a} \n"
        s += f"Total value of hand: {self.getvalue()}"
        print(s)
    def __str__(self):
        s = f"You have {len(self.hand)} cards in your hand. The cards you have are: \n"
        for (a,b) in self.hand:
            s += f"The {b} of {a} \n"
        s += f"Total value of hand: {self.getvalue()}"
        return s    
    def __len__(self):
        return len(self.hand)
