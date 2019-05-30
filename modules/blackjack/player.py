"""
Author: Chow
Create: 2019/05/30
Last Review: 2019/05/30
"""

import deck

class Player:
    hands = [[]]
    chips = 20
    bets = 0
    
    def __init__(self, chips):
        self.chips = chips

    def deal(self, hand_index, card):
        self.hands[hand_index].append(card)
    
    def drop(self, hand_index):
        hands = self.hands[hand_index]
        self.hands[hand_index] = []
        return hands

    def add_bet(self, price):
        if self.chips > price:
            self.chips -= price
            self.bets += price
            return True
        else:
            return False
    
    def command_1(self, hand_index):
        add_bet_allow = chips > 0
        split_allow = (hands[hand_index])
        input("")

    def show_hands(self, check=False):
        for hand_index, hand in enumerate(self.hands):
            print("hands: ", end='')
            for card in hand:
                card.show(check)
                print(' ', end='')
            print('')

if __name__ == "__main__":
    dealer = Player(40)
    dealer.deal(0, deck.Card(12, 'spade'))
    dealer.deal(0, deck.Card(1, 'spade', True))
    dealer.deal(0, deck.Card(2, 'heart', True))
    dealer.show_hands()