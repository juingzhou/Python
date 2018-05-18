import os


def find_file(parent_dir,file_name):
    file_abspath = os.path.join(parent_dir,file_name)
    if os.path.isdir(file_abspath):
        for f in os.listdir(file_abspath):
            find_file(file_abspath,f)
    else:
        if file_abspath.endswith(".py"):
            print(file_abspath)
find_file("F:\Python","Python")



