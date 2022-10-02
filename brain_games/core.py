import prompt


rounds_number = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(f"{game.game_task}")

    for round in range(rounds_number):
        (goal, result) = game.generate_round()
        print(f"Question: {goal}")
        the_answer = prompt.string('Your answer: ')
        if the_answer == result:
            print("Сorrect!")
        else:
            print(f"'{the_answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    return
