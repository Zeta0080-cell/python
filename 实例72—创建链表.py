class Node:
    def __init__(self, data):
        """节点类初始化，包含数据和指向下一个节点的指针"""
        self.data = data  # 存储数据
        self.next = None  # 下一个节点的指针初始化为 None


class LinkedList:
    def __init__(self):
        """链表类初始化，设置头节点为 None"""
        self.head = None  # 链表初始化时头节点为 None

    def append(self, data):
        """向链表尾部添加一个新的节点"""
        new_node = Node(data)  # 创建一个新的节点
        if not self.head:
            # 如果链表为空，将新节点设置为头节点
            self.head = new_node
        else:
            # 否则遍历链表找到最后一个节点，并将其指向新节点
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """向链表头部添加一个新的节点"""
        new_node = Node(data)  # 创建一个新的节点
        new_node.next = self.head  # 新节点的next指向当前头节点
        self.head = new_node  # 头节点指向新节点

    def display(self):
        """显示链表中的所有节点"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # 结束时输出 None，表示链表的终结

    def delete(self, data):
        """删除链表中第一个匹配的数据节点"""
        current = self.head
        # 如果头节点就需要删除
        if current and current.data == data:
            self.head = current.next  # 让头节点指向下一个节点
            current = None  # 删除节点
            return

        # 否则在链表中查找需要删除的节点
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        # 如果没有找到数据
        if current is None:
            print(f"节点 {data} 不存在。")
            return

        # 找到了节点，进行删除操作
        prev.next = current.next
        current = None  # 删除节点

    def search(self, data):
        """查找链表中是否存在某个数据"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


# 测试链表操作
if __name__ == "__main__":
    # 创建一个链表对象
    llist = LinkedList()

    # 向链表尾部添加元素
    llist.append(10)
    llist.append(20)
    llist.append(30)

    # 向链表头部添加元素
    llist.prepend(5)

    # 显示链表内容
    print("当前链表:")
    llist.display()  # 输出: 5 -> 10 -> 20 -> 30 -> None

    # 删除元素
    print("\n删除元素 20:")
    llist.delete(20)
    llist.display()  # 输出: 5 -> 10 -> 30 -> None

    # 搜索元素
    print("\n搜索元素 10:")
    print(llist.search(10))  # 输出: True

    print("\n搜索元素 100:")
    print(llist.search(100))  # 输出: False