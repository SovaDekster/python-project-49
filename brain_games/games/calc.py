import random


RULE = 'What is the result of the expression?'


def generate_round():
    operators = ['+', '-', '*']
    x = random.randint(35, 70)
    y = random.randint(1, 35)
    op = random.choice(operators)
    question = f"{x} {op} {y}"
    if op == '+':
        correct_answer = x + y
    elif op == '-':
        correct_answer = x - y
    elif op == '*':
        correct_answer = x * y
    return question, str(correct_answer)
