from random import choice, randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_calc_game():
    game_config = {
        "rule": 'What is the result of the expression?',
        "generate_question": generate_question,
        "get_correct_answer": lambda question: eval(question),
        "get_user_answer": lambda: prompt.integer("Your answer: "),
    }

    brain_game(**game_config)


def generate_question():
    NUMBER1_MIN = 10
    NUMBER1_MAX = 100
    NUMBER2_MIN = 0
    NUMBER2_MAX = 10

    num1 = randint(NUMBER1_MIN, NUMBER1_MAX)
    num2 = randint(NUMBER2_MIN, NUMBER2_MAX)
    return f'{num1} {get_operation()} {num2}'


def get_operation():
    OPERATIONS = ["+", "-", "*"]
    return choice(OPERATIONS)
