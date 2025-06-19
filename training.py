import os
import random
import time
import shutil

fruits = ["grape", "lemon", "watermelon", "apple", "pear"]

folder_name = input("Enter the name of your folder\n")
file_name_1 = input("Enter the name of the first file\n")
file_name_2 = input("Enter the name of the second file\n")
file_name_3 = input("Enter the name of the third file\n")

if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.mkdir(folder_name)

path1 = os.path.join(folder_name, file_name_1)
path2 = os.path.join(folder_name, file_name_2)
path3 = os.path.join(folder_name, file_name_3)

with open(path1, "w") as f1:
    f1.write(random.choice(fruits))

time.sleep(2)
with open(path2, "w") as f2:
    f2.write(random.choice(fruits))

time.sleep(2)
with open(path3, "w") as f3:
    f3.write(random.choice(fruits))

files = os.listdir(folder_name)
print(files)
