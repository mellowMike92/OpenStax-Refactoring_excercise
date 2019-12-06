from src.Refactoring_exercise.tools.players import Players
from src.Refactoring_exercise.tools.questions import Questions


class Roll(Questions):
    def _init__(self):
        super().__init__()

    @property
    def _current_category(self):
        if self.places[self.current_player] in [0, 4, 8]:
            return 'Pop'

        if self.places[self.current_player] in [1, 5, 9]:
            return 'Science'

        if self.places[self.current_player] in [2, 6, 10]:
            return 'Sports'

        return 'Rock'

    def roll_logic(self, roll):
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
        print("%s is not getting out of the penalty box" % self.players[self.current_player])
        self.is_getting_out_of_penalty_box = False

    def _print_player_roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

    def _print_player_new_location(self):
        print(self.players[self.current_player] +
              '\'s new location is ' +
              str(self.places[self.current_player]))

    def _roll_get_out_of_penalty_box(self, roll):
        self.is_getting_out_of_penalty_box = True
        print("%s is getting out of the penalty box" % self.players[self.current_player])
        self._new_place_out_of_penalty_box(roll)
        self._limit_places_check()

    def _limit_places_check(self):
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12

    def _new_place_out_of_penalty_box(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll

    def _ask_question(self):
        print("The category is %s" % self._current_category)
        print(self.types_of_questions[self._current_category].pop(0))