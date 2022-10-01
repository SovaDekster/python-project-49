import random
import prompt


def calculator():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    operator = ['+', '-', '*']
    count = 0
    while count < 3:
        x = random.randint(35, 70)
        y = random.randint(1, 35)
        op = random.choice(operator)
        answer = f'{x} {op} {y}'
        print('Question:', answer)
        u_answer = prompt.string('Your answer: ')

        if op == '+':
            answer = str(x + y)
        if op == '-':
            answer = str(x - y)
        if op == '*':
            answer = str(x * y)
        if u_answer == answer:
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{u_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
