from src.Trivia.trivia_game import Game
import pytest


@pytest.fixture
def game():
    """ Creates an empty Game instance to be used with test_code.py. """
    return Game()
