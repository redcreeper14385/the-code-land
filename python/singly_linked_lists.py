import pytest


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, data):
        """
        creates a new Node from data
        and assigns the Node to the
        head property.
        :param data: Object
        :return new_head: New head node
        """
        self.head = Node(data, self.head)

    def size(self):
        """
        Counts the number of nodes in the linked list
        :return list_size: Size of the liked list
        """
        list_size = 0
        current = self.head
        while current:
            current = current.next_node
            list_size += 1
        return list_size

    def get_head_node(self):
        """
        Gets the head node of the linked list
        :return self.head: Head node of the linked list
        """
        return self.head

    def get_tail_node(self):
        """
        Gets the tail node of the linked list
        :return current: Tail node of the linked list
        """
        if self.head is None:
            return None
        current = self.head
        while current.next_node:
            current = current.next_node
        return current

    def clear(self):
        """
        Clears the linked list setting the head node to None
        :return self.head:
        """
        self.head = None

    def remove_head(self):
        """
        Removes the head node of the linked list,
        making the node next to it the new head
        """
        if self.head.next_node:
            self.head = self.head.next_node
        else:
            self.head = None

    def remove_tail(self):
        """
        Removes the tail node of the linked list,
        making the node previous to it the new tail
        """
        previous = self.head
        current = self.head.next_node
        while current.next_node:
            previous = current
            current = current.next_node
        previous.next_node = None

    def insert_last(self, data):
        """
        Inserts a new node in the last position of the linked list
        :param data: Value of the node that is being inserted
        """
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)

    def get_node(self, index):
        """
        Get a node given it's index
        :param index: Index of the node to get
        :return current: Node of the given index
        """
        i = 0
        current = self.head
        while i <= index:
            current = current.next_node
            i += 1
        return current

    def insert_at(self, data, index):
        """
        Inserts a new node with given data value,
        in the given index position
        :param data: Value of the new node
        :param index: Position of the new node that is being inserted
        """
        previous = self.get_node(index - 1)
        node = Node(data, previous.next_node)
        previous.next_node = node

    def remove_at(self, index):
        """
        Removes a node at given index
        :param index: Index of the node to be removed
        """
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next_node
            return
        previous = self.get_node(index - 1)
        if previous.next_node:
            previous.next_node = previous.next_node.next_node
        else:
            return


@pytest.fixture(scope='function')
def linked_list():
    linked_list = SinglyLinkedList()
    return linked_list


class TestSinglyLinkedList:
    def test_insert_node_must_insert_a_new_node(self, linked_list):
        linked_list.insert_first(1)
        assert linked_list.head.value == 1

    def test_insert_node_must_link_with_previous_head(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        assert linked_list.head.value == 2
        assert linked_list.head.next_node.value == 1

    def test_size_must_count_correct_number_of_nodes(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(1)
        linked_list.insert_first(1)

        assert linked_list.size() == 3

    def test_get_head_node_must_return_the_head(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        head = linked_list.get_head_node()
        assert head.value == 2

    def test_get_tail_node_must_return_the_last_node(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        tail = linked_list.get_tail_node()
        assert tail.value == 1

    def test_get_tail_node_must_return_None_when_list_is_empty(self, linked_list):
        tail = linked_list.get_tail_node()
        assert tail is None

    def test_clear_must_clear_all_nodes(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.clear()
        assert linked_list.head is None

    def test_remove_head_node(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.remove_head()
        assert linked_list.head.value == 1

    def test_remove_head_node_must_return_None_if_only_head(self, linked_list):
        linked_list.insert_first(2)
        linked_list.remove_head()
        assert linked_list.head is None

    def test_remove_tail(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.remove_tail()
        assert linked_list.get_tail_node().value == 2

    def test_insert_last(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_last(4)
        assert linked_list.get_tail_node().value == 4

    def test_get_node(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        assert linked_list.get_node(1).value == 2

    def test_insert_at(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        linked_list.insert_at(10, 2)
        assert linked_list.get_node(2).value == 10

    def test_remove_at(self, linked_list):
        linked_list.insert_first(1)
        linked_list.insert_first(2)
        linked_list.insert_first(3)
        linked_list.insert_first(4)
        linked_list.remove_at(1)
        assert linked_list.get_node(1).value == 1

