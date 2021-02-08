from random import randint

# 1
rndm20 = [randint(1, 100) for index in range(20)]
print(rndm20)

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

persons = [{"name": "John", "age": 15},
           {"name": "Arthur", "age": 55},
           {"name": "Carolyne", "age": 21},
           {"name": "Vasya", "age": 34},
           {"name": "Harry", "age": 98}]
print("==============")

# a
age_list = []
name_list = []
for item in persons:
    for name, age in [item.values()]:
        age_list.append(age)
        name_list.append(name)
    if min(age_list) in item.values():
        print(name, age)
# b
for name in name_list:
    maximal = max(len(name) for name in name_list)
    if len(name) == maximal:
            print(name)

# c
average = sum(age_list) / len(age_list)
print(average)

############################
# 5
my_dict_1 = {"a": 12, "j": 43, "q": 56, "u": "er", 1: 15}
my_dict_2 = {"q": 11, "j": "temp", 13: "cat", 15: 5, "b": 100, "u": "three"}

# a
common_dict_set = set(my_dict_1.keys()).intersection(set(my_dict_2.keys()))
print(list(common_dict_set))
# b
unique_key_1 = []
for key in list(my_dict_1.keys()):
    if key not in common_dict_set:
        unique_key_1.append(key)
print(unique_key_1)
# c
key_value_1 = {}
for key, value in my_dict_1.items():
    if key in unique_key_1:
        key_value_1.update({key: value})
print(key_value_1)

# d
updated_dict = {}
updated_dict.update(my_dict_1)
updated_dict.update(my_dict_2)
for key, value in my_dict_1.items():
     for key1, value1 in my_dict_2.items():
            if key == key1:
                updated_dict[key] = [value, value1]
print(updated_dict)
