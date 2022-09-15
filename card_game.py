#Ethan Clark & Emory Miller
#Lab section 21

from cisc106 import *
import random 

class Card:
    """model for a card
    attributes:
        number: card number, with jack=11, queen=12, king=13, ace=14 (int)
        suit: "S", "H", "D", or "C" (str)"""  
    number=0
    suit="none"

class Hand:
    """model for a hand of 3 cards
    attributes: pcard1, pcard2, pcard3: empty values"""
    card1=None
    card2=None
    card3=None

Player=Hand()
Dealer=Hand()
Player.card1=Card()
Player.card2=Card()
Player.card3=Card()
Dealer.card1=Card()
Dealer.card2=Card()
Dealer.card3=Card()

class Balance:
    """model for player's stake
    attributes:
        amount: the dollars the player has (int)"""
    amount=100

def score(diff):
    """adds or subtracts inputted amount from Balance.amount
    parameters: diff (int)
    returns: none""" 
    Balance.amount+=diff
    if diff<0:
        print("You lose",abs(diff),"dollars!")
    else:
        print("You win",abs(diff),"dollars!")
    print("You now have",Balance.amount,"dollars.")
    #Not sure if assertEqual will work for this function... otherwise it can be tested by
    #calling it with an integer argument

def main():
    """initiates the game.
    parameters: n/a
    returns: print statements"""
    print("The ante is 10.")
    play_round()
    print("Goodbye!")
    #can be tested by commenting out play_round and running

def play_round():
    """initiates a round
    parameters: n/a
    returns: print statements"""
    print("You have",Balance.amount,"dollars.")
    print("Your hand is:")
    deal(Player)
    check=0
    while check!="p" and check!="f":
        check=input("Play or fold (p/f)?")
    if check=="f":
        score(-10)
    else:
        print("Dealer hand is:")
        deal(Dealer)
        dealer_forp()
    keep_playing()
    #can be tested by commenting out dealPlayer(), dealDealer(), score(-10),
    #keep_playing(), and running

def keep_playing():
    """stops play/initiates new round depending on player input"""
    resume=0
    while resume!="y" and resume!="n":
        resume=input("Keep playing (y/n)?")
    if resume=="y":
        play_round()
    else:
        return
    #can be tested by running the function to see if it calls the function play_round
    #if typing y, or stops by typing n.

def deal(thing):
    """generates new values for hand instances
    parameters: none
    returns: none"""
    thing.card1.number=random.randint(2,14)
    thing.card2.number=random.randint(2,14)
    thing.card3.number=random.randint(2,14)
    thing.card1.suit=random.randint(1,4)
    thing.card2.suit=random.randint(1,4)
    thing.card3.suit=random.randint(1,4)
    show_card(thing)
    #assertEqual will not work for this function, but it can be tested by creating an
    #instance of the Hand class, calling the function with the Hand instance as the
    #argument and then printing the attributes of the Hand instance.


def conv_numb(numb):
    """converts card numerical value to face value.
    parameters: numb (int)
    returns: numb (str)
    """
    if numb>10:
        ret=str(numb)
    if numb==11:
        ret="J"
    elif numb==12:
        ret="Q"
    elif numb==13:
        ret="K"
    elif numb==14:
        ret="A"
    else:
        ret=str(numb)
    return ret

#assertEqual(conv_numb(11), "J")
#assertEqual(conv_numb(12), "Q")
#assertEqual(conv_numb(13), "K")
#assertEqual(conv_numb(4),"4")

def conv_suit(suit):
    """ converts the numerical representation of a suit to
            a string value recognizable by the user.
    parameters: integer
    returns: suit (str)
    """
    if suit==1:
        suit="S"
    elif suit==2:
        suit="H"
    elif suit==3:
        suit="D"
    else:
        suit="C"
    return suit

#assertEqual(conv_suit(1), "S")
#assertEqual(conv_suit(2), "H")
#assertEqual(conv_suit(3), "D")
#assertEqual(conv_suit(4), "C")

def show_card(thing):
    """orders and then prints the cards in the players hand
    parameters: Player; instance of Hand
    returns: none """
    order_hand(thing)
    card1=(conv_numb(thing.card1.number)+conv_suit(thing.card1.suit))
    card2=(conv_numb(thing.card2.number)+conv_suit(thing.card2.suit))
    card3=(conv_numb(thing.card3.number)+conv_suit(thing.card3.suit))
    print(card1,card2,card3)
    #to test, can call the function with a player instances as the argument, and see if it prints
    #the right card instance with the correct value. 

def dealer_forp():  
    """decides whether dealer will fold or play
    parameters: n/a
    returns: boolean"""
    if hand_points(Dealer)<1000 and Dealer.card1.number<12:
        print("Dealer folds.")
        score(+20)          
    else:
        if higher_hand(Player, Dealer)==True:
            score(+20)
        else:
            score(-20)
    #can test this by calling dealer and player instances of hand as well as a score instance of balance
    # and declaring values for them, then running the function. 

def order_hand(thing):
    """orders the player's hand from highest to lowest
    parameters: Player, a Hand instance
    returns: n/a"""
    if thing.card1.number<thing.card2.number:
        thing.card1.number, thing.card2.number = thing.card2.number, thing.card1.number
    if thing.card2.number<thing.card3.number:
        thing.card2.number, thing.card3.number = thing.card3.number, thing.card2.number
    if thing.card1.number<thing.card2.number:
        thing.card1.number, thing.card2.number = thing.card2.number, thing.card1.number
    #can test this by making instances of hand, filling out attributes, and then running the function
    #making sure that they come out in the intended order.

def higher_hand(hand1, hand2):
    """evaluates 2 hands and returns True if first is higher, False otherwise
    parameters: n/a
    returns: boolean"""
    if hand_points(hand1)>hand_points(hand2):
        return True
    else:
        return False
    #Can test this by playing the game, and ensuring that the winner does in fact
    #have a winning hand. 

def hand_points(thing):
    """returns point value corresponding to hand rank out of all possible hands
    parameters: Player, instance of class Hand
    returns: int"""
    straight_flush=0
    three_kind=0
    straight=0
    flush=0
    pair=0
    if thing.card1.number==thing.card2.number:
        pair=1
        if thing.card2.number==thing.card3.number:
            three_kind=1
    if thing.card1.suit==thing.card2.suit and thing.card2.suit==thing.card3.suit:
        flush=1
    if (thing.card1.number==(thing.card2.number + 1) and
        thing.card2.number==(thing.card3.number +1)):
        straight=1
    if flush==1 and straight==1:
        straight_flush=1
    return_value=(225*thing.card1.number + 15*thing.card2.number + thing.card3.number +
                  1000*pair+10000*flush+100000*straight+
                  1000000*three_kind+10000000*straight_flush)
    return return_value
    #Can test by creating player hand instances and running the function. 

