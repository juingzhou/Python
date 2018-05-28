import os


def find_file(parent_dir, file_name):
    file_abspath = os.path.join(parent_dir, file_name)
    if os.path.isdir(file_abspath):
        for f in os.listdir(file_abspath):
            find_file(file_abspath, f)
    else:
        if file_abspath.endswith(".py"):
            print(file_abspath)


find_file("F:\\", "Python")
# file_list_name = "F:\Python\Machine Learning\人工智能PDF中文教材教程资源包2.73G基本包含全部学习资料\人工智能PDF中文教材资源包2.73G基本包含全部学习资料"
# for i,j,k in os.walk(file_list_name):
#     for x in k:
#         print(os.path.join(i,x))
