import math
from .piece import Piece, Side

from collections import defaultdict


class Game(object):
    pass


class TrafficTrauma(Game):
    pass


class Board(object):

    def __init__(self, piece_list: list):
        self.__matrix_size = int(math.sqrt(len(piece_list)))
        self.__piece_table = [[None for _ in range(self.__matrix_size)] for _ in range(self.__matrix_size)]
        self.__unused_pieces = piece_list
        self.__frontier = list()

    def __neighbour_pieces(self, x, y):
        points = self.__neighbours_coordinates(x, y)

        return {d: self.__piece_table[points[d][0]][points[d][1]] for d in points}

    def __neighbours_coordinates(self, x, y):
        points = defaultdict(None)

        if 0 <= x + 1 < self.__matrix_size:
            points[Side.RIGHT] = (x + 1, y)

        if 0 <= x - 1 < self.__matrix_size:
            points[Side.LEFT] = (x - 1, y)

        if 0 <= y + 1 < self.__matrix_size:
            points[Side.UP] = (x, y + 1)

        if 0 <= y - 1 < self.__matrix_size:
            points[Side.DOWN] = (x, y - 1)

        return points

    def valid_action(self, piece: Piece, x, y):
        neighbours = self.__neighbour_pieces(x, y)

        for side in neighbours:
            if not piece.match(neighbours[side], side):
                return False

        return True

    def possible_pieces(self, x, y):
        neighbours = self.__neighbour_pieces(x, y)

        colors = [neighbours[Side.UP].down, neighbours[Side.DOWN].up,
                  neighbours[Side.RIGHT].left, neighbours[Side.LEFT].right]

        if len(colors) == 0:
            return set(self.__unused_pieces)
        else:
            pieces = set()
            for c in colors:
                for p in self.__unused_pieces:
                    if p.has_color(c):
                        pieces.add(p)

            return pieces


    def generate_initial_states(self):
        pass