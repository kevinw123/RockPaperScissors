import pygame
import sys
from rock import Rock
from settings import Settings
from paper import Paper
from scissors import Scissors

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Rock Paper Scissors")
    screen.fill(settings.bg_color)
    rock = Rock(settings, screen)
    paper = Paper(settings, screen)
    scissors = Scissors(settings, screen)
    myfont = pygame.font.SysFont("monospace", 30)
    
    while True:
        label = myfont.render("Choose either rock, paper or scissors", 1, (0,0,0))
        screen.blit(label, (250, 100))
        # check events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
        rock.blitme()
        paper.blitme()
        scissors.blitme()
        pygame.display.flip()
    
run_game()
