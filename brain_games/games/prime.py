import random


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    prime_number = random.randint(0, 129)
    diapason = range(2, prime_number)
    if prime_number == 0 and prime_number == 1:
        result = 'no'
    for elem in diapason:
        if prime_number % elem == 0:
            result = 'no'
            break
        result = 'yes'
    goal = prime_number
    return str(goal), result
