__author__ = 'Keenin'
import tile as t
import character as c
import pygame


def a_star(player):

    N = -24
    S = 24
    E = 1
    W = -1

    for tile in t.TILE_LIST:
        tile.parent = None
        tile.H, tile.G, tile.F = 0,0,0

    def manhattan_distance(start_node, end_node):
        return (abs(end_node.x - start_node.x) + abs(end_node.y - start_node.y))

    def get_candidate_tiles(tile):
        candidate_tiles = (
                        (tile.tile_number + N),
                        (tile.tile_number + E),
                        (tile.tile_number + S),
                        (tile.tile_number + W)
                        )

        tiles = []

        for tile in candidate_tiles:
            candidate_tile = t.get_tile(tile)
            if tile not in range(1, t.tile.total_tiles+1):
                continue

            if candidate_tile.walkable and candidate_tile not in closed_List:
                tiles.append(candidate_tile)

        return tiles

    def G(tile):
        tile.G = tile.parent.G + 10

    def H():
        for tile in t.TILE_LIST:
            tile.H = ((10 * (abs(tile.x - player.x) + abs(tile.y - player.y))))

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

        if open_List == [] or player.get_tile() in closed_List:
            return

        for tile in open_List:
            G(tile)
            F(tile)

        loop()


    for monster in c.monster.List:
        if (abs(monster.x - player.x) + abs(monster.y - player.y)) < 6:
            can_move = True
            open_List = []
            closed_List = []

            monster_tile = monster.get_tile()
            open_List.append(monster_tile)
            candidate_tiles = get_candidate_tiles(monster_tile)

            for tile in candidate_tiles:
                tile.parent = monster_tile
                open_List.append(tile)

            swap(monster_tile)
            H()

            for tile in candidate_tiles:
                G(tile)
                F(tile)

            loop()

            return_tiles = []

            parent = player.get_tile()

            while True:
                return_tiles.append(parent)
                parent = parent.parent

                if parent == None:
                    break

                if parent.tile_number == monster.get_id():
                    break

            if len(return_tiles) > 1:
                if can_move:
                    next_tile = return_tiles[-1]
                    attack_tile = return_tiles[-2]
                    monster.x = next_tile.x
                    monster.y = next_tile.y
                    if attack_tile == player.get_tile():
                        player.HP -= monster.damage
                        can_move = False
