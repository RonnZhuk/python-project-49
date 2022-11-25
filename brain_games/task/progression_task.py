from random import randint


DESCRIPTION = 'What number is missing in the progression?.'


def game_task():
    prog_len = 10
    step = randint(1, 20)
    start_num = randint(1, 100)
    finish_num = start_num + (step * prog_len)
    prog = list(range(start_num, finish_num, step))
    hidden_num = randint(0, 9)
    correct_answer = str(prog[hidden_num])
    prog[hidden_num] = '..'
    question = ' '.join(map(str, prog))
    return question, correct_answer
