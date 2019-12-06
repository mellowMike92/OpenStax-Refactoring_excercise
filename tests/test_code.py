from src.Refactoring_exercise.game_logic import Game


def test_add_player(game):
    game.add("Michael")
    assert "Michael" in game.players


def test_number_of_pop_questions(game):
    print(len(game.types_of_questions['Pop']), '\t', game.number_of_questions)
    assert len(game.types_of_questions['Pop']) == game.number_of_questions


def test_number_of_science_questions(game):
    print(len(game.types_of_questions['Science']), '\t', game.number_of_questions)
    assert len(game.types_of_questions['Science']) == game.number_of_questions


def test_number_of_sports_questions(game):
    print(len(game.types_of_questions['Sports']), '\t', game.number_of_questions)
    assert len(game.types_of_questions['Sports']) == game.number_of_questions


def test_number_of_rock_questions(game):
    print(len(game.types_of_questions['Rock']), '\t', game.number_of_questions)
    assert len(game.types_of_questions['Rock']) == game.number_of_questions
