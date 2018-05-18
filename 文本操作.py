import os
# import random
# import string
fp = open("F:\\test.txt",'a+')
fp.writelines("姓名\t年龄\tqq号\n")
# for i in range(1000):
#     stu = {}
#     randname = ''.join(random.sample(string.ascii_letters,4))
#     # randsex = random.choice(['Male','Female'])
#     rangage = random.randint(10,80)
#     randqq = ''.join(random.sample(string.digits,10))
#     stu["name"] = randname
#     stu["age"] = rangage
#     stu["qq"] = randqq
#     print(stu)
#     fp.writelines(randname+'\t'+str(rangage)+'\t'+str(randqq)+'\n')
# fp.flush()
# fp.close()
#os.name()  --判断现在正在使用的平台
print(os.path.abspath("test.txt"))
#os.getcwd() --得到当前的目录
#os.listdir() --指定所有目录下所有的文件和目录名
source_file_name = os.listdir("F:\\Python")[-1]
source_file = os.path.abspath(source_file_name)
re_file_name = "re_"+source_file_name
re_file = os.path.abspath(source_file_name)[:os.path.abspath(source_file_name).rfind("\\")]
# print(os.path.abspath(os.listdir("F:\\Python")[-1]))
print(re_file)
os.rename(source_file,os.path.join(re_file,re_file_name))
#os.remove() --删除指定文件
#os.rmdir() --删除指定目录
#os.mkdir() --创建目录
#os.path.isfile() --判断指定对象是否为文件。是返回True，否返回False
#os.path.isdir() --判断指定对象是否为目录。是返回True，否返回False
#os.path.exists() --检查指定的对象是否存在。是返回True，否返回False
#os.path.split() --返回路径的目录和文件名
#os.getcwd() --获取当前工作目录
#os.system() --执行shell指令
#os.rename() --重新命名文件
# print(help(os.rename))


# source_file = "F:\\test.txt"
# copy_file = "copy_"+source_file[source_file.rfind("\\")+1:]
# print(copy_file)
# fp = open(source_file,'r+')
# fp1 = open("F:\\"+copy_file,'w+')
# fp1.writelines(fp.readlines())
