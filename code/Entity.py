#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from code.Const import ENTITY_HEALTH
import pygame


class Entity(ABC): #abstract Base Class (ABC) for all entities in the game, only the subclasses can be instantiated, not the base class itself
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf=pygame.image.load(f"./asset/{name}.png").convert_alpha()  # Load the image for the entity
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 5  # Default speed, can be overridden by subclasses
        self.healthy = ENTITY_HEALTH[self.name]

@abstractmethod
def move(self, ):
        pass
