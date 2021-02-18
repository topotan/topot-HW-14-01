from random import randint, choice
from string import ascii_lowercase, ascii_letters

# 1

names = ["vasya", "kolobok", "pavlo", "alexandr", "karina", "katerina", "tolya"]
domains = ["com", "ua", "net", "ru", "uk"]


def email_function(list1, list2):
    random_lowercase = ascii_lowercase
    random_string = "".join(choice(random_lowercase) for _ in range(randint(5, 7)))
    random_int = str(randint(100, 999))
    random_name = choice(list1)
    random_domain = choice(list2)
    return random_name + "." + random_int + "@" + random_string + "." + random_domain


print(email_function(names, domains))


###############################
# 2

def len_random(min_limit, max_limit):
    result = "".join(choice(ascii_letters) for _ in range(randint(min_limit, max_limit)))
    return result


print(len_random(5, 10))

##########################

# 3


def transform_text(text):
    index = 0
    text = list(text)
    while index + 10 < len(text):
        possible_symbols = [", ", " ", "\n", " " + str(randint(1, 50)) + " "]
        space_point = randint(2, 10)
        index += space_point
        text[index] = choice(possible_symbols)
    text.append(".")
    text = "".join(text)
    text = text.title()  # если только первая буква большая, то capitalize, если хотим чтобы некоторые буквы были маленькими - используем функцию ниже
    return text


# print(transform_text(len_random(100,140)))

def add_lower_case(text):  # опционально, если я хочу чтобы случайным образом буквы в начале слова были маленькими / большими
    i = 0
    text = list(text)
    while i + 3 < len(text):
        upper_point = randint(1, 3)
        i += upper_point
        text[i] = text[i].lower()
    return "".join(text)


print(add_lower_case(transform_text(len_random(150, 200))))
