import random


RULE = 'What is the result of the expression?'


def generate_round():
    operators = ['+', '-', '*']
    x = random.randint(35, 70)
    y = random.randint(1, 35)
    random_operator = random.choice(operators)
    question = f"{x} {random_operator} {y}"
    if random_operator == '+':
        correct_answer = x + y
    elif random_operator == '-':
        correct_answer = x - y
    elif random_operator == '*':
        correct_answer = x * y
    return question, str(correct_answer)
