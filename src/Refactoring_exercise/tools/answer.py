from src.Refactoring_exercise.tools.roll import Roll


class ProcessAnswer(Roll):

    def _init__(self):
        super()._init__()

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                return self._correct_outside_penalty_box()
            else:
                return self._current_player_increment()
        else:
            return self._correct_outside_penalty_box()

    def _current_player_increment(self):
        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        return True

    def _correct_outside_penalty_box(self):
        print("Answer was correct!!!!")
        self.purses[self.current_player] += 1
        print(self.players[self.current_player] +
              ' now has ' +
              str(self.purses[self.current_player]) +
              ' Gold Coins.')
        winner = self._did_player_win()
        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        return self._current_player_increment()

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)