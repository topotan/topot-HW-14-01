import os
path = "/Users/tetianatopolian/PycharmProjects"
files = os.listdir(path)
print(files)

for file in sorted(files)[:1]: # take only one file
    file_path = f"{path}/{file}"
    print(file_path, os.path.isfile(file_path))

file_path = os.path.join(path, file)

# reading a file
with open(file_path, "r") as txtfile:
    print(txtfile)
