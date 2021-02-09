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
        new_node.next = self.head
        self.head = new_node


def reverse(head):
    return head


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        llist = SinglyLinkedList()
        llist.insert_node(1)
        llist.insert_node(2)
        llist.insert_node(3)
        self.assertEqual(reverse(llist.head).data, 3)


if __name__ == '__main__':
    unittest.main()
