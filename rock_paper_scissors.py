import pygame
import sys
from rock import Rock
from settings import Settings
from paper import Paper
from scissors import Scissors
import random


def check_results(our_answer):
    bot_answer = random.randrange(1,4)
    #Rock
    if our_answer == 1:
        if bot_answer == 1:
            print("Opponent picked Rock, Draw!")
        elif bot_answer == 2:
            print("Opponent picked Paper, You Lose!")
        else:
            print("Opponent picked Scissors, You Win!")
    #Paper
    elif our_answer == 2:
        if bot_answer == 1:
            print("Opponent picked Rock, You Win!")
        elif bot_answer == 2:
            print("Opponent picked Paper, Draw!")
        else:
            print("Opponent picked Scissors, You Lose!")
    #Scissors
    else:
        if bot_answer == 1:
            print("Opponent picked Rock, You Lose!")
        elif bot_answer == 2:
            print("Opponent picked Paper, You Win!")
        else:
            print("Opponent picked Scissors, Draw!")

def check_collision(rock,paper,scissors,mouse_x,mouse_y,settings):
    """Method for detecting mouse click"""
    # If clicked on rock
    if rock.rect.collidepoint(mouse_x,mouse_y):
        our_answer = rock.value
        print("You chose Rock")
        check_results(our_answer)
    # If clicked on paper
    elif paper.rect.collidepoint(mouse_x,mouse_y):
        our_answer = paper.value
        print("You chose Paper")
        check_results(our_answer)
    # If clicked on scissors
    elif scissors.rect.collidepoint(mouse_x,mouse_y):
        our_answer = scissors.value
        print("You chose Scissors")
        check_results(our_answer)
    else:
        print("Nothing")
        
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
                check_collision(rock,paper,scissors,mouse_x,mouse_y,settings)
        rock.blitme()
        paper.blitme()
        scissors.blitme()

        pygame.display.flip()
    
run_game()
