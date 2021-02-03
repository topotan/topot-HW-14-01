# 1
my_animal_list = ["dog", "cat", "horse", "wolf", "bug", "bird", "fish"]
new_animal_list = []
for index, animal in enumerate(my_animal_list):
    if not index % 2:
        new_animal_list.append(animal)
    else:
        new_animal_list.append(animal[::-1])
print(new_animal_list)

# 2
my_country_list = ["Austria", "Romania", "Ukraine", "Armenia", "Georgia"]
new_country_list = []
for country in my_country_list:
    if country[0] == "A":
        new_country_list.append(country)
print(new_country_list)

# 3
my_food_list = ["cake", "cola", "cucumber", "honey", "jam"]
new_food_list = []
for food in my_food_list:
    if "a" in food:
       new_food_list.append(food)
print(new_food_list)

# 4
my_list = [12, "error", "65", "sunny", 76, "boom"]
my_str = []
for item in my_list:
    if item is str(item):
        my_str.append(item)
print(my_str)

# 5
my_str = "Hello! It is a great day outside, isn't it?"
new_str_list = []
for symbol in my_str:
    if my_str.count(symbol) == 1:
        new_str_list.append(symbol)
print(new_str_list)

# 6
my_str_1 = "Gary didn't understand why Doug went upstairs."
my_str_2 = "He fumbled in the darkness looking for the light switch."
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
print(my_set_1.intersection(my_set_2))

#7
my_str_1 = "Gary understands."
my_str_2 = "He was looking for a switch."
new_str_list_1 = []
new_str_list_2 = []
for symbol_1 in my_str_1:
    if my_str_1.count(symbol_1) == 1:
        new_str_list_1.append(symbol_1)
for symbol_2 in my_str_2:
    if my_str_2.count(symbol_2) == 1:
        new_str_list_2.append(symbol_2)
new_str_list_1 = set(new_str_list_1)
new_str_list_2 = set(new_str_list_2)
print(new_str_list_1.intersection(new_str_list_2))

# 8
человек = {"Фамилия": "Пупкин",
           "Имя": "Вася",
           "Возраст": 34,
           "Проживание": {"Страна": "Украина",
                          "Город": "Киев",
                          "Улица": "Заречная, 11"},
           "Работа": {"Наличие": "трудоустроен",
                      "Должность": "главврач"}}
print(человек["Проживание"]["Город"])

# 9
cake = {"Составляющие":
            {"Коржи":
                 {"Мука": "300г",
                  "Молоко": "200мл",
                  "Масло": "50г",
                  "Яйцо": "2 шт"},
             "Крем":
                  {"Сахар": "100г",
                   "Масло": "75г",
                   "Ваниль": "1 пакетик",
                   "Сметана": "3 столовые ложки"},
              "Глазурь":
                   {"Какао": "150г",
                    "Сахар": "50г",
                    "Масло": "60г"}}}

print(cake["Составляющие"]["Глазурь"]["Какао"])
