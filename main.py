import os
import shutil

current_path = os.getcwd()
try:
    os.mkdir("ana_katalog")
    os.chdir(current_path + "/ana_katalog")
    os.mkdir("Alt_katalog")
except FileExistsError:
    print("Bu adda katalog mövcuddur")

# os.chdir(current_path + "\\ana_katalog\\Alt_katalog")
# for file in os.listdir():
#     if file.endswith(".txt"):
#         shutil.move(file, current_path + "\\ana_katalog\\{}".format(file.split("\\")[-1]))

# os.chdir(current_path)
# for file in os.listdir():
#     if not os.path.isdir(file) and not file.endswith(".py"):
#         shutil.move(file, current_path + "\\ana_katalog\\Alt_katalog\\{}".format(file.split("\\")[-1]))
