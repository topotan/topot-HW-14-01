import json
import csv

# 1


def read_file(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r") as txt_file:
            txt_content = str(txt_file.readlines())
        return txt_content
    if file_path.endswith(".json"):
        with open(file_path, "r") as json_file:
            json_content = json.load(json_file)
        return json_content
    if file_path.endswith(".csv"):
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_content = []
            for row in csv_reader:
                csv_content.append(row)
        return csv_content
    else:
        return "Unsupported file format!"


print(read_file("Name_age_country.csv"))

# 2


def write_file(file_path, data):
    pass