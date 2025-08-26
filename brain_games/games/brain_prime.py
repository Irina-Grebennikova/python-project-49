from math import sqrt
from random import randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_prime_game():
    game_config = {
        "rules": 'Answer "yes" if given number is prime. Otherwise answer "no".',
        "generate_question": lambda: randint(0, 1000),
        "get_correct_answer": lambda question: "yes" if is_prime(question) else "no",
        "get_user_answer": lambda: prompt.string("Your answer: "),
    }

    brain_game(**game_config)


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True
