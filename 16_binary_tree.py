class Node(object):
    """"""
    def __init__(self, item):
        self.elem = item
        self.l_child = None
        self.r_child = None


class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        queue = [self.root]

        if self.root is None:
            self.root = node
            return

        while queue:
            cur_node = queue.pop(0)
            if cur_node.l_child is not None:
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)
            if cur_node.r_child is not None:
                cur_node.r_child = node
                return
            else:
                queue.append(cur_node.r_child)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.l_child is not None:
                queue.append(cur_node.l_child)
            if cur_node.r_child is not None:
                queue.append(cur_node.r_child)


