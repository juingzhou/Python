import twisted
def test1(x,y):
    x = x.replace("c","F")
    print(x)
    y.append(10)
    print(id(x))

a = "abcdef"
b=[1,2,3]
print(id(a))
test1(a,b)
# print(id(a.replace("a","A")))


# def test2(x,y):
#     pass