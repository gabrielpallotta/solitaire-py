from enum import Enum
from pygame.sprite import Group
from card import Card

class CardPile(Group):
    def __init__(self, pos):
        Group.__init__(self)
        self.pos = pos
    
    def add_card(self, card):
        Group.add(self, card)

class TableauPile(CardPile):
    def __init__(self, pos):
        CardPile.__init__(self, pos)

    def add_card(self, card):
        card.rect.x = self.pos[0]
        card.rect.y = self.pos[1] + 50 * len(self.sprites())
        # if not self.cards:
        #     if not visible:
        Group.add(self, card)

    def drag(self, mouse_pos):
        card_start = None

        for sprite in reversed(self.sprites()):
            if sprite.rect.collidepoint(mouse_pos) and sprite.visible:
                card_start = sprite
                break
        
        card_drag_list = []
        if card_start:
            card_drag_list = self.sprites()[self.sprites().index(card_start):]
            del self.sprites()[self.sprites().index(card_start):]

        for card_sprite in card_drag_list:
            self.remove(card_sprite)

        return card_drag_list

    def drop(self, mouse_pos, card_sprite_list):
        can_drop = False
        for sprite in self.sprites():
            if sprite.rect.collidepoint(mouse_pos):
                can_drop = True
                break

        if can_drop:
            # check stuff

            for card in card_sprite_list:
                self.add_card(card)

            return True
        else:
            return False

class FoundationPile(CardPile):
    def __init__(self, pos):
        CardPile.__init__(self, pos)

class StockPile(CardPile):
    def __init__(self, pos):
        CardPile.__init__(self, pos)

class WastePile(CardPile):
    def __init__(self, pos):
        CardPile.__init__(self, pos)