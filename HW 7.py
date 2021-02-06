from random import randint

# 1
rndm20 = [randint(1, 100) for index in range(20)]
print(rndm20)

# 2
triangle = {"A": (randint(-10, 10), randint(-10, 10)),
            "B": (randint(-10, 10), randint(-10, 10)),
            "C": (randint(-10, 10), randint(-10, 10))}
print(triangle)

# 3
def my_print(my_string):
    return "***" + my_string + "***"
print(my_print("I am the string"))

# 4

persons = [{"name": "John", "age": 15}, {"name": "Arthur", "age": 55}, {"name": "Carolyne", "age": 21}, {"name": "Vasya", "age": 34}, {"name": "Harry", "age": 98}]

# a
age_list = []
name_list = []
for item in persons:
    for name, age in {item.values()}:
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
average = [sum(age_list) / len(age_list)]
print(average)