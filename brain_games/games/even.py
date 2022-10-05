import random

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = random.randint(1, 100)
    goal = number
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return goal, result
