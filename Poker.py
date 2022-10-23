#  File: Poker.py

#  Description: This program automates poker games for 2-6 players and outputs
# each players hand and the winner of each game. 

#  Student's Name: Michael Pham

#  Student's UT EID: mp46987

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number:  51125

#  Date Created: 2/7/2022

#  Date Last Modified:
# A5: To be effective, need to know how to represent coordinate system using integer 

import sys, random

class Card (object):
    
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('C', 'D', 'H', 'S')
    
    #Constructor
    
    #The rank is a number, the Suit is a letter
    def __init__(self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12
        
        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self,suit = 'S'
            
        #Override the str function
        #Strign representation of a Card Object
        
    def __str__(self):
        if (self.rank == 14):
            rank = 'A'
        elif(self.rank == 13):
            rank = 'K'
        elif(self.rank == 12):
            rank = 'Q'
        elif(self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit
    
    #Equality tests
    def __eq__(self, other):
        return self.rank == other.rank
    
    def __ne__(self, other):
        return self.rank != other.rank
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __le__(self, other):
        return self.rank <= other.rank
    
    def __gt__(self, other):
        return self.rank > other.rank
    
    def __ge__(self, other):
        return self.rank >= other.rank
    
    #We have achieved in telling python what a card is thus far
    #Now must tell python what a deck is 
        
class Deck(object):
    #constructor 
    def __init__(self, num_decks = 1):
        self.deck = []
        for x in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)
                    
    #Shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)
        
    #Deal a card
    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Poker(object):
    #constructor
    def __init__(self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hands = []
        self.numCards_in_Hand = num_cards

            
        
        #deal all the hands
        #We are going to modify the code, to where it gives one card at a time instead of all 5
        
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.player_hands.append(hand)
            
    #Simulate the play of the game
    def play(self):
        #sort the hands of each playaer and print the hand
        for i in range(len(self.player_hands)):
            sorted_hand = sorted (self.player_hands[i], reverse = True)
            #This above line of code works because of the equality tests earlier
            self.player_hands[i] = sorted_hand
            hand_str = '' 
            #Above starts a string representation of a hand
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Card Hand ' + str(i + 1) + ': ' + hand_str)
        
        print()
        
        #This establishes the points for the types of hands
        royalflush = 10
        straightflush = 9
        fourkind = 8
        fullhouse = 7
        flush = 6
        straight = 5
        threekind = 4
        twopair = 3
        onepair = 2
        highcard = 1
            
           #Determine the type of hand
        hand_type = []
        hand_points = []
        type_and_points = []
           #Determine the winner
           
           #This determines what type of hand each is and calls back the amount of points won from the functions
        for x in range (len(self.player_hands)):
            if self.is_royal(self.player_hands[x]) != 0:    
                hand_type.append(royalflush)
                hand_points.append(self.is_royal(self.player_hands[x]))
                print("Player", str(x + 1) + ": Royal Flush")
            elif self.is_straight_flush(self.player_hands[x]) != 0:    
                hand_type.append(straightflush)
                hand_points.append(self.is_straight_flush(self.player_hands[x]))
                print("Player", str(x + 1) + ": Straight Flush")  
            elif self.is_four_kind(self.player_hands[x]) != 0:    
                hand_type.append(fourkind)
                hand_points.append(self.is_four_kind(self.player_hands[x]))
                print("Player", str(x + 1) + ": Four of a Kind") 
            elif self.is_full_house(self.player_hands[x]) != 0:    
                hand_type.append(fullhouse)
                hand_points.append(self.is_full_house(self.player_hands[x]))
                print("Player", str(x + 1) + ": Full House")
            elif self.is_flush(self.player_hands[x]) != 0:    
                hand_type.append(flush)
                hand_points.append(self.is_flush(self.player_hands[x]))
                print("Player", str(x + 1) + ": Flush")  
            elif self.is_straight(self.player_hands[x]) != 0:    
                hand_type.append(straight)
                hand_points.append(self.is_straight(self.player_hands[x]))
                print("Player", str(x + 1) + ": Straight")  
            elif self.is_three_kind(self.player_hands[x]) != 0:    
                hand_type.append(threekind)
                hand_points.append(self.is_three_kind(self.player_hands[x]))
                print("Player", str(x + 1) + ": Three of a Kind")
            elif self.is_two_pair(self.player_hands[x]) != 0:    
                hand_type.append(twopair)
                hand_points.append(self.is_two_pair(self.player_hands[x]))
                print("Player", str(x + 1) + ": Two Pair")
            elif self.is_one_pair(self.player_hands[x]) != 0:
                hand_type.append(onepair)
                hand_points.append(self.is_one_pair(self.player_hands[x]))
                print("Player", str(x + 1) + ": One Pair")
            else:
                hand_type.append(highcard)
                hand_points.append(self.is_high_card(self.player_hands[x]))
                print("Player", str(x + 1) + ": High Card")
                
        
        #This reads a tuple of the hand type, points, and player
        for x in range(0, len(self.player_hands)):     
            type_and_points.append((hand_type[x], hand_points, x + 1))

        print()       
        
        
        print(type_and_points)
        top_scores = sorted(type_and_points, key = lambda hand_type : hand_type[1], reverse = True)
        amount_of_top_scores = 0
        
        for x in range(1, len(top_scores)):
            if top_scores [x][0] == [0][0]:
                amount_of_top_scores += 1
            else:
                break
        if amount_of_top_scores == 0:
            print('Player', str(top_scores[0][2]), 'wins') #Prints winner
        else:
            for x in range(amount_of_top_scores + 1):
                print('Player', str(top_scores[x][2]), 'ties.') #Prints ties
        
            
    
    
    
           
    def is_high_card(self, hand):
        
        
        #High Card value 
        
        highest_value = 0
        for x in range(len(hand)):
            if highest_value <= hand[x].rank:
                highest_value = hand[x].rank
        #Ordering... lol i forgot about the initial order initially so I ended up doing this. 
        
        first = hand[0].rank
        second = hand[1].rank
        third = hand[2].rank
        fourth = hand[3].rank
        fifth = hand[4].rank
        
        hand_value = 15 ** 5 + first * 15 ** 4 + second * 15 ** 3 + third * 15 ** 2 + fourth * 15 + fifth, 'High Card'
        return hand_value
        
    
    def is_one_pair(self, hand):

        pair_exists = False
        for x in range (len(hand) - 1):
            if (hand[x].rank == hand[x + 1].rank):
                hand.insert(0, hand.pop(x))
                hand.insert(1, hand.pop(x + 1))
                pair_exists = True
                break
            #Tests to see if there are 2 matching cards
            
        if pair_exists == True:
            return 2 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'One Pair'
            
        return 0, ''
        
    
    def is_two_pair(self, hand):
        
        #2 Pairs
        matcher= []
        for x in range(len(hand)):
            if hand[x].rank not in matcher:
                matcher.append(hand[x].rank)
            else:
                continue
        if len(matcher) != 3:
            return 0, ''
        else:
            return 3 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'Two Pair'
        
    
    def is_three_kind(self, hand):
        
        #
        for x in range(len(hand) - 1):
            if hand[x].rank == hand[x + 1].rank: #Testing is adjacent cards are equal
                if (x + 2 < len(hand) - 1):
                    if (hand[x + 1].rank == hand [x + 2].rank):
                        return 4 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'Three of a Kind'
            else:
                continue
        return 0, ''
    
    
    def is_straight(self, hand):
        
        sequence_of_rank = True #Starts as default 
        for x in range (len(hand) - 1):
            sequence_of_rank = sequence_of_rank and (hand[x].rank == hand[x + 1].rank + 1)  #Tests to see if next cards is 1 off
        if sequence_of_rank == True:
            return 5* 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'Straight'
        else:
            return 0, ''
        
    
    def is_flush(self, hand):
        
        matching_suit = True 
        for x in range(len(hand) - 1):
            matching_suit = matching_suit and (hand[x].suit == hand[x + 1].suit) #Pretty much similar to straight but instead we test suit and do not incremenent suit value
        
        if matching_suit == True:
            return 6 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'Flush'
        return 0, ''

        
    def is_full_house(self, hand):
        
        index = 0
        three_kind = False
        two_kind = False
        #Sets the rules for what afull house it 
        
        while index < (len(hand) - 1):
            #Tests the 3 of a kind with the 2 equalling sets to make 3 total
            if (index < len(hand) - 2) and (hand[index].rank == hand[index + 1].rank) and (hand[index + 1].rank == hand[index + 2].rank):
                three_kind = True
                index += 3
            #Tests to see if remaining 2 cards has a pair
            elif (hand[index].rank == hand[index + 1].rank):
                two_kind = True
                index += 2
            else:
                index += 1
                
        if three_kind == True and two_kind == True:
                return 7 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'Full House'
            
        return 0, ''
        
        
   
        
    def is_four_kind(self, hand):
        
        #Four of a kind being true or false 
        is_4_k = False
        for x in range(0, len(hand) - 3):
            if hand[x].rank == hand[x + 3].rank:
                hand.insert(0, hand.pop (x))
                hand.insert(1, hand.pop (x + 1))
                hand.insert(2, hand.pop (x + 2))
                hand.insert(3, hand.pop (x + 3))
                is_4_k = True
        
        if is_4_k == False:
            return 0, ''
        if is_4_k == True:
            return 8 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'Four of a Kind'

        
        
    def is_straight_flush(self, hand):
        
        #Amalgamates the straight and flush functions
        is_s_f = False
        straight_count = 0
        equal_suit = True
        for x in range(len(hand) - 1):
            equal_suit = equal_suit and (hand[x].suit == hand[x + 1].suit)
        if equal_suit != True:
            return 0, ''   
        
        for x in range(len(hand) - 1):
            if hand[x + 1].rank == hand[x].rank -1:
                straight_count += 1
            if straight_count == 4:
                is_s_f = True
                
        if is_s_f == False:
            return 0, ''
        if is_s_f == True:
            return 9 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'Straight Flush'
        
        

    
    def is_royal(self, hand):
        
        equal_suit = True
        for x in range(len(hand) - 1):
            equal_suit = equal_suit and (hand[x].suit == hand[x + 1].suit)
        if equal_suit != True:
            return 0, ''   
        
        sequenced = True
        for x in range(len(hand)):
            sequenced = sequenced and (hand[x].rank == 14 - x)
        if sequenced == True:
            return 10 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + hand[3].rank * 15 + hand[4].rank, 'Royal Flush'
        else:
            return 0, ''
    
    

        

                
def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()   
if __name__ == "__main__":
  main()    

            
            
        
                
                
                
    
    
    

        
    
    
                    



        
