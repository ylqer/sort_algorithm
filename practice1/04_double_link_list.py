class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("")

    def add(self, item):
        """从头部添加"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        node.next = self.__head
        self.__head.prev = node
        self.__head = node

    def append(self, item):
        """从尾部添加"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def insert(self, pos, item):
        """制定位置添加"""
        if pos <= 0:
            self.add(item)
            return
        if pos > self.length() - 1:
            self.append(item)
            return
        node = Node(item)
        cur = self.__head
        count = 0
        while count < pos - 1:
            count += 1
            cur = cur.next
        node.next = cur.next
        cur.next = node
        node.prev = cur
        node.next.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            if cur.elem == item:
                if cur == self.__head:
                    if self.length() > 1:
                        self.__head = cur.next
                        cur.next.prev = self.__head
                        return
                    else:
                        self.__head = None
                        return
                elif count == self.length():
                    cur.prev = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    return
            cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    dll.append(0)
    print(dll.is_empty())
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.travel()
    print(dll.length())
    dll.add(100)
    dll.travel()
    print(dll.length())
    dll.insert(2, 200)
    dll.travel()
    print(dll.length())
    dll.remove(3)
    dll.travel()
    print(dll.length())
    print(dll.search(1))
    print(dll.search(10))
