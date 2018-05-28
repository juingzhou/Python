# coding:utf-8
import string
def alp(s):
    result={}
    for i in set(s):
        result[i] = s.count(i)
    return result
    # for i in s:
    #     result[i] = s.count(i)
    # return max(string.ascii_lowercase,key=s.count)
s1 = "come on baby!".lower()
print(alp(s1))
# print(sorted(alp(s1).keys()))
print(sorted(alp(s1).items(), key=lambda item: item[1], reverse=True)[0:3])
# print(sorted(alp(s1).keys()))
s1 = "I Love You"
print(sorted(alp(s1).items(), key=lambda item: item[1], reverse=True)[0:3])



