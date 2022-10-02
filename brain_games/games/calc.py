import random


game_task = 'What is the result of the expression?'


def generate_round():
    operator = ['+', '-', '*']
    x = random.randint(35, 70)
    y = random.randint(1, 35)
    op = random.choice(operator)
    goal = f"{x} {op} {y}"
    if op == '+':
        result = str(x + y)
    elif op == '-':
        result = str(x - y)
    elif op == '*':
        result = str(x * y)
    return str(goal), str(result)
