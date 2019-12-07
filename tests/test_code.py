import pytest
""" Quick test verification to ensure appropriate compile-time build. 
Test methods decorated with the pytest.mark.slow descriptor can be ignored by configuring the pytest.ini file - 
This is done to provide an option after initial test verification so that concurrent tests can be executed quicker."""

def test_add_player(game):
    """ Tests that a player can be successfully added into the game. """
    game.add("Michael")
    assert "Michael" in game.players


@pytest.mark.slow
def test_number_of_questions_in_question_type(game):
    """ Tests that the number of questions initializes correctly. """
    for question_type in game.categories_of_questions.keys():
        for num in range(game.number_of_questions):
            assert len(game.types_of_questions[question_type]) == game.number_of_questions


@pytest.mark.slow
def test_question_statements_in_question_type(game):
    """ Tests that the question statements match the question category and question number. """
    for question_type in game.categories_of_questions.keys():
        for num in range(game.number_of_questions):
            assert str(question_type + ' Question ' + str(num)) in game.types_of_questions[question_type][num]


def test_roll_logic(game):
    game.roll(5)
