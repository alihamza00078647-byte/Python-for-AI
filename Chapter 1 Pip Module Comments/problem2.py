import os
# pwd = os.getcwd()
# print("Current Working Directory", pwd)
directory_path = '/'
content = os.listdir(directory_path)

for i in content:
    print(i)