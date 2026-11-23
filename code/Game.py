#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT 
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
            menu.run()
            pass
            # Check for all events
            #for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.quit()  # Close window
            #        quit()  # End Pygame loop

