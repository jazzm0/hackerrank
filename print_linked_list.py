import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


def printLinkedList(head):
    while head is not None:
        print(head.data)
        head = head.next


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        llist = SinglyLinkedList()
        llist.insert_node(1)
        llist.insert_node(2)
        llist.insert_node(3)
        printLinkedList(llist.head)


if __name__ == '__main__':
    unittest.main()
