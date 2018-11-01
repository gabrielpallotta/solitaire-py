from enum import Enum
from pygame.sprite import Group
from card import CardSprite

class CardPile(Group):
    def __init__(self, pos):
        Group.__init__(self)
        self.pos = pos
    
    def add_card(self, card):
        Group.add(self, CardSprite(card, self.pos))

class TableauPile(CardPile):
    def __init__(self, pos):
        CardPile.__init__(self, pos)

class FoundationPile(CardPile):
    def __init__(self, pos):
        CardPile.__init__(self, pos)

class StockPile(CardPile):
    def __init__(self, pos):
        CardPile.__init__(self, pos)

class WastePile(CardPile):
    def __init__(self, pos):
        CardPile.__init__(self, pos)