from src.Refactoring_exercise.game_logic import Game
import pytest


@pytest.fixture
def game():
    """ Creates an empty Game instance """
    return Game()
