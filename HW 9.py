from random import randint, choice, choices, uniform
from string import ascii_lowercase
import json

# 1

with open("/Users/tetianatopolian/PycharmProjects/Tanya_Hillel_HW/names.txt", "r") as names:
    name_list = []
    for line in names.readlines():
        name_list.append(line.split("\t"))
for word in name_list:
    print(word[1])

####################
# 2

def create_json_dict():
    number_of_keys = randint(5, 20)
    unique_dict = {}
    index = 0
    while index < number_of_keys:
        random_key = "".join(choice(ascii_lowercase) for _ in range(5))
        int_value = randint(-100, 100)
        float_value = uniform(0, 1)
        bool_list = [True, False]
        bool_value = choice(bool_list)
        value_list = [int_value, float_value, bool_value]
        probability = (1/3, 1/3, 1/3)  # если не ошибаюсь, то пайтон по умолчанию выбирает с одинаковой вероятностью?
        inside_value = choices(value_list, probability)
        unique_dict[random_key] = inside_value
        unique_dict.update({random_key: inside_value[0]}) # иначе value печатается в виде списка
        index += 1
    return unique_dict


print(create_json_dict())

#######################
# 3


def write_in_json(file_path):
    with open(file_path, "w") as json_file:
        json_data = create_json_dict()
        json.dump(json_data, json_file)


print(write_in_json("random_key_json.json"))