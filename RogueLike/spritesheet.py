import pygame

class spritesheet(object):
	def __init__(self, filename):
		try:
			self.sheet = pygame.image.load(filename).convert()
		except pygame.error, message:
			print "Unable to load spritesheet image: ", filename
			raise SystemExit, message
	#Load a specific image from a specific rectangle
	def image_at(self, rectangle):
		#Loads image from x, y, x+offset, y+offset
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0,0), rect)
		return image