import random
import string


letters = string.ascii_letters
special_char = string.punctuation
numbers = string.digits


def pwd_generator(min_length, special_characters=True):
    characters = letters + numbers

    if special_characters:
        characters += special_char
    pwd = ""
    meets_criteria = False
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if any(x in numbers for x in pwd):
            meets_criteria = True
    return pwd


print(pwd_generator(6))
