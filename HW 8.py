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

new_string = "".join(choice(ascii_lowercase) for _ in range(randint(120, 150)))


def transform_text(text):
    index = 0
    text = list(text)
    while index + 10 < len(text):
        possible_symbols = [", ", "\n", " " + str(randint(1, 100)) + " "]
        space_point = randint(2, 10)
        index += space_point
        text[index] = choice(possible_symbols)
    text.append(".")
    text = "".join(text)
    text = text.capitalize()
    return text


print(transform_text(new_string))
