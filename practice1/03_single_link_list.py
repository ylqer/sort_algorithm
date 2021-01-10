class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        return

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos >= self.length():
            self.append(item)
        if pos < 0:
            self.add(item)
        node = Node(item)
        count = 0
        cur = self.__head
        while count < pos - 1:
            cur = cur.next
            count += 1
        node.next = cur.next
        cur.next = node
        return

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        if self.__head.elem == item:
            self.__head = cur.next
            return
        while cur.next is not None:
            if cur.next == item:
                cur.next = cur.next.next
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
    ll = SingleLinkList()
    print(ll.length())
    print(ll.is_empty())
    ll.append(0)
    print(ll.is_empty())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.add(100)
    ll.travel()
    ll.insert(2, 200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    print(ll.search(4))
    print(ll.length())
