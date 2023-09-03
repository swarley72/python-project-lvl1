from brain_games.games.utils import (
    get_random_int,
    get_user_answer,
    get_user_name_and_greet,
    print_question,
    show_lose_screen,
    show_success_screen,
)


def start_progression_game():
    user_name = get_user_name_and_greet()
    print("What number is missing in the progression?")
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


def get_progression_arr(start: int, end: int, step: int) -> list[int]:
    return list(map(str, range(start, end, step)))


def get_question_and_correct_answer() -> tuple[str, str]:
    progression = get_progression_arr(0, 21, 3)
    missing_index = get_random_int(len(progression) - 1)
    missing_number = progression[missing_index]
    progression[missing_index] = ".."

    return " ".join(progression), str(missing_number)
