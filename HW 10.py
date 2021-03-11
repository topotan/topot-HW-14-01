import json
import csv

# 1


def read_txt(txt_file_path):
    with open(txt_file_path, "r") as txt_file:
        txt_content = txt_file.read().strip()
    return txt_content


def read_json(json_file_path):
    with open(json_file_path, "r") as json_file:
        json_content = json.load(json_file)
    return json_content


def read_csv(csv_file_path):
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_content = []
        for row in csv_reader:
            csv_content.append(row)
    return csv_content


def read_file(file_path):
    if file_path.endswith(".txt"):
        return read_txt(file_path)
    elif file_path.endswith(".json"):
        return read_json(file_path)
    elif file_path.endswith(".csv"):
        return read_csv(file_path)
    else:
        return print("Unsupported format!")


print(read_file("csv_authors_hw12.csv"))

# 2


with open("Sacramentorealestatetransactions.csv", "r") as new_csv:
    information = []
    reader_dict = csv.DictReader(new_csv)
    for row in reader_dict:
        information.append(dict(row))
print(information)

jsondata = {"street": "3526 HIGH ST",
            "city": "SACRAMENTO",
            "zip": "95838",
            "state": "CA",
            "beds": "2",
            "baths": "1",
            "sq__ft": "836",
            "type": "Residential",
            "sale_date": "Wed May 21 00:00:00 EDT 2008",
            "price": "59222", "latitude": "38.631913",
            "longitude": "-121.434879"}


txtdata = ["About one-third of members of the U.S. military have declined vaccine shots.", "\nWhen shots first became available to Ohio nursing-home workers, about 60 percent said no.", "\nSome N.B.A. stars are wary of appearing in public-services ads encouraging vaccination."]


def write_in_txt(txt_file_path, txt_data):
    with open(txt_file_path, "w") as txt_doc:
        txt_doc.writelines(txt_data)


def write_in_json(json_file_path, json_data):
    with open(json_file_path, "w") as json_doc:
        json.dump(json_data, json_doc, indent=4)


def write_in_csv(csv_file_path, csv_data):
    with open(csv_file_path, "w") as csv_doc:
        field_name_row = csv_data[0]
        fieldnames = field_name_row.keys()
        csv_writer = csv.DictWriter(csv_doc, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(csv_data)


def write_file(file_path, data):
    if file_path.endswith(".txt"):
        return write_in_txt(file_path, data)
    elif file_path.endswith(".json"):
        return write_in_json(file_path, data)
    elif file_path.endswith(".csv"):
        return write_in_csv(file_path, data)
    else:
        return print("Unsupported format!")


write_file("write_in.json", jsondata)
