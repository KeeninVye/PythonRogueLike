import pygame, math, sys, random, spritesheet
from pygame.locals import *
import tile as t
import mapgenerator as m
from mapgenerator import maps
import items as i
import inventory as inv
import astar_movement_monster as a
import astar_movement as am









MAPWIDTH = 24
MAPHEIGHT = 24
TILE_SIZE = 32
MAP = 0
player = None

class base(object):
	def __init__(self, image, x, y, health, MAPWIDTH, MAPHEIGHT, INFO):
		self.image = image
		self.x = x
		self.y = y
		self.MAPWIDTH = MAPWIDTH
		self.MAPHEIGHT = MAPHEIGHT
		self.INFO = INFO

	def info(self):
		return self.INFO
		#label = 


class monster(base):
    
    List = []
    
    def __init__(self, image, x, y, health, damage, MAPWIDTH, MAPHEIGHT, INFO, HARMFUL):
        self.image = image
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.MAPWIDTH = MAPWIDTH
        self.MAPHEIGHT = MAPHEIGHT
        self.INFO = INFO
        self.harmful = HARMFUL
        monster.List.append(self)

    def getx():
        return x

    def get_id(self):
        return maps[0][self.y][self.x].tile_number

    def get_tile(self):
        return maps[0][self.y][self.x]

    def move(self):



        candidate_tiles = []
        current_tile = candidate_tile(self.x, self.y, MAP)
        candidate_tiles.append(current_tile)
        candidate_tiles = [m.maps[MAP][self.y][self.x+1], m.maps[MAP][self.y][self.x-1], m.maps[MAP][self.y+1][self.x], m.maps[MAP][self.y-1][self.x]]
        
        for tile in candidate_tiles:
            if t.get_tile(tile).solid:
                candidate_tiles.remove(tile)


def kill(self):
    del(self)

def monster_move(player):
    a.a_star(player)



class player(base):
    def __init__(self, image, x, y, health, MAPWIDTH, MAPHEIGHT, INFO):
        self.image = image
        self.x = x
        self.y = y
        self.MAPWIDTH = MAPWIDTH
        self.MAPHEIGHT = MAPHEIGHT
        self.INFO = INFO
        self.HP = 100
        self.STR = 1
        self.CRIT = 1
        self.AGIL = 1
        self.INTL = 1
        self.AC = 0
        self.min_mov = 1
        self.max_mov = 4
        player = self

    def get_id(self):
        return maps[0][self.y][self.x].tile_number

    def get_tile(self):
        return maps[0][self.y][self.x]

    def move(self, player, SCREEN):

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == KEYDOWN:
                can_move = True
                if(event.key == K_RIGHT) and self.x < self.MAPWIDTH - 1:
                    if not monster.List:
                        if (m.maps[0][self.y][self.x+1]).walkable == False:
                            pass
                        else:
                            self.x += 1
                            monster_move(player)
                    elif monster.List:
                        for creep in monster.List:
                            if ((not self.y == creep.y) or (not self.x + 1 == creep.x)):
                                pass
                            else:
                                can_move = False
                                creep.health -= self.STR
                                self.HP -= creep.damage
                                monster_move(player)
                                if creep.health <= 0:
                                    kill(creep)
                                    monster.List.remove(creep)
                        if (m.maps[0][self.y][self.x+1]).walkable == False:
                            pass
                        elif can_move:
                            self.x += 1
                            monster_move(player)

                elif(event.key == K_LEFT) and self.x > 0:
                    if not monster.List:
                        if (m.maps[0][self.y][self.x-1]).walkable == False:
                            pass
                        else:
                            self.x -= 1
                            monster_move(player)
                    elif monster.List:
                        for creep in monster.List:
                            if ((not self.y == creep.y) or (not self.x - 1 == creep.x)):
                                pass
                            else:
                                can_move = False
                                creep.health -= self.STR
                                self.HP -= creep.damage
                                monster_move(player)
                                if creep.health <= 0:
                                    kill(creep)
                                    monster.List.remove(creep)
                        if (m.maps[0][self.y][self.x-1]).walkable == False:
                            pass
                        elif can_move:
                            self.x -= 1
                            monster_move(player)
                        
                elif(event.key == K_UP) and self.y > 0:
                    if not monster.List:
                        if (m.maps[0][self.y-1][self.x]).walkable == False:
                            pass
                        else:
                            self.y -= 1
                            monster_move(player)
                    elif monster.List:
                        for creep in monster.List:
                            if ((not self.x == creep.x) or (not self.y - 1 == creep.y)):
                                pass
                            else:
                                can_move = False
                                creep.health -= self.STR
                                self.HP -= creep.damage
                                monster_move(player)
                                if creep.health <= 0:
                                    kill(creep)
                                    monster.List.remove(creep)
                                
                        if (m.maps[0][self.y-1][self.x]).walkable == False:
                            pass
                        elif can_move:
                            self.y -= 1
                            monster_move(player)


                elif(event.key == K_DOWN) and self.y < self.MAPHEIGHT -1:
                    if not monster.List:
                        if (m.maps[0][self.y+1][self.x]).walkable == False:
                            pass
                        else:                            
                            self.y += 1
                            monster_move(player)
                    elif monster.List:
                        for creep in monster.List:
                            if ((not self.x == creep.x) or (not self.y + 1 == creep.y)):
                                pass
                            else:
                                can_move = False
                                creep.health -= self.STR
                                self.HP -= creep.damage
                                monster_move(player)
                                if creep.health <= 0:
                                    kill(creep)
                                    monster.List.remove(creep)
                        if (m.maps[0][self.y+1][self.x]).walkable == False:
                            pass
                        elif can_move:
                            self.y += 1
                            monster_move(player)

            #Check to see if you click in inventory
            if (((MAPWIDTH * TILE_SIZE) + 32)/32 <= abs(pygame.mouse.get_pos()[0]/32) <= ((MAPWIDTH * TILE_SIZE) + 160)/32) and ((4 * TILE_SIZE)/32 <= (abs(pygame.mouse.get_pos()[1]/32)) <= (15 * TILE_SIZE)/32):
                if event.type == MOUSEBUTTONDOWN:
                    #Need -25 and -4 to go to origin [0,0] for Inventory List
                    inv_y = abs(pygame.mouse.get_pos()[0]/32) - 25
                    inv_x = abs(pygame.mouse.get_pos()[1]/32) - 4
                    if pygame.mouse.get_pressed()[2] == 1:
                        item_id = inv.BACKPACK[inv_x][inv_y]
                        if not item_id == 402:
                            item = i.get_item(item_id)
                            if i.is_armor(item):
                                self.AC+=item.armor
                            elif i.is_weapon(item):
                                self.STR+=item.damage 
                            slot_x = item.slot[0]
                            slot_y = item.slot[1]
                            replacement = inv.ARMOR[slot_x][slot_y]
                            inv.ARMOR[slot_x][slot_y] = item_id
                            inv.BACKPACK[inv_x][inv_y] = replacement
                            print "Damage: " + str(self.STR)
                            print "Armor: " + str(self.AC)

            #Check to see if you click in Armor
            if (((MAPWIDTH * TILE_SIZE) + 32)/32 <= abs(pygame.mouse.get_pos()[0]/32) <= ((MAPWIDTH * TILE_SIZE) + 160)/32) and ((17 * TILE_SIZE)/32 <= (abs(pygame.mouse.get_pos()[1]/32)) <= (18 * TILE_SIZE)/32):
                if event.type == MOUSEBUTTONDOWN:
                    #Need -25 and -17 to go to origin [0,0] for Armor List
                    armor_y = abs(pygame.mouse.get_pos()[0]/32) - 25
                    armor_x = abs(pygame.mouse.get_pos()[1]/32) - 17
                    if pygame.mouse.get_pressed()[2] == 1:
                        item_id = inv.ARMOR[armor_x][armor_y]
                        if not item_id == 402:
                            item = i.get_item(item_id)
                            if i.is_armor(item):
                                self.AC-=item.armor
                            elif i.is_weapon(item):
                                self.STR-=item.damage
                            slot_x = item.slot[0]
                            slot_y = item.slot[1]
                            loop = True
                            for row in range(12):
                                for column in range(4):
                                    if inv.BACKPACK[row][column] == 402 and loop == True:
                                        replacement = inv.BACKPACK[row][column]
                                        inv.BACKPACK[row][column] = item_id
                                        inv.ARMOR[slot_x][slot_y] = replacement
                                        loop = False
                                        print "Damage: " + str(self.STR)
                                        print "Armor: " + str(self.AC)


	def getx(self):
		return self.x


