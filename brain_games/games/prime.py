import random
import prompt
from brain_games import cli


def is_prime(n):
    if n <= 1:
        return "no"
    else:
        for i in range(2, n):
            if n % i == 0:
                return "no"
    return "yes"


def genereate_question_and_answer():
    question = random.randint(1, 20)
    answer = is_prime(question)

    return question, answer


def main():
    accumulator = 0
    game_on = True
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while game_on:
        result = genereate_question_and_answer()
        right_answer = result[1]
        print(f'Question: {result[0]}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
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
