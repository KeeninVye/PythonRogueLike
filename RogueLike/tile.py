import pygame, math, sys, random

TILE_LIST = []
NAV_LIST = []
H,V = 1, 24

class tile():
	List = []
	total_tiles = 1
	def __init__(self, name, id, image, walkable, x, y, resource = False, entrance = False):
		self.name = name
		self.id = id
		self.image = image
		self.walkable = walkable
		self.parent = None
		self.x = x
		self.y = y
		self.type = type
		self.H, self.G, self.F = 0,0,0
		self.tile_number = tile.total_tiles
		self.resource = resource
		self.entrance = entrance
		
		tile.total_tiles += 1
		TILE_LIST.append(self)

	def get_name():
		return name

	def get_id():
		return id

	def get_image():
		return image

	def get_solid():
		return solid

	def get_resource():
		return resource

	def get_entrance():
		return entrance


class nav_tile():
	List = []
	total_tiles = 1
	def __init__(self, x, y, walkable, type):
		self.parent = None
		self.x = x
		self.y = y
		self.type = type
		self.H, self.G, self.F = 0,0,0
		self.id = nav_tile.total_tiles
		self.walkable = walkable
		nav_tile.total_tiles += 1
		NAV_LIST.append(self)

def get_nav_tile(tile_id):
	for tile in NAV_LIST:
		if tile.id == tile_id:
			return tile

def get_tile(tile_number):
	for tile in TILE_LIST:
		if tile.tile_number == tile_number:
			return tile

def get_tile_by_id(id):
	for tile in TILE_LIST:
		if tile.id == id:
			return tile