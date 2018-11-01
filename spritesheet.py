import pygame
from pygame.locals import *

class SpriteSheet:
    def __init__(self, path, h_imgs, v_imgs):
        self.sprite_sheet = pygame.image.load(path).convert_alpha()
        self.w = self.sprite_sheet.get_width() / h_imgs;
        self.h = self.sprite_sheet.get_height() / v_imgs;
    
    def get_image(self, i, j):
        return self.sprite_sheet.subsurface(Rect(i * self.w, j * self.h, self.w, self.h))