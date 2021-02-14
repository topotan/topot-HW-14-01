import os


path = "/Users/tetianatopolian/PycharmProjects/Tanya_Hillel_HW"
files = os.listdir(path)
print(files)

for file in sorted(files):
    file_path = os.path.join(path, file)
    print(file_path, os.path.isfile(file_path))