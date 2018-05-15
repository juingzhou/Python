def test(num):
    list_num = [1,1]
    for i in range(num-2):
        list_num.append(list_num[i]+list_num[i+1])
    return list_num
while True:
    num = int(input("请输入数字："))
    if num<=2:
        print("请输入大于等于3的数")
    else:
        for i in test(num):
            print("%s,"%i,end='')
        print()

