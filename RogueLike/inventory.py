import pygame, math, sys, random
from pygame.locals import *
import items as i

HEAD, CHEST, GLOVES, CLOAK, LEGS, BOOTs, HAND1, HAND2 = 0, 1,2,3,4,5,6,7
BACKPACK_SLOT = [[402 for w in range(4)] for h in range(12) ]
BACKPACK = [[402 for w in range(4)] for h in range(12) ]
ARMOR_SLOT = [[402 for w in range(4)] for h in range (2) ]
ARMOR = [[402 for w in range(4)] for h in range (2) ]
EQUIP = {	HEAD : None, 
			CHEST : None,
			GLOVES : None,
			CLOAK : None,
			LEGS : None,
			BOOTs : None,
			HAND1 : None,
			HAND2 : None
		}

class inventory():
	def __init__():
		pass