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

class Card:
    def __init__(self, suit, value, visible):
        self.suit = suit
        self.value = value
        self.visible = visible

class CardSprite(Sprite):
    def __init__(self, card, pos = (0, 0)):
        Sprite.__init__(self)
        self.card = card
        self.image = CardSprite.get_card_image(self.card)
        self.rect = Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.moving = False
        self.last = pos

    @staticmethod
    def load_spritesheet():
        CardSprite.cards_spritesheet = SpriteSheet("res/cards_sprite.gif", 13, 5)

    @staticmethod
    def get_card_image(card):
        if not card.visible:
            return CardSprite.cards_spritesheet.get_image(0, 4)

        suit = card.suit
        value = card.value

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
        
        return CardSprite.cards_spritesheet.get_image(value, suit)
    
    def update_card(card):
        self.card = card
        self.image = CardSprite.get_card_image(self.card)


