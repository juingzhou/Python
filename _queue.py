class Queue(object):
    def __init__(self):
        self.__list = []
    def enqueue(self,item):
        """往队列添加一个item元素"""
        self.__list.append(item)
        # pass
    def dequeue(self):
        """从头部删除一个元素"""
        return self.__list.pop(0)
        # pass
    def is_empty(self):
        """"判断一个队列是否为空"""
        return self.__list==[]
        # pass
    def size(self):
        """"返回队列的长度"""
        return len(self.__list)
        # pass

if __name__ =="__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())

    print(q.dequeue())
    print(q.dequeue())