from src.Trivia.tools.roll import Roll


class ProcessAnswer(Roll):
    """ Inherits Roll base class initialization. """

    def __init__(self):
        super().__init__()

    def was_correctly_answered(self):
        """ Determines that the player answered correctly and decides which helper method to execute based on
        conditional checks. """

        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                return self._outside_penalty_box_correct_answer()
            else:
                return self._incrementing_current_player()
        else:
            return self._outside_penalty_box_correct_answer()

    def _incrementing_current_player(self):
        """ Increments the current player's turn to the next player's turn or resets the current_player to 0 after
        the last player takes their turn in order to start the turns over. """

        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        return True

    def _outside_penalty_box_correct_answer(self):
        """ Determines the player was outside of the penalty box and awards the coins based on the correct answer. """

        print("Answer was correct!!!!")
        self.purses[self.current_player] += 1
        print(self.players[self.current_player] +
              ' now has ' +
              str(self.purses[self.current_player]) +
              ' Gold Coins.')
        winner = self._did_player_win()
        self._incrementing_current_player()
        return winner

    def wrong_answer(self):
        """ Determines that the player incorrectly answered the question and places him/her in the penalty box. """

        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        return self._incrementing_current_player()

    def _did_player_win(self):
        """ Check if player won by returning a boolean value of owning 6 gold coins. """

        return not (self.purses[self.current_player] == 6)
