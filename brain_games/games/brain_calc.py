from random import choice, randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_calc_game():
    game_config = {
        "rules": 'What is the result of the expression?',
        "generate_question": lambda: f'{randint(10, 100)} {get_operation()} {randint(0, 10)}',
        "get_correct_answer": lambda question: eval(question),
        "get_user_answer": lambda: prompt.integer("Your answer: "),
    }

    brain_game(**game_config)


def get_operation():
    operations = ["+", "-", "*"]
    return choice(operations)