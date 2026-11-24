#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Protocol

import pygame


class Entity(ABC): #abstract Base Class (ABC) for all entities in the game, only the subclasses can be instantiated, not the base class itself
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf=pygame.image.load(f"./asset/{name}.png")
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 5  # Default speed, can be overridden by subclasses

@abstractmethod
def move(self, ):
        pass
