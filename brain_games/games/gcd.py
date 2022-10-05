import random
from math import gcd

GAME_TASK = 'Find the greatest common divisor of given numbers.'


def generate_round():
    num1 = random.randint(1, 26)
    num2 = random.randint(26, 48)
    goal = f'{num1} {num2}'
    result = gcd(num1, num2)
    return str(goal), str(result)
