def test1(x,y,*args):
    print(x,y)
    print(args)

test1(1,2,3,4,5,6,7)


def test2(x,*args,**kwargs):
    # print(x)
    # print(args)
    # print(kwargs)
    sum = x
    for i in args:
        sum+=i
    for j in kwargs.values():
        sum+=j
    return sum

print(test2(1,2,3,4,num1=5,num2=6,num3=7))