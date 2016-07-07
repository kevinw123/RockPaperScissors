import pygame
import sys
from rock import Rock
from settings import Settings

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Rock Paper Scissors")
    screen.fill(settings.bg_color)
    rock = Rock(settings, screen)

    while True:
        # check events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        rock.blitme()
        pygame.display.flip()
    
run_game()
