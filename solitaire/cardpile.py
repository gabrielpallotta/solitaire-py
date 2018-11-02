from enum import Enum
from pygame.sprite import Group
from pygame import Surface
from solitaire.card import Card

class TableauPile(Group):
    def __init__(self, rect, image, card_spacing = 30):
        Group.__init__(self)
        self.rect = rect
        self.image = image
        self.spacing = card_spacing

    def add_card(self, card):
        if not card.visible:
            if self.sprites():
                self.sprites()[-1].hide()
            card.unhide()

        card.rect.x = self.rect.x
        card.rect.y = self.rect.y + self.spacing * len(self.sprites())

        if self.sprites():
            self.rect.height += self.spacing
        # if not self.cards:
        #     if not visible:
        self.add(self, card)

    def remove_card(self, card):
        self.remove(card)
        if self.sprites():
            self.rect.height -= self.spacing
        print(card)

    def collidepoint(self, point):
        return self.rect.collidepoint(point)

    def start_drag(self, mouse_pos):
        card_start = None

        for sprite in reversed(self.sprites()):
            if sprite.rect.collidepoint(mouse_pos) and sprite.visible:
                card_start = sprite
                break
        
        card_drag_list = []
        if card_start:
            card_drag_list = self.sprites()[self.sprites().index(card_start):]
            for card_sprite in card_drag_list:
                self.remove_card(card_sprite)
                print("REMOVEU")

        print (card_drag_list)
        return card_drag_list

    def end_drag(self):
        if self.sprites():
            self.sprites()[-1].unhide()

    def drop(self, card_sprite_list):
        for card in card_sprite_list:
            self.add_card(card)

    def draw(self, surf):
        if not self.sprites():
            surf.blit(self.image, (self.rect.x, self.rect.y))
        Group.draw(self, surf)

class FoundationPile(Group):
    def __init__(self, rect, image):
        Group.__init__(self)
        self.rect = rect
        self.image = image

    def draw(self, surf):
        if not self.sprites():
            surf.blit(self.image, (self.rect.x, self.rect.y))

class StockPile(Group):
    def __init__(self, rect):
        Group.__init__(self)
        self.rect = rect

    def collidepoint(self, point):
        return self.rect.collidepoint(point)

    def add_card(self, card):
        card.rect.x = self.rect.x
        card.rect.y = self.rect.y

        Group.add(self, card)

    def draw_cards(self):
        card = self.sprites()[0]
        self.remove(card)
        return [card]
    
    def draw(self, surf):
        if not self.sprites():
            surf.blit(self.image, (self.rect.x, self.rect.y))
        else:
            surf.blit(self.sprites()[0].image, (self.rect.x, self.rect.y))

class WastePile(Group):
    def __init__(self, rect, card_spacing):
        Group.__init__(self)
        self.rect = rect
        self.spacing = card_spacing
    
    def add_card(self, card):
        Group.add(self, card)

        i = 0
        for card in self.sprites()[-3:]:
            card.rect.x = self.rect.x + self.spacing * i
            card.rect.y = self.rect.y
            i += 1

    
    def draw(self, surf):
        for card in self.sprites()[-3:]:
            surf.blit(card.image, card.rect)