#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.key

from code.PlayerShot import PlayerShot
from code.Const import PLAYER_KEY_LEFT, PLAYER_KEY_DOWN, PLAYER_KEY_SHOOT, PLAYER_KEY_UP, PLAYER_KEY_SHOOT, PLAYER_KEY_RIGHT, WIN_HEIGHT, WIN_WIDTH, WIN_HEIGHT, WIN_WIDTH
from code.Const import ENTITY_SPEED
from code.Entity import Entity
from code.Const import ENTITY_SHOT_DELAY

class Player(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Initialize shot delay counter

    def update(self):
        pass

    def move(self,):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]  # Move the player up
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]  # Move the player down
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]  # Move the player left
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]  # Move the player right
        pass

    def shoot(self):
        self.shot_delay -= 1  # Decrease the shot delay counter
        if self.shot_delay == 0:  # If the shot delay has elapsed
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Reset the shot delay counter  
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))
        