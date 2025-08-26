from random import randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_progression_game():
    game_config = {
        'rule': 'What number is missing in the progression?',
        'generate_question': generate_question,
        'get_correct_answer': get_correct_answer,
        'get_user_answer': lambda: prompt.integer('Your answer: '),
    }

    brain_game(**game_config)


def generate_question():
    progression = get_progression()
    question = ' '.join('..' if x is None else str(x) for x in progression)
    return question


def get_progression():
    PROGRESSION_LENGTH = 10
    MIN_FIRST_NUMBER = 0
    MAX_FIRST_NUMBER = 10
    MIN_STEP = 1
    MAX_STEP = 50

    start = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    missing_number_index = randint(0, PROGRESSION_LENGTH - 1)

    progression = []
    for index in range(PROGRESSION_LENGTH):
        current_element = start + index * step
        if index == missing_number_index:
            progression.append(None)
        else:
            progression.append(current_element)

    return progression


def get_correct_answer(question):
    progression = [None if x == '..' else int(x) for x in question.split()]
    return find_missing_number(progression)


def find_missing_number(progression):
    for i, num in enumerate(progression):
        if num is not None:
            continue

        if i == 0:
            _, second, third = progression[:3]
            step = third - second
            return second - step

        if i == len(progression) - 1:
            third_from_end, second_from_end, _ = progression[-3:]
            step = second_from_end - third_from_end
            return second_from_end + step

        prev_num = progression[i - 1]
        next_num = progression[i + 1]
        step = (next_num - prev_num) // 2
        return prev_num + step
