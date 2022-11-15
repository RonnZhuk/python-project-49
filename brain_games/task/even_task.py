from random import randint
import prompt


def even_number(name):
    print('Answer "yes" if the number is even, otherwise answer "no"')
    win = 0
    amount_round = 3
    while win < amount_round:
        number = randint(1, 100)
        print(f'Question: {number}')
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        client_answer = prompt.string('Your answer: ')
        if client_answer == correct_answer:
            print('Correct!')
            win = win + 1
        else:
            client_answer != correct_answer
            print(f"'{client_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            win = 0
    if win == 3:
        print(f'Congratulations, {name}!')
