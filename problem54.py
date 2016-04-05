#!-*-coding=utf8 -*-

import time


"""
========================
Project Euler Problem 54
=======================
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, 
for example, both players have a pair of queens, then highest cards in each hand are compared 
(see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
	 	2C 3S 8S 8D TD
Pair of Eights
	 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
	 	2C 5C 7D 8S QH
Highest card Queen
	 	Player 1
3	 	2D 9C AS AH AC
Three Aces
	 	3D 6D 7D TD QD
Flush with Diamonds
	 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
	 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
	 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
	 	3C 3D 3S 9S 9D
Full House
with Three Threes
	 	Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""


with open('./Downloads/poker.txt') as data:
    hands=[]
    for line in data:
        hands.append(line.strip('\n\r').split())    


CARD_VALUES = {'2':0 , '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9, 'Q':10, 'K':11, "A":12}
HAND_VALUES = {'high_card':0, 'one_pair':100, 'two_pairs':200, 'three_of_a_kind': 300, 'straight':400, 'flush':500,
                'full_house':600, 'four_of_a_kind':700, 'straight_flush':800, 'royal_flush':900}        
def score_hand(hand):
    cards=[CARD_VALUES[i[0]] for i in hand]
    cards.sort()
    if hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1]:
        if sum(cards)==50:
            return HAND_VALUES['royal_flush']        
        for i in xrange(1,5):
            if cards[i] - cards[i-1] != 1 and len(set(cards)) > 2:
                return HAND_VALUES['flush'] + max(cards)
        else:
            return HAND_VALUES['straight_flush'] + max(cards)
    if len(set(cards))==2:
        for i in cards:
            if cards.count(i)==4:
                return HAND_VALUES['four_of_a_kind'] + i
                
            if cards.count(i)==3:
                return HAND_VALUES['full_house'] + i
    if cards[4]-cards[3]==1 and cards[3]-cards[2]==1 and cards[2]-cards[1]==1 and cards[1]-cards[0]==1:
        return HAND_VALUES['straight'] + max(cards)
    
    if len(set(cards))==3:
        pairs=set()
        for i in cards:
            if cards.count(i)==3:
                return HAND_VALUES['three_of_a_kind'] + i
            if cards.count(i)==2:
                pairs.add(i)
        return HAND_VALUES['two_pairs'] + max(pairs)
    if len(set(cards))==4:
        for i in cards:
            if cards.count(i)==2:
                return HAND_VALUES['one_pair'] + i
    else:
        return HAND_VALUES['high_card'] + max(cards)    
          
def problem54():
    player_one_wins=0          
    for hand in hands:
        if score_hand(hand[:5]) > score_hand(hand[5:]):
            player_one_wins+=1
    return player_one_wins

if __name__=="__main__":
    time1=time.time()
    print problem54()
    time2=time.time()
    print time2-time1
    
