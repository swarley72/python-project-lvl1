from brain_games.games.utils import (
    get_random_int,
    get_user_answer,
    get_user_name_and_greet,
    print_question,
    show_lose_screen,
    show_success_screen,
)


def start_prime_game():
    user_name = get_user_name_and_greet()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    count_wins = 0

    while count_wins < 3:
        question, correct_answer = get_question_and_correct_answer()
        print_question(question)
        user_answer = get_user_answer()

        if user_answer == correct_answer:
            count_wins += 1
            show_success_screen(user_name, count_wins >= 3)
        else:
            show_lose_screen(user_name, user_answer, correct_answer)
            return


def check_is_prime(number) -> bool:
    if number <= 1:
        return False

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False

    return True


def get_question_and_correct_answer() -> tuple[str, str]:
    number_to_guess = get_random_int(100)
    correct_answer = "yes" if check_is_prime(number_to_guess) else "no"

    return str(number_to_guess), correct_answer
