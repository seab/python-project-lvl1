import random
import prompt
from brain_games import cli

operations = ["+", "-", "*"]


def generate_expression():
    return f'{random.randint(1, 20)} {random.choice(operations)} {random.randint(1, 20)}'


def result(exrp):
    list_of_expr = exrp.split()
    digit_1 = int(list_of_expr[0])
    digit_2 = int(list_of_expr[2])
    operation = list_of_expr[1]
    if operation == '+':
        return digit_1 + digit_2
    elif operation == '-':
        return digit_1 - digit_2
    elif operation == '*':
        return digit_1 * digit_2


def main():
    accumulator = 0
    game_on = True
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('What is the result of the expression?')
    while game_on:
        expression = generate_expression()
        right_answer = result(expression)
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
