def test(num):
     if num==1:
        return 1
     else:
        return num * test(num-1)
print(test(5))