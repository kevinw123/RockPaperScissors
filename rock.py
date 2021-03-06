import pygame
from pygame.sprite import Sprite

class Rock(Sprite):

    def __init__(self, settings, screen):
        super(Rock, self).__init__()
        self.screen = screen
        self.settings = settings
        self.value = 1
        self.image = pygame.image.load('images/rock.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
