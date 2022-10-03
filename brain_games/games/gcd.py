import random
from math import gcd

game_task = 'Find the greatest common divisor of given numbers.'


def generate_round():
    x = random.randint(1, 26)
    y = random.randint(26, 48)
    goal = f'{x} {y}'
    result = gcd(x, y)
    return str(goal), str(result)
