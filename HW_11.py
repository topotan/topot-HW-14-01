import json
import re

# 1


def read_json_file(file_path):
    with open(file_path, "r") as json_doc:
        content = json.load(json_doc)
    return content


print(read_json_file("data.json"))

hw_dict = read_json_file("data.json")

# 2


def sort_name(dict_name):
    name = dict_name.get("name")
    last_name = name.split()[-1]
    return last_name


sorted_names = sorted(hw_dict, key=sort_name)
print(sorted_names)

# 3


def sort_years(dict_name):
    year = dict_name.get("years")
    if year.endswith("BC."):
        dates = r"\d+"
        death_year = int(re.findall(dates, year)[-1]) * -1
    else:
        dates = r"\d+"
        death_year = int(re.findall(dates, year)[-1])
    return death_year


sorted_years = sorted(hw_dict, key=sort_years)
print(sorted_years)


# 4


def sort_len(dict_name):
    return len(dict_name["text"])


sorted_len = sorted(hw_dict, key=sort_len)
print(sorted_len)
