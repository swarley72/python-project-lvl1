import prompt
import random


def start_even_game():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    count_wins = 0

    while count_wins < 3:
        number_to_guess = get_random_number()
        is_number_even = check_is_even(number_to_guess)
        print(f"Question: {number_to_guess}")
        answer = prompt.string('Your answer: ')

        if answer == "yes" and is_number_even \
           or answer == "no" and not is_number_even:
            count_wins += 1
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{'yes' if answer == 'no' else 'no'}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def check_is_even(number):
    return number % 2 == 0


def get_random_number():
    return random.randint(1, 100)
