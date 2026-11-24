#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import name

import pygame

from code.Level import Level
from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT 
from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        print("Setup Starting...")
        print("Setup Complete!")
        print("Start Loop")
     
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                print("Starting New Game 1P")
                level = Level(self.window, "Level1", game_mode=menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:
                print("Starting New Game 2P - COOPERATIVE")
                level = Level(self.window, "Level2", menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[2]:
                print("Starting New Game 2P - COMPETITIVE")
                level = Level(self.window, "Level3", menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[3]:
                print("Showing Score")
            elif menu_return == MENU_OPTION[4]:
                print("Exiting Game")
                pygame.quit()
                quit()
            else:
                print("Invalid menu option selected. Returning to menu.")
                pass
            # Check for all events
            #for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.quit()  # Close window
            #        quit()  # End Pygame loop

