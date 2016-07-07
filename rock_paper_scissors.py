import pygame
from rock import Rock
from settings import Settings

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Rock Paper Scissors")
    screen.fill(settings.bg_color)
    rock = Rock(settings, screen)
    rock.blitme()
    pygame.display.flip()
    
run_game()
