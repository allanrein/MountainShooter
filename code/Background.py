#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Move the background to the left
        if self.rect.right <= 0:  # If the background has moved completely off the screen
            self.rect.left = WIN_WIDTH  # Reset its position to the right side of the screen
        
