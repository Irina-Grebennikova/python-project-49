from random import randint
import prompt


def brain_even_game(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    for _ in range(3):
        random_number = get_random_int()
        print(f'Question: {random_number}')

        correct_answer = 'yes' if is_even(random_number) else 'no'
        user_answer = prompt.string('Your answer: ')
        check_result = user_answer == correct_answer

        if check_result:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {username}!")
            return

    print(f'Congratulations, {username}!')


def get_random_int():
    return randint(1, 100)


def is_even(number):
    return number % 2 == 0