import pygame
from pygame.locals import *
from pygame.sprite import Sprite

from solitaire.spritesheet import SpriteSheet

from enum import Enum

class CardSuit(Enum):
    DIAMONDS = 1
    SPADES = 2
    HEARTS = 3
    CLUBS = 4

class Card(Sprite):
    @staticmethod
    def load_spritesheet():
        Card.cards_spritesheet = SpriteSheet("res/cards_sprite.png", 13, 5)
        Card.width = Card.cards_spritesheet.w
        Card.height = Card.cards_spritesheet.h
        
    @staticmethod
    def get_card_image(suit, value, visible):
        if not visible:
            return Card.cards_spritesheet.get_image(5, 4)

        new_value = value - 1
        new_suit = 0
        if suit == CardSuit.DIAMONDS:
            new_suit = 1
        elif suit == CardSuit.SPADES:
            new_suit = 3
        elif suit == CardSuit.HEARTS:
            new_suit = 0
        elif suit == CardSuit.CLUBS:
            new_suit = 2
        
        return Card.cards_spritesheet.get_image(new_value, new_suit)
    
    @staticmethod
    def is_valid_tableau_append(tableau_cards, new_card):
        if not tableau_cards:
            if new_card.value == 13:
                return True
        elif (abs(tableau_cards[-1].suit.value - new_card.suit.value) % 2 != 0 and
               tableau_cards[-1].value - 1 == new_card.value):
             return True
            
        return False

    def __init__(self, suit, value, visible, pos = (0, 0)):
        Sprite.__init__(self)
        self.suit = suit
        self.value = value
        self.visible = visible
        self.image = Card.get_card_image(self.suit, self.value, self.visible)
        self.rect = Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.moving = False
        self.last = pos
    
    def unhide(self):
        self.visible = True
        self.update_image()

    def hide(self):
        self.visible = False
        self.update_image()

    def update_image(self):
        self.image = Card.get_card_image(self.suit, self.value, self.visible)

    def move(self, pos):
        # if self.moving:
        self.rect.x += pos[0]
        self.rect.y += pos[1]
            # self.last = new_mouse_pos
