class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素到栈顶"""
        return self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.__list[self.size()-1]

    def is_empty(self):
        """判断栈是否为空"""
        if len(self.__list) == 0:
            return True
        return False

    def size(self):
        """返回栈的元素的个数"""
        return len(self.__list)


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(0)
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    print(stack.size())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
