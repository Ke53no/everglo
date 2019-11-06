import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230,230,230)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()