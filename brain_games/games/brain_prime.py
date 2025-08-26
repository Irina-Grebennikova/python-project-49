from math import sqrt
from random import randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_prime_game():
    game_config = {
        "rule": 'Answer "yes" if given number is prime. Otherwise answer "no".',
        "generate_question": generate_question,
        "get_correct_answer": get_correct_answer,
        "get_user_answer": lambda: prompt.string("Your answer: "),
    }

    brain_game(**game_config)


def generate_question():
    MIN_NUMBER = 0
    MAX_NUMBER = 1000
    return randint(MIN_NUMBER, MAX_NUMBER)


def get_correct_answer(question):
    return "yes" if is_prime(question) else "no"


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True
