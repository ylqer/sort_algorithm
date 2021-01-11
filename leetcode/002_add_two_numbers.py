class Node(object):
    """定义节点"""

    def __init__(self, val=0):
        self.elem = val
        self.next = None


class SingleLinkList(object):
    """单向链表"""
    def __init__(self, node):
        self.__head = node
        self.next = None


class Solution(object):
    """两数相加"""
    def add_two_numbers(self: Node, l2: Node) -> Node:
        re = Node(0)
        r = re
        carry = 0
        while self or l2:
            x = self.elem if self else 0
            y = l2.elem if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = Node(s % 10)
            r = r.next
            if self is not None:
                self = self.next
            if l2 is not None:
                l2 = l2.next
        if carry:
            r.next = Node(1)
        return re.next
