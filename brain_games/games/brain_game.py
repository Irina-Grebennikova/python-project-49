from brain_games.cli import welcome_user


def brain_game(rules, generate_question, get_correct_answer, get_user_answer):
    username = welcome_user()
    print(rules)

    for _ in range(3):
        question = generate_question()
        print(f"Question: {question}")

        correct_answer = get_correct_answer(question)
        user_answer = get_user_answer()
        check_result = user_answer == correct_answer

        if check_result:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {username}!"
            )
            return

    print(f"Congratulations, {username}!")