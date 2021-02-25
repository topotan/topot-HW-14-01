from random import randint, choice, choices, uniform
from string import ascii_lowercase
import json

# 1

with open("names.txt", "r") as names:
    info_list = []
    for line in names.readlines():
        info_list.append(line.split("\t")[1])
print(info_list)


####################
# 2


def create_json_dict(number_of_keys):
    unique_dict = {}
    index = 0
    while index < number_of_keys:
        random_key = "".join(choice(ascii_lowercase) for _ in range(5))
        value_list = [randint(-100, 100), uniform(0, 1), choice([True, False])]
        probability = (1/3, 1/3, 1/3)  # если не ошибаюсь, то пайтон по умолчанию выбирает с одинаковой вероятностью?
        inside_value = choices(value_list, probability)
        unique_dict[random_key] = inside_value
        unique_dict.update({random_key: inside_value[0]})  # иначе value печатается в виде списка
        index += 1
    return unique_dict


key_number = randint(5, 20)
print(create_json_dict(key_number))

#######################
# 3


def write_in_json(file_path):
    with open(file_path, "w") as json_file:
        json_data = create_json_dict(randint(5, 20))
        json.dump(json_data, json_file)


write_in_json("/Users/tetianatopolian/Desktop/lesson3 2")
