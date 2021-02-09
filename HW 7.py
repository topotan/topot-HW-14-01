from random import randint

# 1
random_20_numbers = [randint(1, 100) for index in range(20)]
print(random_20_numbers)

###########################
# 2
triangle = {"A": (randint(-10, 10), randint(-10, 10)),
            "B": (randint(-10, 10), randint(-10, 10)),
            "C": (randint(-10, 10), randint(-10, 10))}
print(triangle)

###########################
# 3
def my_print(my_string):
    return "***" + my_string + "***"
print(my_print("I am the string"))

############################
# 4

persons = [{"name": "John", "age": 17},
           {"name": "Arthur", "age": 10},
           {"name": "Carolyne", "age": 21},
           {"name": "Vasya", "age": 9},
           {"name": "Harry", "age": 98}]

# a
age_list = []
name_list = []
for item in persons:
    for name, age in [item.values()]:
        age_list.append(age)
        name_list.append(name)
for item in persons:
    if min(set(age_list)) is item["age"]:
        print(item["name"])

# б
for name in name_list:
    maximal = max(len(name) for name in set(name_list))
    if len(name) == maximal:
            print(name)

# в
average = sum(age_list) / len(age_list)
print(average)

############################
# 5
my_dict_1 = {"a": 12, "j": 43, "q": 56, "u": "er", 1: 15}
my_dict_2 = {"q": 11, "j": "temp", 13: "cat", 15: 5, "b": 100, "u": "three"}

# a
common_dict_set = set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))
print(list(common_dict_set))

# б
unique_key_1 = []
for key in list(my_dict_1.keys()):
    if key not in common_dict_set:
        unique_key_1.append(key)
print(unique_key_1)

# в
key_value_1 = {}
for key, value in my_dict_1.items():
    if key in unique_key_1:
        key_value_1.update({key: value})
print(key_value_1)

# г
updated_dict = {**my_dict_1, **my_dict_2}
for key, value in my_dict_1.items():
     for value1 in my_dict_2.values():
            if key in common_dict_set:
                updated_dict[key] = [value, value1]
print(updated_dict)
