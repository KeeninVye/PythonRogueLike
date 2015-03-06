import pygame, math, sys, random
from pygame.locals import *

#Slots
#[0 = head, 1 = chest, 2 = gloves, 3 = cloak, 4 = legs, 5 = boots, 6 = hand1, 7 = hand2]
ITEM_LIST = []

class item(object):
    def __init__(self, name, id, info, image, slot):
        self.name = name
        self.id = id
        self.info = info
        self.image = image
        self.slot = slot
        ITEM_LIST.append(self)


class armor(item):
	def __init__(self, name, id, info, image, slot, armor, style):
		item.__init__(self, name, id, info, image, slot)
		self.armor = armor
		self.style = style

class weapon(item):
	def __init__(self, name, id, info, image, slot, damage):
		item.__init__(self, name, id, info, image, slot)
		self.damage = damage
		
def get_item(id):
    for item in ITEM_LIST:
    	if item.id == id:
    		return item

def is_weapon(item):
    if 219 < item.id < 250:
        return True

def is_armor(item):
    if 249 < item.id < 300:
        return True