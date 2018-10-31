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
    game_state = GameState.MENU
    should_quit = False

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jogo")

        self.background = Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        cards = SpriteSheet("cards_sprite.gif", 13, 5)

        self.group = Group()
        self.group.add(Card(cards.get_sprite(0, 0), (20, 20)))

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.should_quit = True
            elif event.type == MOUSEBUTTONDOWN:
                for sprite in self.group:
                    sprite.mouse_move(event.pos)
                    sprite.check_click(event.pos)
            elif event.type == MOUSEMOTION:
                for sprite in self.group:
                    sprite.check_click(event.pos)


    def render(self):
        self.screen.blit(self.background, (0, 0))
        # self.screen.blit(self.card_spritesheet.get_sprite(0, 0), (20, 20))
        self.group.draw(self.screen)
        pygame.display.flip()