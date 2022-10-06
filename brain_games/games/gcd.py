import random
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'


def generate_round():
    num1 = random.randint(1, 26)
    num2 = random.randint(26, 48)
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)
    return question, str(correct_answer)
