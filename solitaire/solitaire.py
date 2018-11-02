import pygame
from pygame.locals import *
from pygame.sprite import Group
from pygame import Surface

from random import shuffle

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

        Card.load_spritesheet()
        
        self.dragged_cards_pile = None
        self.dragged_cards = []

        self.background = Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((68, 163, 92))

        self.cards = []
        for i in range(0, 4):
            for j in range(0, 13):
                self.cards.append((Card(i, j, True)))

        # Card piles
        self.stock = StockPile((0, 0))
        self.tableaus = []
        for i in range(0, 7):
            self.tableaus.append(TableauPile((100 * i, 50)))
            for j in range (0, i + 1):
                self.tableaus[i].add_card(self.cards[7 * i + j])

        # for i in range(0, 50):
        #     self.stock.add_card(self.cards[10])

    def update(self):
        print(self.dragged_cards)
        for event in pygame.event.get():
            if event.type == QUIT:
                self.should_quit = True
            elif event.type == MOUSEBUTTONDOWN:
                for tableau in self.tableaus:
                    self.dragged_cards = tableau.drag(event.pos)
                    if self.dragged_cards:
                        self.dragged_cards_pile = tableau
                        break
            elif event.type == MOUSEMOTION:
                mouse_rel = pygame.mouse.get_rel()
                for sprite in self.dragged_cards:
                    sprite.move(mouse_rel)
                
            elif event.type == MOUSEBUTTONUP:
                if self.dragged_cards:
                    for tableau in self.tableaus:
                        if tableau.drop(event.pos, self.dragged_cards):
                            self.dragged_cards = []
                            break
                    for card in self.dragged_cards:
                        self.dragged_cards_pile.add_card(card)
                    self.dragged_cards = []
                    
        self.stock.update()
        for tableau in self.tableaus:
            tableau.update()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.stock.draw(self.screen)

        for tableau in self.tableaus:
            tableau.draw(self.screen)

        for card_sprite in self.dragged_cards:
            self.screen.blit(card_sprite.image, card_sprite.rect)
        
        pygame.display.flip()