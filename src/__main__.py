from random import randrange
# from src.Refactoring_exercise import tools
# from src.Refactoring_exercise.tools import answer
# from src.Refactoring_exercise.tools import questions
# from src.Refactoring_exercise.tools import players
# from src.Refactoring_exercise.tools import roll
from src.Refactoring_exercise.game_logic import Game
# from src.Refactoring_exercise.tools.answer import ProcessAnswer
# from src.Refactoring_exercise.tools.players import Players
# from src.Refactoring_exercise.tools.roll import Roll

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
