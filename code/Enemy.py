#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, WIN_WIDTH
from code.EnemyShot import EnemyShot

class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Initialize shot delay counter

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Move the background to the left

    def shoot(self):
        self.shot_delay -= 1  # Decrease the shot delay counter
        if self.shot_delay == 0:  # If the shot delay has elapsed
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Reset the shot delay counter  
            return EnemyShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))
        