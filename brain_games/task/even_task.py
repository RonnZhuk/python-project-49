from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_task():
    number = randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer
