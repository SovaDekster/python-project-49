import random
import math


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    diapason = range(2, int(math.sqrt(number)) + 1)
    if number <= 1:
        return False
    for elem in diapason:
        if number % elem == 0:
            return False
        return True


def generate_round():
    random_number = random.randint(0, 129)
    if is_prime(random_number) is True:  # E712
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = str(random_number)
    return question, correct_answer
