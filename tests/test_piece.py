import pytest

from stupid_cockroach.piece import Piece, Colors

def test_copy():
    x = Piece(Colors.BLACK, Colors.GREEN, Colors.PINK, Colors.RED)
    y = x.rotate()
    assert x != y


def test_rotate_all():
    x = Piece(Colors.BLACK, Colors.GREEN, Colors.PINK, Colors.RED)
    y = x.rotate()
    for _ in range(3):
        y = y.rotate()
    assert x == y