from random import randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_gcd_game():
    game_config = {
        "rule": 'Find the greatest common divisor of given numbers.',
        "generate_question": generate_question,
        "get_correct_answer": get_correct_answer,
        "get_user_answer": lambda: prompt.integer("Your answer: "),
    }

    brain_game(**game_config)


def generate_question():
    NUMBER1_MIN = 0
    NUMBER1_MAX = 100
    NUMBER2_MIN = 1
    NUMBER2_MAX = 100

    num1 = randint(NUMBER1_MIN, NUMBER1_MAX)
    num2 = randint(NUMBER2_MIN, NUMBER2_MAX)
    return f'{num1} {num2}'


def get_correct_answer(question):
    a, b = map(int, question.split())
    return gcd(a, b)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
