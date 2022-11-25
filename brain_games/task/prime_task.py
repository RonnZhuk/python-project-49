from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(random_num):
    divider = 2
    while random_num % divider != 0:
        divider = divider + 1
    return divider == random_num


def game_task():
    random_num = randint(2, 101)
    question = str(random_num)
    correct_answer = prime_check(random_num)
    if correct_answer:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
