import random
import math


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False

    for elem in range(2, int(math.sqrt(number)) + 1):
        if number % elem == 0:
            return False

    return True


def generate_round():
    random_number = random.randint(0, 129)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = str(random_number)
    return question, correct_answer
