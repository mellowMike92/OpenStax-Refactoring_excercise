from src.Refactoring_exercise.game_logic import Game


def test_add_player(game):
    game.add("Michael")
    assert "Michael" in game.players

# def test_initialize_questions()