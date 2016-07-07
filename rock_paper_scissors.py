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
        print("Bot: Rock")
        if bot_answer == 1:
            print("Draw")
        elif bot_answer == 2:
            print("Lose")
        else:
            print("Win")
    #Paper
    elif our_answer == 2:
        print("Bot: Paper")
        if bot_answer == 1:
            print("Win")
        elif bot_answer == 2:
            print("DRaw")
        else:
            print("Lose")
    #Scissors
    else:
        print("Bot: Scissors")
        if bot_answer == 1:
            print("Lose")
        elif bot_answer == 2:
            print("Win")
        else:
            print("Draw")
              
def check_collision(rock,paper,scissors,mouse_x,mouse_y,settings):
    """Method for detecting mouse click"""
    # If clicked on rock
    if rock.rect.collidepoint(mouse_x,mouse_y):
        #settings.game_screen = False
        our_answer = rock.value
        check_results(our_answer)
        print("Rock")
    # If clicked on paper
    elif paper.rect.collidepoint(mouse_x,mouse_y):
        #settings.game_screen = False
        our_answer = paper.value
        check_results(our_answer)
        print("Paper")
    # If clicked on scissors
    elif scissors.rect.collidepoint(mouse_x,mouse_y):
        #settings.game_screen = False
        our_answer = scissors.value
        check_results(our_answer)
        print("Scissors")
    else:
        print("Nothing")

def game_screen(myfont,screen,rock,scissors,paper,settings):
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

def result_screen(myfont,screen):
    resultlabel = myfont.render("YOU WIN!", 1, (0,0,0))
    screen.blit(resultlabel, (250, 100))
    # check events here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
        
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
        if settings.game_screen:
            game_screen(myfont,screen,rock,scissors,paper,settings)
        else:
            screen.fill(settings.bg_color)
            result_screen(myfont,screen)
        pygame.display.flip()
    
run_game()
