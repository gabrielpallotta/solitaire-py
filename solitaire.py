import pygame
from pygame.locals import *
from pygame.sprite import Group
from pygame import Surface

from enum import Enum
from card import Card
from spritesheet import SpriteSheet

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
        pygame.display.set_caption("Jogo")

        self.dragged_card = None

        self.background = Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((68, 163, 92))

        cards = SpriteSheet("res/cards_sprite.png", 13, 5)

        self.group = Group()
        
        for i in range(0, 50):
            self.group.add(Card(cards.get_sprite(0, 0), (i, i)))

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