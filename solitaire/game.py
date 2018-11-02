import pygame
from pygame.locals import *
from pygame.sprite import Group
from pygame import Surface

from random import shuffle

from enum import Enum
from solitaire.card import Card, CardSuit
from solitaire.cardpile import *

# TODO: use these game states
class GameState(Enum):
    MENU = 1
    GAME = 2
    GAME_OVER = 3

class Solitaire:
    game_state = GameState.GAME
    should_quit = False

    def __init__(self, spacing, tableau_spacing):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Solitaire")

        Card.load_spritesheet()

        self.spacing = spacing

        width = 8 * self.spacing + 7 * int(Card.width)
        height = 2 * self.spacing + int(Card.height) + 500
        self.screen = pygame.display.set_mode((width, height))
        
        self.dragged_cards_pile = None
        self.dragged_cards = []

        self.background = Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((66, 163, 78))
        
        cards = []
        for i in range(0, 4):
            for j in range(0, 13):
                cards.append((Card(i, j, False)))
        shuffle(cards)
 
        # Stock pile
        self.stock = StockPile(Rect(20, 20, Card.width, Card.height))
        
        # Waste pile
        self.waste = WastePile(Rect(100, 0, Card.width, Card.height))
        
        # Foundation piles
        self.foundations = []
        for i in range (0, 4):
            foundation_rect = Rect(4 * self.spacing + 3 * Card.width + (self.spacing + Card.width) * i, self.spacing, Card.width, Card.height)
            self.foundations.append(FoundationPile(foundation_rect, Card.cards_spritesheet.get_image(2, 4)))

        # Tableau piles
        self.tableaus = []
        index = 0
        for i in range(0, 7):
            tableau_rect = Rect(self.spacing + (self.spacing + Card.width) * i, 2 * self.spacing + Card.height, Card.width, Card.height)
            self.tableaus.append(TableauPile(tableau_rect, Card.cards_spritesheet.get_image(2, 4), tableau_spacing))
            for j in range (0, i + 1):
                self.tableaus[i].add_card(cards[index])
                index += 1

        # Add cards to stock
        for i in range(28, 52):
            self.stock.add_card(cards[i])

    def update(self):
        # print(self.dragged_cards)
        for event in pygame.event.get():
            if event.type == QUIT:
                self.should_quit = True
            elif event.type == MOUSEBUTTONDOWN:
                if not self.dragged_cards:
                    for tableau in self.tableaus:
                        if tableau.collidepoint(event.pos):
                            self.dragged_cards = tableau.start_drag(event.pos)
                            self.dragged_cards_pile = tableau
                            break
            elif event.type == MOUSEMOTION:
                mouse_rel = pygame.mouse.get_rel()
                for sprite in self.dragged_cards:
                    sprite.move(mouse_rel)
                
            elif event.type == MOUSEBUTTONUP:
                if self.dragged_cards:
                    for tableau in self.tableaus:
                        if tableau.collidepoint(event.pos):
                            tableau.drop(self.dragged_cards)
                            self.dragged_cards = []
                            break
                    for card in self.dragged_cards:
                        self.dragged_cards_pile.add_card(card)
                    self.dragged_cards = []
                    self.dragged_cards_pile.end_drag()
                    self.dragged_cards_pile = None
                    
        self.stock.update()
        for tableau in self.tableaus:
            tableau.update()

    def render(self):
        self.screen.blit(self.background, (0, 0))

        self.stock.draw(self.screen)
        self.waste.draw(self.screen)

        for foundation in self.foundations:
            foundation.draw(self.screen)

        for tableau in self.tableaus:
            tableau.draw(self.screen)

        for card_sprite in self.dragged_cards:
            self.screen.blit(card_sprite.image, card_sprite.rect)
        
        pygame.display.flip()

    def run(self):
        while not self.should_quit:
            self.update()
            self.render()