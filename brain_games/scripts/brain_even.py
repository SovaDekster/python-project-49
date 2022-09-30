#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        question = random.randint(1, 100)
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')

        if question % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'

        if (question % 2 == 0 and your_answer == 'yes') or (question % 2 != 0 and your_answer == 'no'):
            count += 1
            print('Correct!')
        elif (question % 2 == 0 and your_answer == 'no') or (question % 2 != 0 and your_answer == 'yes'):
            print(f'\'{your_answer}\' is wrong answer ;(. Correct answer was \'{true_answer}\'.\nLet\'s try again, {name}!')
            break
        elif your_answer != 'yes' and your_answer != 'no':
            print(f'\'{your_answer}\' is wrong answer ;(. Correct answer was \'{true_answer}\'.\nLet\'s try again, {name}!')
            break
        if count == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
