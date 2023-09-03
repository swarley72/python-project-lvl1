from brain_games.games.utils import (
    get_random_int,
    get_user_answer,
    get_user_name_and_greet,
    print_question,
    show_lose_screen,
    show_success_screen,
)


def start_gcd_game():
    user_name = get_user_name_and_greet()
    print("Find the greatest common divisor of given numbers.")
    count_wins = 0

    while count_wins < 3:
        question, correct_answer = get_question_and_gcd()
        print_question(question)
        user_answer = get_user_answer()

        if user_answer == correct_answer:
            count_wins += 1
            show_success_screen(user_name, count_wins >= 3)
        else:
            show_lose_screen(user_name, user_answer, correct_answer)
            break


def get_question_and_gcd() -> tuple[str, int]:
    first_number = get_random_int(10, 1)
    second_number = get_random_int(10, 1)
    return f"{first_number} {second_number}", str(get_gcd(first_number, second_number))


def get_gcd(first: int, second: int) -> int:
    result = min(first, second)

    while result:
        if first % result == 0 and second % result == 0:
            break
        result -= 1

    return result
