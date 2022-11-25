import operator
from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = ((operator.add, '+'), (operator.sub, '-'), (operator.mul, '*'))


def game_task():
    first_num = randint(1, 10)
    second_num = randint(1, 10)
    operator, sign = choice(OPERATIONS)
    correct_answer = str(operator(first_num, second_num))
    question = f'{first_num} {sign} {second_num}'
    return question, correct_answer
