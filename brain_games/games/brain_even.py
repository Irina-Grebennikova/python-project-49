from random import randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_even_game():
    game_config = {
        "rule": 'Answer "yes" if the number is even, otherwise answer "no".',
        "generate_question": generate_question,
        "get_correct_answer": get_correct_answer,
        "get_user_answer": lambda: prompt.string("Your answer: "),
    }

    brain_game(**game_config)


def generate_question():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    return randint(MIN_NUMBER, MAX_NUMBER)


def get_correct_answer(question):
    return "yes" if is_even(question) else "no"


def is_even(number):
    return number % 2 == 0
