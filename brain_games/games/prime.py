import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = random.randint(0, 129)
    diapason = range(2, random_number)
    correct_answer = ''
    if random_number == 0 and random_number == 1:
        correct_answer = 'no'
    for elem in diapason:
        if random_number % elem == 0:
            correct_answer = 'no'
            break
        correct_answer = 'yes'
    question = random_number
    return str(question), correct_answer
