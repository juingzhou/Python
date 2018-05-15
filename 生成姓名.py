import random
import string
for i in range(1000):
    randname = ''.join(random.sample(string.ascii_letters,4))
    randsex = random.choice(['Male','Female'])
    rangage = random.randint(10,80)
    randqq = ''.join(random.sample(string.digits,10))
    print("%s    %s     %s     %s"%(randname,randsex,rangage,randqq))