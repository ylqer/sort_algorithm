class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            count = 0
            return count
        cur = self.__head
        count = 0
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        count += 1
        return count

    def travel(self):
        """遍历整个列表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = self.__head
        return

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return
        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = Node(item)
        if pos <= 0:
            self.add(item)
            return
        cur = self.__head
        count = 0
        while count < pos - 1:
            count += 1
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def remove(self, item):
        """删除节点"""
        if self.__head.elem == item:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            self.__head = self.__head.next
            if self.is_empty():
                return
            cur.next = self.__head
            return
        cur = self.__head
        prev = None
        while cur.next is not self.__head:
            if cur.elem == item:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        if cur.elem == item:
            prev.next = cur.next
            return

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur.next is not self.__head:
            if cur.elem == item:
                return True
            cur = cur.next
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    ll.append(0)
    print(ll.is_empty())
    ll.add(100)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.travel()
    ll.insert(0, 12)
    ll.travel()
    ll.insert(6, 23)
    ll.travel()
    print(ll.search(23))
    print(ll.search(22))
    ll.remove(100)
    ll.travel()
    print(ll.length())
    ll.remove(12)
    ll.travel()
    ll.remove(23)
    ll.travel()
    print(ll.length())
