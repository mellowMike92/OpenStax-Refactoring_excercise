from src.Refactoring_exercise.game_logic import Game


def test_add_player(game):
    game.add("Michael")
    assert "Michael" in game.players


def test_number_of_questions_in_question_type(game):
    for question_type in game.types_of_questions.keys():
        for num in range(game.number_of_questions):
            assert len(game.types_of_questions[question_type]) == game.number_of_questions


def test_question_statements_in_question_type(game):
    for question_type in game.types_of_questions.keys():
        for num in range(game.number_of_questions):
            assert str(question_type + ' Question ' + str(num)) in game.types_of_questions[question_type][num]

