from random import randint, choice, choices, uniform
from string import ascii_lowercase
import json

# 1

# with open("names.txt", "r") as names:
#     info_list = []
#     name_list = []
#     for line in names.readlines():
#         info_list.append(line.split("\t"))
# for word in info_list:
#     name_list.append(word[1])
# print(name_list)

####################
# 2


def create_json_dict(number_of_keys):
    unique_dict = {}
    full_dict = {}
    index = 0

    while index in range(number_of_keys):
        random_key = "".join(choice(ascii_lowercase) for _ in range(5))
        value = choice(["int", "float", "bool"])
        if value == "int":
            inside = randint(-100, 100)
            unique_dict = {random_key: inside}
        elif value == "float":
            inside = uniform(0, 1)
            unique_dict = {random_key: inside}
        else:
            inside = choice([True, False])
            unique_dict = {random_key: inside}
        index += 1
        full_dict.update(unique_dict)

    return full_dict


key_number = randint(5,20)
print(create_json_dict(key_number))

#######################
# 3


# def write_in_json(file_path):
#     with open(file_path, "w") as json_file:
#         json_data = create_json_dict(randint(5, 20))
#         json.dump(json_data, json_file)
#
#
# write_in_json("new_json.json")
