#!/usr/bin/env python3

from random import randrange
from src.Trivia.tools.answer import ProcessAnswer
from src.Trivia.tools.players import Players
from src.Trivia.tools.roll import Roll


class Game(ProcessAnswer):
    """ Inherits from the ProcessAnswer base class. """
    def __init__(self):
        super().__init__()

    def add(self, player_name):
        """ Adds a player with a specified player_name to the trivia game by appending to the Players.players list. """
        Players.add_player(self, player_name)

    def roll(self, roll_number):
        """ Handles the logic behind rolling the dice.  Calls the roll_logic method in the Roll class with the specified
        roll number. """
        Roll.roll_logic(self, roll_number)


""" 

#  The main block has been copied into __main__.py, but the code will be left here for future testing/development.

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
             
"""
