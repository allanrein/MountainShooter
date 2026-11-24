#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import pygame

from code.Const import COLOR_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name=name
        self.game_mode=game_mode
        self.entity_list: list[Entity] = []  # List to hold all entities in the level
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # Add background entities to the list
        self.timeout = 20000  # Set the level timeout to 20 seconds (20000 milliseconds)

    def run(self):
        pygame.mixer_music.load("./asset/Level1.mp3")  # Load the background music for the level
        pygame.mixer_music.play(-1)  # Loop the music -1 parameter means loop indefinitely
        clock = pygame.time.Clock()  # Create a clock object to manage the frame rate fps
        while True:
            clock.tick(60)  # Limit the frame rate to 60 frames per second
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()  # Call the move method for each entity
            pygame.display.flip()  # Update the display to show the drawn entities
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    sys.exit()  # End Pygame loop

            # printed text
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color=COLOR_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps() :.0f}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont(name="Lucinda Sans TypeWriter", size=text_size)
        text_surf: pygame.surface.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.rect.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
