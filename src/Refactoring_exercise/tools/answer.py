from src.Refactoring_exercise.tools.roll import Roll


class ProcessAnswer(Roll):
    """ Inherits Roll base class initialization. """

    def __init__(self):
        super().__init__()

    def was_correctly_answered(self):
        """ Determines that the player answered correctly and decides which helper method to execute based on
        conditional checks. """

        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                return self._correct_outside_penalty_box()
            else:
                return self._current_player_increment()
        else:
            return self._correct_outside_penalty_box()

    def _current_player_increment(self):
        """ Increments the current player's turn or resets it to 0. """

        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        return True

    def _correct_outside_penalty_box(self):
        """ Determines the player was outside of the penalty box and awards the coins based on the correct answer. """

        print("Answer was correct!!!!")
        self.purses[self.current_player] += 1
        print(self.players[self.current_player] +
              ' now has ' +
              str(self.purses[self.current_player]) +
              ' Gold Coins.')
        winner = self._did_player_win()
        self._current_player_increment()
        return winner

    def wrong_answer(self):
        """ Determines that the player incorrectly answered the question and places him/her in the penalty box. """

        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        return self._current_player_increment()

    def _did_player_win(self):
        """ Check if player won by returning a boolean value of owning 6 gold coins. """

        return not (self.purses[self.current_player] == 6)
