import pygame
from pygame.locals import *
from pygame.sprite import Group
from pygame import Surface

from spritesheet import SpriteSheet
from enum import Enum
from card import Card, CardSuit

class GameState(Enum):
    MENU = 1
    GAME = 2
    GAME_OVER = 3

class Solitaire:
    game_state = GameState.GAME
    should_quit = False

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Solitaire")

        self.cards_spritesheet = SpriteSheet("res/cards_sprite.png", 13, 5)

        self.dragged_card = None

        self.background = Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((68, 163, 92))

        self.group = Group()
        
        for i in range(0, 50):
            self.group.add(Card(self.get_card_image(CardSuit.HEARTS, 2), (i, i)))

    def get_card_image(self, suit, value):
        value -= 1
        if value == 0:
            value = 12

        if suit == CardSuit.DIAMONDS:
            suit = 1
        elif suit == CardSuit.SPADES:
            suit = 3
        elif suit == CardSuit.HEARTS:
            suit = 0
        elif suit == CardSuit.CLUBS:
            suit = 2
        
        return self.cards_spritesheet.get_image(suit, value)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.should_quit = True
            elif event.type == MOUSEBUTTONDOWN:
                for sprite in reversed(self.group.sprites()):
                    if sprite.start_drag(event.pos):
                        self.dragged_card = sprite
                        break
            elif event.type == MOUSEMOTION:
                if self.dragged_card:
                    self.dragged_card.mouse_move(event.pos)
            elif event.type == MOUSEBUTTONUP:
                if self.dragged_card:
                    self.dragged_card.end_drag()
                    self.dragged_card = None


    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.group.draw(self.screen)
        pygame.display.flip()