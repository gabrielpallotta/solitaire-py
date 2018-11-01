import pygame
from pygame.locals import *
from pygame.sprite import Group
from pygame import Surface

from enum import Enum
from card import Card, CardSuit
from cardpile import *

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

        CardSprite.load_spritesheet()

        self.dragged_cards = None

        self.background = Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((68, 163, 92))

        self.cards = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.cards.insert(len(self.cards), Card(i, j, False))

        # Card piles
        self.stock = StockPile((0, 0))
        self.tableaus = []
        for i in range(0, 7):
            self.tableaus.insert(len(self.tableaus), TableauPile((100 * i, 50)))
            for j in range (0, i + 1):
                self.tableaus[i].add_card(self.cards[10])

        for i in range(0, 50):
            self.stock.add_card(self.cards[10])

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.should_quit = True
            elif event.type == MOUSEBUTTONDOWN:
                for tableaus in self.tableaus:
                    if sprite.start_drag(event.pos):
                        self.dragged_card = sprite
                        break
            elif event.type == MOUSEMOTION:
                
            elif event.type == MOUSEBUTTONUP:
                
        self.stock.update()
        for tableau in self.tableaus:
            tableau.update()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.stock.draw(self.screen)
        for tableau in self.tableaus:
            tableau.draw(self.screen)

        pygame.display.flip()