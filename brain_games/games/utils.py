import prompt
import random


def get_user_name_and_greet() -> str:
    print("Welcome to the Brain Games!")
    user_name = get_user_input("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name


def get_random_int(max_int: int, min_int=0):
    return random.randint(min_int, max_int)


def print_message(message: str):
    print(message)


def print_question(question):
    print(f"Question: {question}")


def get_user_answer():
    return prompt.string('Your answer: ')


def get_user_input(message: str) -> str:
    return prompt.string(message)


def show_lose_screen(user_name: str, user_answer: str, correct_answer: str | int):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {user_name}!")


def show_success_screen(user_name: str, is_win: bool):
    print("Correct!")
    if is_win:
        print(f"Congratulations, {user_name}!")
