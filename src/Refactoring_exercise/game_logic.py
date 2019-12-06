#!/usr/bin/env python3

from random import randrange

from src.Refactoring_exercise.tools.players import Players
from src.Refactoring_exercise.tools.questions import Questions


class Game(Players, Questions):
    def __init__(self):
        Players.__init__(self)
        Questions.__init__(self)

    def add(self, player_name):
        Players.add_player(self, player_name)

    def roll(self, roll):
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

    @property
    def _current_category(self):
        if self.places[self.current_player] in [0, 4, 8]:
            return 'Pop'

        if self.places[self.current_player] in [1, 5, 9]:
            return 'Science'

        if self.places[self.current_player] in [2, 6, 10]:
            return 'Sports'

        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
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
            else:
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0
                return True

        else:
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

        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner:
            break
