class Dequeue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """从头部往队列中添加一个元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """从尾部往队列中添加一个元素"""
        self.__list.append(item)

    def pop_front(self):
        """从头部弹出一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从尾部弹出一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回一个队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    dequeue = Dequeue()
    dequeue.add_rear(0)
    dequeue.add_rear(1)
    dequeue.add_rear(2)
    dequeue.add_rear(3)
    dequeue.add_rear(4)
    print(dequeue.pop_rear())
    print(dequeue.pop_rear())
    print(dequeue.pop_rear())
    print(dequeue.pop_rear())
    print(dequeue.pop_rear())
