import os
path = "/Users/tetianatopolian/PycharmProjects"
files = os.listdir(path)
print(files)

for file in sorted(files)[:1]: # take only one csv_authors_hw12
    file_path = f"{path}/{file}"
    print(file_path, os.path.isfile(file_path))

file_path = os.path.join(path, file)

# reading a csv_authors_hw12
with open(file_path, "r") as txtfile:
    print(txtfile)
