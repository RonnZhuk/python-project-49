import prompt


def game_frame(task):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(task.DESCRIPTION)
    win = 0
    amount_round = 3
    while win < amount_round:
        question, correct_answer = task.game_task()
        print(f'Question: {question}')
        client_answer = prompt.string('Your answer: ')
        if client_answer == correct_answer:
            print('Correct!')
            win = win + 1
        else:
            client_answer != correct_answer
            print(f"'{client_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            win = 0
    if win == 3:
        print(f'Congratulations, {name}!')
