import random
import prompt
from brain_games import cli


def generate_progression():
    progression_length = random.randrange(5, 10)
    progression_start = random.randrange(1, 20)
    progression_step = random.randrange(2, 8)
    progression = [progression_start + progression_step * i for i in range(progression_length)]
    return progression


def genereate_question_and_answer():
    progression = generate_progression()
    hidden_number = random.choice(progression)
    hidden_number_index = progression.index(hidden_number)
    progression[hidden_number_index] = '..'
    answer = hidden_number
    question = ' '.join(str(item) for item in progression)
    return question, answer


def main():
    accumulator = 0
    game_on = True
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('What number is missing in the progression?')
    while game_on:
        result = genereate_question_and_answer()
        right_answer = result[1]
        print(f'Question: {result[0]}')
        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == right_answer:
            print('Correct')
            accumulator += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'")
            game_on = False
        if accumulator == 3:
            game_on = False
            print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()
