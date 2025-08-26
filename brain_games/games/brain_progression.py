from random import randint

import prompt

from brain_games.games.brain_game import brain_game


def brain_progression_game():
    game_config = {
        "rules": 'What number is missing in the progression?',
        "generate_question": generate_question,
        "get_correct_answer": get_correct_answer,
        "get_user_answer": lambda: prompt.integer("Your answer: "),
    }

    brain_game(**game_config)


def generate_question():
    progression = get_progression()
    question = " ".join(map(lambda x: str(x) if x is not None else "..", progression))
    return question


def get_progression():
    progression_length = 10

    start = randint(0, 10)
    step = randint(1, 50)
    missing_number_index = randint(0, progression_length - 1)

    progression = []
    for index in range(progression_length):
        current_element = start + index * step
        if index == missing_number_index:
            progression.append(None)
        else:
            progression.append(current_element)

    return progression


def get_correct_answer(question):
    progression = list(map(lambda x: None if x == '..' else int(x), question.split()))
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

        previous = progression[i - 1]
        next = progression[i + 1]
        step = (next - previous) // 2
        return previous + step