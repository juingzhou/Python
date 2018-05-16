# import random
# import string
# fp = open("F:\\test.txt",'a+')
# fp.writelines("姓名\t年龄\tqq号\n")
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
source_file = "F:\\test.txt"
# print(source_file[0:source_file.find("\\")+1])
copy_file = "copy_"+source_file[source_file.rfind("\\")+1:]
print(copy_file)
fp = open(source_file,'r+')
fp1 = open("F:\\"+copy_file,'w+')
fp1.writelines(fp.readlines())
