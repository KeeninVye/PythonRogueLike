import pygame, math, sys, random
#import spritesheet
import mapgenerator as MAP
import items as i
import inventory as inv
import spells as s
import spellbar as sb
import tile as t
import character as char
from pygame.locals import *

m = MAP.generator()

#Constants for colors
BLACK = (0,0,0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#Setup the display
pygame.init()
gamefont = pygame.font.SysFont("monospace", 15)
MAPWIDTH = 24
MAPHEIGHT = 24
SCREENWIDTH = 30
SCREENHEIGHT = 24
TILE_SIZE = 32
SCREEN = pygame.display.set_mode((MAPWIDTH * TILE_SIZE + 192, MAPHEIGHT * TILE_SIZE))
FONT = pygame.font.SysFont("monospace", 15)

#Constants of tiles, starting at 0
DIRT = 0
GRASS = 1
WATER = 2
STONE = 3
SHOP = 4

#Constants for monsters, starting at 100
PLAYER = 100
BEETLE = 101
BEETLE2 = 102

#Constants for items, starting at 200
HEALTH_POT = 200
MANA_POT = 201
#Weapons are from 220 to 249
STONE_SWORD = 220
#Armor is from 250 to 299
WORN_SHIRT = 250
PANTS = 260
BOOTS = 270

#Constants for Magic, Starting at 300
FIRE_NOVA = 300

#Constants for GUI, starting at 400
CURSOR = 400
STAT = 401
HEALTHBAR = 402
#used in items dictionary
OPENSLOT = 402
OPENMAGIC = 403

# #Sprite sheets
# tile_sheet = spritesheet.spritesheet('images/terrain_tile.png')
# monster_sheet = spritesheet.spritesheet('images/monster_tile.png')
# npc_sheet = spritesheet.spritesheet('images/npc_tile.png')
# gui_sheet = spritesheet.spritesheet('images/cursor.png')

#GUI constants
gui_sprites = {
			CURSOR : pygame.image.load("images/misc/cursor.png").convert_alpha(),
            STAT : pygame.image.load("images/stat.png").convert_alpha(),
            #HEALTHBAR : pygame.image.load("images/misc/mdam_not_damaged.png").convert_alpha()
			}

# #Constants for textures
# TILES = {
#             DIRT : t.tile("Dirt", 0, pygame.image.load("images/dungeon/floor/grass/grass_full.png").convert_alpha(), False),
#             GRASS : t.tile("Grass", 1, pygame.image.load("images/dungeon/floor/grass/grass_flowers_red1.png").convert_alpha(), False),
#             WATER : t.tile("Water", 2, pygame.image.load("images/dungeon/water/shallows1.png").convert_alpha(), True),
#             STONE : t.tile("Stone", 3, pygame.image.load("images/dungeon/floor/cobble_blood1.png").convert_alpha(), True)
#             }

#Monster objects    npc_sheet.image_at((1 * TILE_SIZE, 0 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
monsters = {
            PLAYER : char.player(pygame.image.load("images/player/base/human_m.png").convert_alpha(), MAPWIDTH/2, MAPHEIGHT/2, 10, MAPWIDTH, MAPHEIGHT, "You, an Adventurer."),
            BEETLE : char.monster(pygame.image.load("images/monsters/animals/boring_beetle.png").convert_alpha(), 9, 6, 2, 1, MAPWIDTH, MAPHEIGHT, "Beetle, weak shell.", True),
            BEETLE2 : char.monster(pygame.image.load("images/monsters/animals/boring_beetle.png").convert_alpha(), 9, 8, 2, 1, MAPWIDTH, MAPHEIGHT, "Beattle, weak shell.", True)
            }
#item objects
ITEMS = {
        STONE_SWORD : i.weapon("Stone Sword", 220, "+1 Damage", pygame.image.load("images/player/hand1/sword2.png").convert_alpha(), (1,2), 1),

        WORN_SHIRT : i.armor("Green Shirt", 250, "+1 Defense", pygame.image.load("images/player/body/shirt_vest.png").convert_alpha(), (0,1), 1, "Leather"),

        PANTS : i.armor("Brown Pants", 260, "+1 Defense", pygame.image.load("images/player/legs/pants_brown.png").convert_alpha(), (1,0), 1, "Cloth"),

        BOOTS : i.armor("Grey Boots", 270, "+1 Defense", pygame.image.load("images/player/boots/middle_gray.png").convert_alpha(), (1,1), 1, "Leather"),

        OPENSLOT : i.item("Open Slot", 402, "Empty Slot", pygame.image.load("images/misc/slot.png").convert_alpha(), 9)
        }

MAGIC = {
        FIRE_NOVA : s.magic("Fire Nova", 300, pygame.image.load("images/spells/fire/fireball.png").convert_alpha(), 1, "AOE"),
        OPENMAGIC : s.magic("Open Magic Slot", 403, pygame.image.load("images/misc/slot_magic.png").convert_alpha(), 1, "AOE")

        }


#Generate map and store it
TILE_MAP = m.do(MAPWIDTH, MAPHEIGHT)

#TEST puts items in backpack
inv.BACKPACK[0][0] = STONE_SWORD
inv.BACKPACK[0][1] = WORN_SHIRT
inv.BACKPACK[0][2] = PANTS
inv.BACKPACK[0][3] = BOOTS

#TEST learns spell
sb.MAGIC[0][0] = FIRE_NOVA

while True:

    #Loop to draw tiles
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            image = TILE_MAP[row][column].image
            SCREEN.blit(image, (column * TILE_SIZE, row * TILE_SIZE))

    SCREEN.blit(gui_sprites[STAT], (MAPWIDTH*TILE_SIZE, 0))

    #Loop to draw inventory slots
    for row in range(MAPHEIGHT/2):
        for column in range(4):
            SCREEN.blit(ITEMS[inv.BACKPACK_SLOT[row][column]].image, (((MAPWIDTH + 1) * TILE_SIZE) + (column * TILE_SIZE), (row + 4) * TILE_SIZE))

     #Loop to draw inventory items
    for row in range(MAPHEIGHT/2):
        for column in range(4):
            SCREEN.blit(ITEMS[inv.BACKPACK[row][column]].image, (((MAPWIDTH + 1) * TILE_SIZE) + (column * TILE_SIZE), (row + 4) * TILE_SIZE))

    #Loop to draw Armor slots
    for row in range(2):
        for column in range(4):
            SCREEN.blit(ITEMS[inv.ARMOR_SLOT[row][column]].image, (((MAPWIDTH + 1) * TILE_SIZE) + (column * TILE_SIZE), (row + 17) * TILE_SIZE))

     #Loop to draw Armor items
    for row in range(2):
        for column in range(4):
            SCREEN.blit(ITEMS[inv.ARMOR[row][column]].image, (((MAPWIDTH + 1) * TILE_SIZE) + (column * TILE_SIZE), (row + 17) * TILE_SIZE))

    #Loop to draw Magic slots
    for row in range(2):
        for column in range(4):
            SCREEN.blit(MAGIC[sb.MAGIC_SLOT[row][column]].image, (((MAPWIDTH + 1) * TILE_SIZE) + (column * TILE_SIZE), (row + 20) * TILE_SIZE))

     #Loop to draw Magic items
    for row in range(2):
        for column in range(4):
            SCREEN.blit(MAGIC[sb.MAGIC[row][column]].image, (((MAPWIDTH + 1) * TILE_SIZE) + (column * TILE_SIZE), (row + 20) * TILE_SIZE))

    monsters[PLAYER].move(monsters[PLAYER], SCREEN)

    #Display the Player and Monsters
    SCREEN.blit(monsters[PLAYER].image, (monsters[PLAYER].x * TILE_SIZE, monsters[PLAYER].y * TILE_SIZE))
    #SCREEN.blit(gui_sprites[HEALTHBAR], (monsters[PLAYER].x * TILE_SIZE, (monsters[PLAYER].y-1) * TILE_SIZE))

    #Updating the text
    hptext = gamefont.render("Health: " + str(monsters[PLAYER].HP), 1, (255, 255, 0))
    strtext = gamefont.render("Damage: " + str(monsters[PLAYER].STR), 1, (255, 255, 255))
    actext = gamefont.render("Armor: " + str(monsters[PLAYER].AC), 1, (255, 255, 255))

    #Display Stats
    SCREEN.blit(hptext, ((MAPWIDTH+1)*TILE_SIZE, TILE_SIZE))
    SCREEN.blit(strtext, ((MAPWIDTH+1)*TILE_SIZE, TILE_SIZE*1.75))
    SCREEN.blit(actext, ((MAPWIDTH+1)*TILE_SIZE, TILE_SIZE*2.5))

    for gear in inv.ARMOR:
        for armor in gear:
            for item in ITEMS:
                if item == armor and not item == 402:
                    SCREEN.blit(ITEMS[item].image, (monsters[PLAYER].x * TILE_SIZE, monsters[PLAYER].y * TILE_SIZE))
        
    for npc in char.monster.List:
        SCREEN.blit(npc.image, (npc.x * TILE_SIZE, npc.y * TILE_SIZE))
        if (abs(pygame.mouse.get_pos()[0]/32) == npc.x) and (abs(pygame.mouse.get_pos()[1]/32) == npc.y):
            if npc == PLAYER:
                gui_sprites[CURSOR] = pygame.image.load("images/misc/cursor_green.png").convert_alpha()
            elif npc.harmful:
                gui_sprites[CURSOR] = pygame.image.load("images/misc/cursor_red.png").convert_alpha()
            elif not npc.harmful:
                gui_sprites[CURSOR] = pygame.image.load("images/misc/cursor_green.png").convert_alpha()
            info = FONT.render(npc.info(), 1, (255,255,0))

            SCREEN.blit(info, (MAPWIDTH * TILE_SIZE+12, (MAPHEIGHT - 1) * TILE_SIZE))
            break
        else:
            gui_sprites[CURSOR] = pygame.image.load("images/misc/cursor.png").convert_alpha()
    #Display the cursor
    SCREEN.blit(gui_sprites[CURSOR], (abs(pygame.mouse.get_pos()[0]/32) * TILE_SIZE, abs(pygame.mouse.get_pos()[1]/32) * TILE_SIZE))
    

    #update the display
    pygame.display.update()