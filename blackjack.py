from deck import Deck
from hand import Hand
startamt = 100.00
valid,playerbust,dealerbust,tie = False, False, False, False
print("Welcome to Blackjack. Your starting amount is $100.")
while True:
    valid,playerbust,dealerbust,tie = False, False, False, False
    while not valid:
        try:
            bet = int(input("How much do you want to bet? "))
            if bet <= 0 or bet > startamt:
                print("Invalid betting amount. Try again")
            else:
                valid = True    
        except:
            print("That is not a number. Try again.")
    print("Shuffling the deck and dealing the cards...")
    deck = Deck()
    deck.shuffle()
    player = Hand(deck)
    dealer = Hand(deck)   
    print(player)
    dealer.printone()
    while not playerbust:
        while True:
            hitres = input("Do you want to hit (h) or stay (s)? ")
            if hitres.lower() == 'h' or hitres.lower() == 's':
                break
            else:
                print("We need an answer...")
        if hitres == 'h':
            player.hit(deck.drawcard())
            print(player)
            dealer.printone()
            playerbust = player.checkbust()
        else:
            break
    if not playerbust:
        print("Now it's the dealer's turn")
        dealer.printdealer()
        while not dealerbust:
            if dealer.getvalue() < player.getvalue():
                print("The dealer will hit again...")
                dealer.hit(deck.drawcard())
                dealer.printdealer()
                dealerbust = dealer.checkbust()
            elif dealer.getvalue == player.getvalue():
                tie = True
                break
            else: 
                print("The dealer stays...")
                break
    if playerbust:
        print(f"You busted! The dealer won {bet} dollar(s)!")
        startamt -= bet
    elif dealerbust:
        print(f"The dealer busted! You won {bet*2} dollar(s)!")      
        startamt += 2*bet
    elif tie:
        print("It's a tie. No money was lost but none was gained either")    
    elif player.getvalue() > dealer.getvalue():
        print(f"Your hand value is higher. You won {bet*2} dollar(s)!")
        startamt += 2*bet
    else:
         print(f"The dealer's hand value is higher. You lost {bet} dollar(s)!")   
         startamt -= bet
    print(f"You now have {startamt} dollars")
    if startamt == 0:
        print("Looks like you've gone bankrupt. Restart the game to try to win more money!")
        break
    replay = input("Do you want to play again? (Enter y/n)") 
    if replay.lower() == 'n':
        break
    del dealer,player,deck
