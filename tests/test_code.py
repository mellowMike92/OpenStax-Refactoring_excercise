from random import randrange
import pytest
"""
Test methods decorated with the pytest.mark.slow descriptor can be ignored by configuring the pytest.ini file - 
This is done to provide an option after initial test verification so that concurrent tests can be executed quicker.
"""


def test_add_player(game):
    """
    Tests that a player can be successfully added into the game.
    :param game: Constructs game instance
    :return: Assert that Joe is in the ``players`` class attribute list
    """
    game.add("Joe")
    assert "Joe" in game.players


@pytest.mark.slow
def test_number_of_questions_in_question_category(game):
    """
    Tests that the number of questions initializes correctly.
    :param game: Constructs game instance
    :return: Assert that the number of questions is constructed correctly
    """
    for question_category in game.question_categories.keys():
        for num in range(game.number_of_questions):
            assert len(game.question_categories[question_category]) == game.number_of_questions


@pytest.mark.slow
def test_question_statements_in_question_category(game):
    """
    Tests that the question statements are constructed properly
    with the question category and question number.
    :param game: Constructs game instance
    :return: Assert that the game instance is constructed with the appropriate question category statements.
    """
    for question_category in game.question_categories.keys():
        for num in range(game.number_of_questions):
            assert str(question_category + ' Question ' + str(num)) in game.question_categories[question_category][num]


def test_roll_ask_pop_category(game):
    """
    Tests that the appropriate categories are called based on the player's roll summation / place.
    Rolls 0 first, then 4, then 4 resulting in the places 0, 4, and 8 which correlate with the Pop category.
    :param game: Constructs game instance
    :return: Assert ``Pop`` is returned for every consecutive roll.
    """
    game.add('Chet')
    game.roll(0)
    assert game._current_category == 'Pop'
    game.roll(4)
    assert game._current_category == 'Pop'
    game.roll(4)
    assert game._current_category == 'Pop'


def test_roll_ask_science_category(game):
    """
    Tests that the appropriate categories are called based on the player's roll summation / place.
    Rolls 1 first, then 4, then 4 resulting in the places 0, 4, and 8 which correlate with the Pop category.
    :param game: Constructs game instance
    :return: Assert ``Science`` is returned for every consecutive roll.
    """

    game.add('Sue')
    game.roll(1)
    assert game._current_category == 'Science'
    game.roll(4)
    assert game._current_category == 'Science'
    game.roll(4)
    assert game._current_category == 'Science'


def test_roll_ask_sports_category(game):
    """
    Tests that the appropriate categories are called based on the player's roll summation / place.
    Rolls 2 first, then 4, then 4 resulting in the places 0, 4, and 8 which correlate with the Pop category.
    :param game: Constructs game instance
    :return: Assert ``Sports`` is returned for every consecutive roll.
    """

    game.add('Pat')
    game.roll(2)
    assert game._current_category == 'Sports'
    game.roll(4)
    assert game._current_category == 'Sports'
    game.roll(4)
    assert game._current_category == 'Sports'


def test_roll_ask_rock_category(game):
    """
    Tests that the appropriate categories are called based on the player's roll summation / place.
    Rolls 3 first, then 4, then 4 resulting in the places 3, 7 and 11 which correlate with the Rock category.
    :param game: Constructs game instance
    :return: Assert ``Rock`` is returned for every consecutive roll.
    """

    game.add('Mike')
    game.roll(3)
    assert game._current_category == 'Rock'
    game.roll(4)
    assert game._current_category == 'Rock'
    game.roll(4)
    assert game._current_category == 'Rock'


def test_wrong_answer_increment_current_player(game):
    """
    Tests that the wrong answer returns an increment to player's turn.
    :param game: Constructs game instance
    :return: Assert game._incrementing_current_player() is True
    """

    game.add("Luke")
    bad_luck = True
    game.roll(4)
    if bad_luck is True:
        game.wrong_answer()
        assert game._incrementing_current_player() is True


def test_wrong_answer_increment_to_next_player_turn(game):
    """
    Tests that the wrong answer correctly switches to the next player's turn and comes back to
    the first player's turn after the last player's turn.
    :param game: Constructs game instance
    :return: Assert current_player increments between players.
    """

    game.add("Henry")
    game.add("Paul")
    bad_luck = True
    game.roll(4)
    if bad_luck is True:
        game.wrong_answer()
        assert game.current_player == 1
    game.roll(3)
    if bad_luck is True:
        game.wrong_answer()
        assert game.current_player == 0


def test_correctly_answered_outside_penalty_box(game):
    """
    Tests that the player is outside of the penalty box when answering correctly.
    :param game: Constructs game instance
    :return: Assert game.in_penalty_box[0] is not True
    """

    game.add("Jordan")
    game.roll(8)
    game.was_correctly_answered()
    assert game.in_penalty_box[0] is not True


def test_correctly_answered_gold_awarded(game):
    """
    Tests that the player receives a gold coin after answering correctly.
    :param game: Constructs game instance
    :return: Assert game.purses[0] == 1
    """

    game.add("Tim")
    game.roll(6)
    game.was_correctly_answered()
    assert game.purses[0] == 1


def test_wrong_answer_go_to_penalty_box(game):
    """
    Tests that the player goes to the penalty box after answering incorrectly.
    :param game: Constructs game instance
    :return: Assert game.in_penalty_box[0] is True
    """

    game.add("Brian")
    bad_luck = True
    game.roll(4)
    if bad_luck is True:
        game.wrong_answer()
        assert game.in_penalty_box[0] is True


def test_wrong_answer_no_gold_awarded(game):
    """
    Tests that the player does not receive a gold coin after answering incorrectly.
    :param game: Constructs game instance
    :return: Assert game.purses[0] == 0
    """

    game.add("Mark")
    bad_luck = True
    game.roll(5)
    if bad_luck is True:
        game.wrong_answer()
        assert game.purses[0] == 0


def test_roll_odd_get_out_of_penalty_box(game):
    """
    Tests that the player gets out of the penalty box when rolling an odd number.
    :param game: Constructs game instance
    :return: Assert game.is_getting_out_of_penalty_box is True
    """
    game.add("Rudy")
    bad_luck = True
    game.roll(5)
    if bad_luck is True:
        game.wrong_answer()
    game.roll(3)
    assert game.is_getting_out_of_penalty_box is True


def test_roll_odd_new_place_out_of_penalty_box(game):
    """
    Tests that the player is allocated the correct place outside of penalty box according to the roll.
    :param game: Constructs game instance
    :return: Assert prev_roll + current_roll == game.places[0]
    """
    game.add("Rudy")
    bad_luck = True
    prev_roll = 5
    game.roll(prev_roll)
    if bad_luck is True:
        game.wrong_answer()
    current_roll = 3
    game.roll(current_roll)
    assert prev_roll + current_roll == game.places[0]


def test_player_wins(game):
    """
    Tests that the player with 6 gold coins wins the game.
    :param game: Constructs game instance
    :return: Assert game._did_player_win() is False
    """
    game.add("Leo")
    game.purses[0] = 6
    assert game._did_player_win() is False
