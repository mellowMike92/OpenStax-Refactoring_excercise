from src.Refactoring_exercise.tools.players import Players
from src.Refactoring_exercise.tools.questions import Questions


class Roll(Questions):
    """ Inherits the Questions base class. """
    def __init__(self):
        super().__init__()

    @property
    def _current_category(self):
        """ Quickly checks the player place and returns the appropriate question category. """

        if self.places[self.current_player] in [0, 4, 8]:
            return 'Pop'

        if self.places[self.current_player] in [1, 5, 9]:
            return 'Science'

        if self.places[self.current_player] in [2, 6, 10]:
            return 'Sports'

        return 'Rock'

    def roll_logic(self, roll):
        """ Handles function calls to extracted helper methods by using a series of conditional checks. """

        self._print_player_roll(roll)
        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self._roll_get_out_of_penalty_box(roll)
            else:
                self._roll_stay_in_penalty_box()
        else:
            self._new_place_out_of_penalty_box(roll)
            self._limit_places_check()

        self._print_player_new_location()
        self._ask_question()

    def _roll_stay_in_penalty_box(self):
        """ Determines that the player stays in the penalty box due to the dice roll and the
        player's position inside the penalty box. """

        print("%s is not getting out of the penalty box" % self.players[self.current_player])
        self.is_getting_out_of_penalty_box = False

    def _print_player_roll(self, roll):
        """ Prints the player's name along with their rolled number. """

        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

    def _print_player_new_location(self):
        """ Prints the player's new location after each player roll. """
        print(self.players[self.current_player] +
              '\'s new location is ' +
              str(self.places[self.current_player]))

    def _roll_get_out_of_penalty_box(self, roll):
        """ Determines that the player can leave the penalty box due to the dice roll. """

        self.is_getting_out_of_penalty_box = True
        print("%s is getting out of the penalty box" % self.players[self.current_player])
        self._new_place_out_of_penalty_box(roll)
        self._limit_places_check()

    def _limit_places_check(self):
        """ Performs the check relevant to the player's place and limits it below 12."""

        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12

    def _new_place_out_of_penalty_box(self, roll):
        """ Sets a new player place due to the roll and the player not being inside the penalty box. """
        self.places[self.current_player] = self.places[self.current_player] + roll

    def _ask_question(self):
        """ Prepares the next category question """

        print("The category is %s" % self._current_category)
        print(self.categories_of_questions[self._current_category].pop(0))