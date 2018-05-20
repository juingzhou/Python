import twisted
import os

s = "helloworld"
result = {}
for i in s:
    result[i] = s.count(i)
print(result)

result1 = {}
for j in s:
    if j in result1:
        result1[j] += 1
    else:
        result1[j] = 1
print(result1)
if os.name == 'nt':
    print("Windows")
else:
    print("Linux")
