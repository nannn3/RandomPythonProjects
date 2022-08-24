# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 08:34:48 2022

@author: Tristen
"""

import cards
import pdb


def hand_val(hand):
    ace = False
    total = 0
    for i in hand.get_cards():
        if not i.get_rank().isnumeric():
            if i.get_rank() == 'Ace':
                total += 11
                ace = True
            else:
                total += 10
        else:
            total += int(i.get_rank())
    if ace and total > 21:
        total -= 10  # ace is 11 unless it would cause you to bust
    return total


def determine_winner(hand1, hand2):
    if hand_val(hand1) > hand_val(hand2):
        return hand1
    elif hand_val(hand1) < hand_val(hand2):
        return hand2
    else:
        return None


def game_over(hand1, hand2, winner=None):
    if not winner:
        winner = determine_winner(hand1, hand2)
        if winner:
            if winner == hand1:
                print("You won!")
            if winner == hand2:
                print("You lost")
        else:
            print("It was a push")

    foo = input("Would you like to play another hand? y/n")
    if foo.lower() == 'y':
        main()
    else:
        print("Have a nice day")


def main():
    # pdb.set_trace()

    deck = cards.Deck()
    dealer_hand = cards.Hand("Dealer")
    player_hand = cards.Hand("your")
    winner = None
    for _ in range(2):
        dealer_hand.add(deck.draw())
        player_hand.add(deck.draw())
    while hand_val(player_hand) < 21:
        print(dealer_hand)
        print(player_hand)

        foo = input("Would you like to hit[h] or pass[p]?\n")
        hit = ['h', 'hit']
        pas = ['p', 'pass']
        if foo.lower() in hit:
            player_hand.add(deck.draw())
        elif foo.lower() in pas:
            break
    if hand_val(player_hand) > 21:
        print(player_hand)
        print("You went bust, sorry\n")
        winner = 'dealer'
    else:
        while hand_val(dealer_hand) < 17:
            # dealer stays on 17
            print("Dealer draws")
            dealer_hand.add(deck.draw())
            print(dealer_hand)
            print(player_hand)
        if hand_val(dealer_hand) > 21:
            winner = 'player'
    game_over(player_hand, dealer_hand, winner)


if __name__ == '__main__':
    main()
