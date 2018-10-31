import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Card(Sprite):
    def __init__(self, image, pos = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.moving = False
        self.last = pos

    def mouse_move(self, new_mouse_pos):
        if self.moving:
            self.rect.move_ip((new_mouse_pos[0] - self.last[0], new_mouse_pos[1] - self.last[1]))
            self.last = new_mouse_pos

    def start_drag(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.last = mouse_pos
            self.moving = True
            return True
        else:
            return False

    def end_drag(self):
        self.moving = False

