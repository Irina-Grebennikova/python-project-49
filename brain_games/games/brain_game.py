from brain_games.cli import welcome_user


def brain_game(rule, generate_question, get_correct_answer, get_user_answer):
    ROUND_COUNT = 3

    username = welcome_user()
    print(rule)

    for _ in range(ROUND_COUNT):
        question = generate_question()
        print(f"Question: {question}")

        correct_answer = get_correct_answer(question)
        user_answer = get_user_answer()
        check_result = user_answer == correct_answer

        if check_result:
            print("Correct!")
        else:
            fail_message = (
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {username}!"
            )
            print(fail_message)
            return

    print(f"Congratulations, {username}!")
