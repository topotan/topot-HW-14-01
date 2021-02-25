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
    if " " in dict_name["name"]:
        space_index = dict_name["name"].rfind(" ")
        last_name = dict_name["name"][space_index+1:]
    else:
        last_name = dict_name["name"]

    return last_name


sorted_names = sorted(hw_dict, key=sort_name)
print(sorted_names)

# 3


def sort_years(dict_name):
    if dict_name["years"].endswith("BC."):
        dates = r"\d+"
        death_year = int(re.findall(dates, dict_name["years"])[-1]) * -1
    else:
        dates = r"\d+"
        death_year = int(re.findall(dates, dict_name["years"])[-1])
    return death_year


sorted_years = sorted(hw_dict, key=sort_years)
print(sorted_years)


# 4


def sort_len(dict_name):
    text_len = len(dict_name["text"])
    return text_len


sorted_len = sorted(hw_dict, key=sort_len)
print(sorted_len)
