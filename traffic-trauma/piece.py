import enum
import copy


class Colors(enum.Enum):
    GREEN = 0
    PINK = 1
    PURPLE = 2
    ORANGE = 3
    RED = 4
    BLACK = 5
    YELLOW = 6
    WHITE = 7


class Side(enum.Enum):
    UP = 'u'
    RIGHT = 'r'
    DOWN = 'd'
    LEFT = 'l'


class Piece(object):

    counter = 0

    def __init__(self, up: Colors, right: Colors, down: Colors, left: Colors):
        self.__up = up
        self.__right = right
        self.__down = down
        self.__left = left
        self.__cached_colors = (up, right, down, left)
        self.__id = Piece.counter + 1

    def __eq__(self, other):
        if isinstance(other, Piece):
            return self.up == other.up and self.right == other.right \
                   and self.down == other.down and self.left == other.left
        return False

    def unique_colors(self):
        return set(self.__cached_colors)

    def match(self, other_piece, direction):
        if not other_piece:
            return True

        if direction == Side.UP:
            return self.up == other_piece.down

        elif direction == Side.DOWN:
            return self.down == other_piece.up

        elif direction == Side.RIGHT:
            return self.right == other_piece.left

        elif direction == Side.LEFT:
            return self.left == other_piece.right

        else:
            raise ValueError('Wrong direction value')

    @property
    def up(self):
        return self.__up

    @up.setter
    def up(self, value: Colors):
        self.__up = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value: Colors):
        self.__right = value

    @property
    def down(self):
        return self.__down

    @down.setter
    def down(self, value: Colors):
        self.__down = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    def has_color(self, color):
        return color in self.__cached_colors

    def rotate(self):
        """
        Rotate the piece right.

        :return:
        """
        new_piece = copy.copy(self)
        new_piece.up, new_piece.right, new_piece.down, new_piece.left = self.left, self.up, self.right, self.down
        return new_piece

    def __repr__(self):
        return f'Piece({self.up},{self.right},{self.down}, {self.left})'
