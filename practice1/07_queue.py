class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列中取出一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    print(queue.size())
    queue.enqueue(0)
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.size())
