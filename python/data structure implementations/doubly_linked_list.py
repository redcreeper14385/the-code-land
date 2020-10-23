import pytest


class Node(object):
    def __init__(self, value, next_node=None, previous_node=None):
        """
        Node object of the Doubl Linked List
        """
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


class DoublyLinkedList(object):
    def __init__(self, head=None):
        """
        A doubly linked list implementation
        :param head:
        """
        self.head = head

    def insert_first(self, data):
        """
        Inserts a node in the head position with
        a given data value
        :param data: Value of the node
        """
        if self.head is None:
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)

    def clear(self):
        """
        Clears the list
        """
        self.head = None

    def size(self):
        """
        Counts the number of nodes in the linked list
        :return position: Size of the liked list
        """
        if not self.head:
            return 0
        position = 0
        current = self.head
        while current:
            current = current.next_node
            position += 1
        return position

    def get_node(self, desired_position):
        """
        Get a node given it's index
        :param desired_position: Index of the node to get
        :return current: Node of the given index
        """
        if not self.head:
            return None
        position = 0
        current = self.head
        while position < desired_position:
            current = current.next_node
            position += 1
        return current


@pytest.fixture(scope="function")
def doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_first(1)
    return doubly_linked_list


@pytest.fixture(scope="function")
def big_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_first(4)
    doubly_linked_list.insert_first(3)
    doubly_linked_list.insert_first(2)
    doubly_linked_list.insert_first(1)
    return doubly_linked_list


class TestDoublyLinkedList(object):
    def test_insert_first(self, doubly_linked_list):
        """
        Given a value
        when insert_first is called,
        must insert a given value in the head position
        """
        doubly_linked_list.insert_first(2)
        assert doubly_linked_list.head.value == 2

    def test_clear(self, doubly_linked_list):
        """
        Given a doubly linked list,
        when clear is called,
        should empty out the list
        """
        doubly_linked_list.clear()
        assert doubly_linked_list.head is None

    def test_size(self, doubly_linked_list):
        """
        Given a doubly linked list,
        when size is called,
        must return the size of the list.
        """
        assert doubly_linked_list.size() == 1

    def test_get_node(self, doubly_linked_list):
        """
        Given a doubly llinked list,
        hen get node is called
        should return the node at desired position
        """
        assert doubly_linked_list.get_node(0).value == 1

    def test_insert_at(self, big_doubly_linked_list):
        """
        Given a doubly linked list
        when insert_at is called
        must insert data at desired position
        """
        big_doubly_linked_list.insert_at(100, 2)
        assert big_doubly_linked_list.get_node(2).value == 100

    def test_remove_at(self, big_doubly_linked_list):
        """
        Given a doubly linked list
        when remove_at is called
        must remove data at desired position
        """
        big_doubly_linked_list.remove_at(2)
        assert big_doubly_linked_list.get_node(2).value == 4