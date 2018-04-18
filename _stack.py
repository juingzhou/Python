class Stack(object):
    """"栈"""
    def __init__(self):
        self.__list = []
    def push(self,item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)
        # pass
    def pop(self):
        """"弹出栈顶元素"""
        return self.__list.pop()
        # pass
    def peek(self):
        """"返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
        # pass
    def is_empty(self):
        if self.__list==[]:
            return True
        else:
            return False
        # pass
    def size(self):
        return len(self.__list)
        # pass

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

