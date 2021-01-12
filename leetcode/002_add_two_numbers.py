class Node(object):
    """定义节点"""
    def __init__(self, val=0):
        self.elem = val
        self.next = None


class SingleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.head = node

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def append(self, item):
        node = Node(item)
        cur = self.head
        if cur is None:
            self.head = node
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')


def add_two_numbers(l1: Node, l2: Node):
    re = Node(0)
    r = re
    carry = 0
    while l1 or l2:
        x = l1.elem if l1 else 0
        y = l2.elem if l2 else 0
        s = carry + x + y
        carry = s // 10
        r.next = Node(s % 10)
        r = r.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    if carry > 0:
        r.next = Node(1)
    return re.next
    # while re.next is not None:
    #     print(re.next.elem, end='')
    #     re = re.next


if __name__ == '__main__':
    sll = SingleLinkList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.travel()
    a_all = SingleLinkList()
    a_all.append(1)
    a_all.append(2)
    a_all.append(8)
    a_all.travel()
    # sol = Solution()
    res = add_two_numbers(sll.head, a_all.head)
    while res is not None:
        print(res.elem, end='')
        res = res.next
