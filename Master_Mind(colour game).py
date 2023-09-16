import random

COLOR = ["R", "B", "G", "Y", "O", "W"]
TRIES = 10
CODE_LENGTH = 4


def code_generator():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLOR)
        code.append(color)
    return code


def guess_color():
    while True:
        guess = input("Guess:").rstrip().upper().split(" ")
        if len(guess) != CODE_LENGTH:
            print(f"You Have To Guess {CODE_LENGTH} Colors")
            continue
        for i in guess:
            if i not in COLOR:
                print(f"Invalid color : {i}. Try again")
                break
        else:
            break
    return guess


def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for i in real_code:
        if i not in color_count:
            color_count[i] = 0
        color_count[i] += 1
    for i, j in zip(guess, real_code):
        if i == j:
            correct_pos += 1
            color_count[i] -= 1
    for i, j in zip(guess, real_code):
        if i in real_code and color_count[i] > 0:
            incorrect_pos += 1
            color_count[i] -= 1
    return correct_pos, incorrect_pos


def game():
    code = code_generator()
    for attempts in range(1, TRIES + 1):
        guess = guess_color()
        correct_pos, incorrect_pos = check_code(guess, code)
        if correct_pos == CODE_LENGTH:
            print(f"You Guessed The Code in {attempts} Tries!!!")
            break

        print(
            f"Correct Possitions : {correct_pos}  |  Incorrect positions : {incorrect_pos}"
        )
    else:
        print("You Ran Out of Tries . The Correct Code Was", *code)


if __name__ == "__main__":
    game()
