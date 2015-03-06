__author__ = 'Keenin'
import tile as t
import character as c
import pygame

        # move_list = []

        # for x in range(self.x - self.max_mov, self.x + (self.max_mov+1)):
        #     for y in range(self.y - self.max_mov, self.y + (self.max_mov+1)):
        #         if 0<= x <=MAPWIDTH and 0<= y <=MAPHEIGHT:
        #             mov_range = abs(self.x - x) + abs(self.y - y)
        #             if mov_range >= self.min_mov and mov_range <= self.max_mov:
        #                 if 0<=x<MAPWIDTH and 0<=y<MAPWIDTH:
        #                     if m.maps[0][y][x].walkable:
        #                         if monster.List:
        #                             for creep in monster.List:
        #                                 if ((y == creep.y) and (x == creep.x)):
        #                                     break
        #                                 else:
        #                                     tile = m.maps[0][y][x]
        #                                     move_list.append(tile)
        #                                     pygame.draw.circle(SCREEN, (255,255,255), (x * TILE_SIZE + 16, y * TILE_SIZE + 16), 8)



        #     for tile in move_list:
        #         if abs(pygame.mouse.get_pos()[0]/32) == tile.x and abs(pygame.mouse.get_pos()[1]/32) == tile.y:
        #             if event.type == MOUSEBUTTONDOWN:
        #                 print "Player Move"
        #                 am.a_star(self, tile, total_frames, FPS)

def a_star(player, target_tile):

    N = -24
    S = 24
    E = 1
    W = -1

    for tile in t.nav_tile.List:
        tile.parent = None
        tile.H, tile.G, tile.F = 0,0,0

    def manhattan_distance(start_node, end_node):
        return (abs(end_node.x - start_node.x) + abs(end_node.y - start_node.y))

    def get_candidate_tiles(tile):
        candidate_tiles = (
                        (tile.id + N),
                        (tile.id + E),
                        (tile.id + S),
                        (tile.id + W)
                        )

        tiles = []

        for tile in candidate_tiles:
            candidate_tile = t.get_nav_tile(tile)
            if tile not in range(1, t.nav_tile.total_tiles):
                continue

            if candidate_tile.walkable and candidate_tile not in closed_List:
                tiles.append(candidate_tile)

        return tiles

    def G(tile):
        tile.G = tile.parent.G + 10

    def H():
        for tile in t.nav_tile.List:
            tile.H = ((10 * (abs(tile.x - target_tile.x) + abs(tile.y - target_tile.y))))

    def F(tile):
        tile.F = tile.G + tile.H

    def swap(tile):
        open_List.remove(tile)
        closed_List.append(tile)

    def get_LFT():
        f_values = []
        for tile in open_List:
            f_values.append(tile.F)

        o = open_List[::-1]

        for tile in o:
            if tile.F == min(f_values):
                return tile

    def g_cost(LFT, tile):
        gval = LFT.G + 10
        return gval

    def loop():
        LFT = get_LFT()
        swap(LFT)
        candidate_tiles = get_candidate_tiles(LFT)

        for tile in candidate_tiles:
            if tile not in open_List:
                open_List.append(tile)
                tile.parent = LFT

            elif tile in open_List:
                calc_g = g_cost(LFT, tile)
                if calc_g < tile.G:
                    tile.parent = LFT
                    G(tile)
                    F(tile)

        if open_List == [] or target_tile in closed_List:
            return

        for tile in open_List:
            G(tile)
            F(tile)

        loop()


    open_List = []
    closed_List = []

    player_tile = player.get_tile()
    open_List.append(player_tile)
    candidate_tiles = get_candidate_tiles(player_tile)

    for tile in candidate_tiles:
        tile.parent = player_tile
        open_List.append(tile)

    swap(player_tile)
    H()

    for tile in candidate_tiles:
        G(tile)
        F(tile)

    loop()

    return_tiles = []

    parent = target_tile

    while True:
        return_tiles.append(parent)
        parent = parent.parent

        if parent == None:
            break

        if parent.id == player.get_id():
            break

    if len(return_tiles) > 0:
        next_tile = return_tiles[-1]
        player.x = next_tile.x
        player.y = next_tile.y
