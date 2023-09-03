from brain_games.games.utils import (
    get_random_int,
    get_user_answer,
    get_user_name_and_greet,
    print_question,
    show_lose_screen,
    show_success_screen,
)
import random


def start_calc_game():
    user_name = get_user_name_and_greet()
    count_wins = 0

    while count_wins < 3:
        question, correct_answer = get_question_and_correct_answer()
        print_question(question)
        user_answer = int(get_user_answer())
        if user_answer == correct_answer:
            count_wins += 1
            show_success_screen(user_name, count_wins >= 3)
        else:
            show_lose_screen(user_name, user_answer, correct_answer)
            return


def get_question_and_correct_answer() -> tuple[str, int]:
    first_number = get_random_int(20)
    second_number = get_random_int(20)
    operation = get_operation()

    question = f"{first_number} {operation} {second_number}"
    return question, eval(question)


def get_operation():
    return random.choice(["+", "-", "*"])
