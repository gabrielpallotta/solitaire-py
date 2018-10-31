import pygame
from pygame.locals import *

class SpriteSheet:
    def __init__(self, path, h_imgs, v_imgs):
        self.sprite_sheet = pygame.image.load(path).convert_alpha()
        self.w = self.sprite_sheet.get_width() / h_imgs;
        self.h = self.sprite_sheet.get_height() / v_imgs;
        print(self.w)
        print(self.h)
    
    def get_sprite(self, i, j):
        return self.sprite_sheet.subsurface((i * self.w, j * self.h, (i + 1) * self.w, (j + 1) * self.h))