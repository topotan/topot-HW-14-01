import requests
import csv
import json
import re


# 1

def sort_authors_in_csv(amount, file):
    try:
        url = "http://api.forismatic.com/api/1.0/"
        author_dicts = []
        for number in range(amount):
            params = {"method": "getQuote",
                      "format": "json",
                      "key": number,
                      "lang": "en"}
            r = requests.get(url, params=params)
            result = r.json()

            if result["quoteAuthor"]:
                author_dicts.append(result)

        def sort_by_name(dictionary):
            name = dictionary["quoteAuthor"]
            return name

        author_dicts = sorted(author_dicts, key=sort_by_name)

        with open(file, "w") as csv_file:
            field_name_row = ["Author", "Quote", "URL"]
            writer = csv.DictWriter(csv_file, field_name_row)
            writer.writeheader()
            for unit in author_dicts:
                writer.writerow({"Author": unit["quoteAuthor"], "Quote": unit["quoteText"], "URL": unit["quoteLink"]})

    except json.decoder.JSONDecodeError:
        print("Web server is not loading correctly. Try again!")


sort_authors_in_csv(5, "csv_authors_hw12.csv")


# 2.1

def read_txt(doc="authors.txt"):
    with open(doc, "r") as txt_file:
        txt_content = []
        for line in txt_file.read().split("\n"):
            if "'s" in line:  # т.к. только в строчках где указаны полные даты и рождение/смерть есть 's, этого условия было достаточно. Альтернативно можно придумать другие методы для других вариаций
                txt_content.append(line)
        return txt_content


print(read_txt())

# 2.2


def create_dict(list_of_authors):

    months = {"January": "1",
              "February": "2",
              "March": "3",
              "April": "4",
              "May": "5",
              "June": "6",
              "July": "7",
              "August": "8",
              "September": "9",
              "October": "10",
              "November": "11",
              "December": "12"}

    full_date_name = []

    for unit in list_of_authors:
        dash_point = unit.find("-")
        apo_point = unit.find("'")

        date = unit[:dash_point]
        date_num = r"\d+"
        date_numbers = re.findall(date_num, date)
        date_month = str(r"[a-zA-Z]{3,10}")
        month = re.findall(date_month, date)[0]

        for m_name, count_number in months.items():
            if month == m_name:
                month = count_number

        date_numbers.insert(1, month)
        date_numbers = f"{date_numbers[0]}/{date_numbers[1]}/{date_numbers[2]}"

        name = unit[dash_point + 2:apo_point]
        name_and_date = {"name": name, "date": date_numbers}
        full_date_name.append(name_and_date)

    return full_date_name


print(create_dict(read_txt()))


# 2.3

author_date = create_dict(read_txt())


def save_in_json(filepath, data):
    with open(filepath, "w") as json_file:
        json.dump(data, json_file, indent=4)


save_in_json("json_authors_hw12.json", author_date)
