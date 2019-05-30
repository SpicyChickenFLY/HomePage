"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/05/30
"""

import deck.Deck
import player.Player

def check_player():
    pass

def compare_hands(dealer_hand, player_hand):
    pass

def game():
    '''check all players and dealer are ready'''
    deck = Deck(2)
    players = [Player(20), Player(30),  Player(30)]
    dealer = Player(70)
    while True:
        for player in players:
            player.add_bet(5)
        for player in players:
            card = deck.deal()
            player.deal(card)
        card = deck.deal()
        dealer.deal(card)
        for player in players:
            card = deck.deal().flip()
            player.deal(card)
        card = deck.deal().flip()
        dealer.deal(card)
        for player in players:
            command = player.command_1()
            if command == 1:
                pass
            elif command == 2:
                pass
            elif command == 3:
                pass
            else:
                pass
            


    



