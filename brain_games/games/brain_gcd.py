from random import randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_gcd_game():
    game_config = {
        "rules": 'Find the greatest common divisor of given numbers.',
        "generate_question": lambda: f'{randint(0, 100)} {randint(1, 100)}',
        "get_correct_answer": get_correct_answer,
        "get_user_answer": lambda: prompt.integer("Your answer: "),
    }

    brain_game(**game_config)


def get_correct_answer(question):
    a, b = map(int, question.split())
    return gcd(a, b)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a