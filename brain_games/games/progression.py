import random


RULE = 'What number is missing in the progression?'


def generate_round():
    first_number = random.randint(0, 34)
    length = random.randint(5, 10)
    step = random.randint(1, 8)

    def generate_progression():
        progression = [str(first_number), ]
        current_step = 1
        current_number = first_number
        while current_step <= length:
            current_number += step
            progression.append(str(current_number))
            current_step += 1
        return progression
    progression = generate_progression()
    random_index = random.randint(0, (len(progression) - 1))
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    question = ' '.join([str(elem) for elem in progression])
    return correct_answer, question
