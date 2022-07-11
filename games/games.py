# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 12:38:45 2022

@author: Tristen
"""
import random
import pdb
class Deck:
    #A classic deck. Hold info on the cards not yet drawn
    def __init__(self):
        self.avail=[Card(i+1) for i in range(52)]
        random.shuffle(self.avail) #It's like this is what it's made for
    def __repr__(self):
        return 'Deck(%s /52)'%len(self.avail)
    def __str__(self):
        return 'Deck(%s /52)'%len(self.avail)
    def draw(self): #Draw a card from the top of the deck
        foo=self.avail[0]
        self.avail.pop(0)
        return foo
    
    def shuffle(self): #Puts the discard pile back into the deck and shuffles
        return random.shuffle(self.avail)
    
class Hand:
    def __init__(self,owner,cards=[]):
        self.owner = owner
        self.cards = cards
        self.size = len(self.cards)
    def __repr__(self):
        return 'Hand of size %s' %self.size
    def __str__(self):
        if self.cards != None:
            foo=f"{self.owner}'s hand :\n"
            foo+=cardArt(self.cards)
            return(foo)
        else:
            return f"{self.owner}'s hand is empty\n"
    
    def add(self,card):
        self.cards.append(card)
        self.size=len(self.cards)
    def empty(self):
        self.cards = None
    
class Card:
    #Card class holds information about the cards. Their rank and suit, and provides a method to see the carsds
    def __init__(self,number):
        #Creates a card from a number, 1-52.
        rank=(number%13)+1 #number will be between 1 & 13, inclusive
        if rank <11 and rank != 1:
            self.rank= str(rank)
        elif rank==11:
                self.rank='Jack'
        elif rank == 12:
            self.rank='Queen'
        elif rank == 13:
            self.rank='King'
        elif rank == 1:
            self.rank='Ace'
        
        if number <14:
            self.suit="Hearts"
        elif number >= 14 and number <27:
            self.suit="Clubs"
        elif number >=27 and number <40:
            self.suit ="Diamonds"
        else:
            self.suit="Spades"
        
        
    def __repr__(self):
        return 'Card(%s of %s)' %(self.rank,self.suit)
    
    def __str__(self):
        return cardArt(self)
    
def cardArt(*cards):
    ''' Helper function to make printing the ACII art for cards'''
    suits_symbols = {'Spades':'♠','Diamonds': '♦','Hearts': '♥', 'Clubs' :'♣'}
    
    lines=[[] for i in range(9)]# create an empty list of list, each sublist is a line
    #pdb.set_trace()
    if type(cards[0])==list:
        for card in cards[0]:
            if card.rank== '10': #10 is the only rank we want to display 2 characters
                space=''
                rank=card.rank
            else: 
                rank=card.rank[0] #Take the first part of the rank, IE, the first letter for special cards
                space=' '
            sym=suits_symbols.get(card.suit) #Grab the symbol for  the suit
            # add the individual card on a line by line basis
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(sym))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')
    else:
            card=cards[0]
            if card.rank== '10': #10 is the only rank we want to display 2 characters
                space=''
                rank=card.rank
            else: 
                rank=card.rank[0] #Take the first part of the rank, IE, the first letter for special cards
                space=' '
            sym=suits_symbols.get(card.suit) #Grab the symbol for  the suit
            # add the individual card on a line by line basis
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(sym))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')
        
    result = [''.join(line) for line in lines]

    return '\n'.join(result)

    
if __name__=='__main__':
    hand=Hand("Me")
    deck=Deck()
    card=deck.draw()
    for i in range(3):
     hand.add(deck.draw())
    print(hand)
    hand.empty()
    print(hand)
    print(card)

