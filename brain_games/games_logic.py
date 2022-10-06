import prompt


ROUNDS_NUMBER = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(f"{game.RULE}")

    for round in range(ROUNDS_NUMBER):
        (question, correct_answer) = game.generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print("Сorrect!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    return
