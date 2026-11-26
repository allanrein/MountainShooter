#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import pygame
import pygame.mixer
import code
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Const import C_ORANGE
from code.Const import C_BLACK
from code.Const import MENU_OPTION
from code.Const import C_WHITE
from code.Const import C_YELLOW


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf=pygame.image.load("./asset/MenuBg.png").convert_alpha()  # Load the image for the menu background
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load("./asset/Menu.mp3")
        pygame.mixer_music.play(-1)  # Loop the music -1 parameter means loop indefinitely
        while True:
            #DRAW IMAGES     
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=(C_WHITE), text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Shooter", text_color=(C_WHITE), text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=28, text=MENU_OPTION[i], text_color=(C_YELLOW), text_center_pos=((WIN_WIDTH / 2), 200 + (i * 25)))
                else:
                    self.menu_text(text_size=28, text=MENU_OPTION[i], text_color=(C_WHITE), text_center_pos=((WIN_WIDTH / 2), 200 + (i * 25)))

            pygame.display.flip()

            #check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    sys.exit()  # End Pygame loop
                if event.type == pygame.KEYDOWN: #key pressed
                    if event.key == pygame.K_UP: #up arrow key pressed
                        menu_option = (menu_option - 1) % len(MENU_OPTION) #get the rest of the division f ex menu option =2 (2 - 1) % 3 → 1 % 3 = 1
                    if event.key == pygame.K_DOWN: #down arrow key pressed
                        menu_option = (menu_option + 1) % len(MENU_OPTION) #get the rest of the division (0 + 1) % 3 → 1 % 3 = 1
                    if event.key == pygame.K_RETURN: #enter key pressed
                     return MENU_OPTION[menu_option]

                """  if menu_option == 0:
                            pygame.mixer_music.stop()
                            return 1
                        elif menu_option == 1:
                            pygame.mixer_music.stop()
                            return 2
                        elif menu_option == 2:
                            pygame.mixer_music.stop()
                            return 3
                        elif menu_option == 3:
                            pygame.mixer_music.stop()
                            return 4
                        elif menu_option == 4:
                            pygame.quit()  # Close window
                            quit()  # End Pygame loop """


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont(name="Lucinda Sans TypeWriter", size=text_size)
        text_surf: pygame.surface.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.rect.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
