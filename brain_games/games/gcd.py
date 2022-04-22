import random
import prompt
import math
from brain_games import cli


def generate_expression():
    return f"{random.randint(1, 100)} {random.randint(1, 100)}"


def get_result(expr):
    list_of_expr = expr.split()
    digit_1 = int(list_of_expr[0])
    digit_2 = int(list_of_expr[1])
    return math.gcd(digit_1, digit_2)


def main():
    accumulator = 0
    game_on = True
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.?')
    while game_on:
        expression = generate_expression()
        right_answer = get_result(expression)
        print(f'Question: {expression}')
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
