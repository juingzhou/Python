class DoubleQueue(object):
    """"双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列头部添加一个item元素"""
        self.__list.append(0,item)
        # pass
    def add_end(self,item):
        """往队列尾部添加一个item元素"""
        self.__list.append(item)
    def pop_front(self):
        """从头部删除一个元素"""
        return self.__list.pop(0)
        # pass
    def pop_end(self):
        """从尾部删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """"判断一个队列是否为空"""
        return self.__list == []
        # pass

    def size(self):
        """"返回队列的长度"""
        return len(self.__list)
        # pass

if __name__ == "__main__":
    dq = DoubleQueue()
    dq.add_end(1)
    dq.add_front(2)

