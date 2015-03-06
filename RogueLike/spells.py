import pygame, math, sys, random, spritesheet
from pygame.locals import *

SPELL_LIST = []

class magic():
	def __init__(self, name, id, image, amount=None, effect=None):
		self.name = name
		self.id = id
		self.image = image
		self.amount = amount
		self.effect = effect
		SPELL_LIST.append(self)

class damage(magic):
	def __init__(self, name, id, image, amount=None, effect=None):
		magic.__init__(self, name, id, image, amount, effect)
		
class heal(magic):
	def __init__(self, name, id, image, amount=None, effect=None):
		magic.__init__(self, name, id, image, amount, effect)

class buff(magic):
	def __init__(self, name, id, image, amount=None, effect=None):
		magic.__init__(self, name, id, image, amount, effect)