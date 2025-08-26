from random import randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_even_game():
    game_config = {
        "rules": 'Answer "yes" if the number is even, otherwise answer "no".',
        "generate_question": lambda: randint(1, 100),
        "get_correct_answer": lambda question: "yes" if is_even(question) else "no",
        "get_user_answer": lambda: prompt.string("Your answer: "),
    }

    brain_game(**game_config)


def is_even(number):
    return number % 2 == 0
