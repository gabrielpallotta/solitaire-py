import pygame
from pygame.locals import *
from pygame.sprite import Sprite

from spritesheet import SpriteSheet

from enum import Enum

class CardSuit(Enum):
    DIAMONDS = 1
    SPADES = 2
    HEARTS = 3
    CLUBS = 4

class Card(Sprite):
    def __init__(self, suit, value, visible, pos = (0, 0)):
        Sprite.__init__(self)
        self.suit = suit
        self.value = value
        self.visible = visible
        self.image = Card.get_card_image(self.suit, self.value, self.visible)
        self.rect = Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.moving = False
        self.last = pos

    @staticmethod
    def load_spritesheet():
        Card.cards_spritesheet = SpriteSheet("res/cards_sprite.gif", 13, 5)

    @staticmethod
    def get_card_image(suit, value, visible):
        if not visible:
            return Card.cards_spritesheet.get_image(0, 4)

        value -= 2
        if value < 0:
            value = 12

        if suit == CardSuit.DIAMONDS:
            suit = 1
        elif suit == CardSuit.SPADES:
            suit = 3
        elif suit == CardSuit.HEARTS:
            suit = 0
        elif suit == CardSuit.CLUBS:
            suit = 2
        
        return Card.cards_spritesheet.get_image(value, suit)
    
    def unhide(self):
        self.visible = True
        self.update_image()

    def hide(self):
        self.card = card
        self.update_image()

    def update_image(self):
        self.image = Card.get_card_image(self.suit, self.value, self.visible)

    def move(self, pos):
        # if self.moving:
        self.rect.x += pos[0]
        self.rect.y += pos[1]
            # self.last = new_mouse_pos
