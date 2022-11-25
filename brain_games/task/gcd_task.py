from math import gcd
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game_task():
    first_num = randint(1, 50)
    second_num = randint(1, 50)
    correct_answer = str(gcd(first_num, second_num))
    question = f'{first_num} {second_num}'
    return question, correct_answer
