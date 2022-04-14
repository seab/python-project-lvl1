import prompt
import random
from brain_games import cli


def is_even(digit: int):
    if digit % 2 == 0:
        return "yes"
    else:
        return "no"


def guess_even():
    accumulator = 0
    game_on = True
    while game_on:
        number = random.randint(1, 20)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == is_even(number):
            print("Correct!")
            accumulator += 1

        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{is_even(number)}'"
                  f"\nLet's try again {name}")
            game_on = False

        if accumulator == 3:
            game_on = False
            print(f"Congratulations, {name}")


print('Welcome to the Brain Games!')
name = cli.welcome_user()
print('Answer "yes" if the number is even, otherwise answer "no".')
