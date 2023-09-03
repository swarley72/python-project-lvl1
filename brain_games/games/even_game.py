from brain_games.games.utils import (
    get_random_int,
    get_user_answer,
    get_user_name_and_greet,
    print_question,
    show_lose_screen,
    show_success_screen,
)


def start_even_game():
    name = get_user_name_and_greet()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    count_wins = 0

    while count_wins < 3:
        number_to_guess = get_random_int(100)
        is_number_even = check_is_even(number_to_guess)
        print_question(number_to_guess)
        answer = get_user_answer()

        if answer == "yes" and is_number_even \
           or answer == "no" and not is_number_even:
            count_wins += 1
            show_success_screen(name, count_wins >= 3)
        else:
            show_lose_screen(name, answer, 'yes' if answer == 'no' else 'no')
            return


def check_is_even(number):
    return number % 2 == 0
