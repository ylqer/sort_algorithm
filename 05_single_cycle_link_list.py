class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标，用来遍历节点
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur is not self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，cur指向尾节点，但尾节点还未打印
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素, 头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        # 退出循环，cur指向尾节点
        node.next = self.__head
        self.__head = node
        cur.next = self.__head

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    # 头节点
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                    # self.__head = cur.next
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):
        """查找结点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
