import pygame, math, sys, random, spritesheet
from pygame.locals import *
import tile as t

#Constants of tiles, starting at 0
DIRT = 0
GRASS = 1
WATER = 2
STONE = 3
SHOP = 4
x=0
y=0
#Constants for textures
texture_sprites = {
			DIRT : t.tile("Dirt", 0, "images/dungeon/floor/grass/grass_full.png", True, x, y),
			GRASS : t.tile("Grass", 1, "images/dungeon/floor/grass/grass_flowers_red1.png", True, x, y),
			WATER : t.tile("Water", 2, "images/dungeon/water/shallows1.png", False, x, y),
			STONE : t.tile("Stone", 3, "images/dungeon/floor/cobble_blood1.png", False, x, y)
            }

maps = []

class generator():
	def do(self, MAPWIDTH, MAPHEIGHT):
		DIRT = 0
		GRASS = 1
		WATER = 2
		STONE = 3
		SHOP = 4
		TILE_MAP = [ [WATER for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

		for row in range(MAPHEIGHT):
			for column in range(MAPWIDTH):
				randomNumber = random.randint(0, 15)
				if randomNumber == 0:
					TILE = t.tile("Stone", 3, pygame.image.load("images/dungeon/floor/cobble_blood1.png").convert_alpha(), False, column, row)
				elif randomNumber == 1 or randomNumber == 2:
					TILE = t.tile("Water", 2, pygame.image.load("images/dungeon/water/shallows1.png").convert_alpha(), False, column, row)
				elif randomNumber >= 3 or randomNumber <= 7:
					TILE = t.tile("Grass", 1, pygame.image.load("images/dungeon/floor/grass/grass_flowers_red1.png").convert_alpha(), True, column, row)
				else:
					TILE = t.tile("Dirt", 0, pygame.image.load("images/dungeon/floor/grass/grass_full.png").convert_alpha(), True, column, row)
				TILE_MAP[row][column] = TILE
			maps.append(TILE_MAP)
		return TILE_MAP
########