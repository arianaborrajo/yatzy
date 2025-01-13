import pytest
from src.yatzy import Yatzy

def test_twos():
    '''
    The player scores the sum of the dice that reads two
    '''
    assert 12 == Yatzy(4, 4, 4, 5, 5).fours()
    assert 8 == Yatzy(4, 4, 5, 5, 5).fours()
    assert 4 == Yatzy(4, 5, 5, 5, 5).fours()
    assert 8 == Yatzy(4, 5, 6, 4, 5).fours()