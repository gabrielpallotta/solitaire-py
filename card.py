import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Card(Sprite):
    def __init__(self, image, pos = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.moving = False
        self.last = pos

    def mouse_move(self, mouse):
        if self.moving:
            self.rect.move_ip((mouse[0] - self.last[0], mouse[1] - self.last[1]))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.last = mouse
            self.moving = True


