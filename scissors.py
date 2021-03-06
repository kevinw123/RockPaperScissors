import pygame
from pygame.sprite import Sprite

class Scissors(Sprite):

    def __init__(self, settings, screen):
        super(Scissors, self).__init__()
        self.screen = screen
        self.settings = settings
        self.value = 3
        self.image = pygame.image.load('images/scissors.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx - 300
        self.rect.bottom = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
