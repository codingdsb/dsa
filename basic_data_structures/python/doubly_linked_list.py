class LengthNotEnoughException(Exception):

    def __init__(self, length):
        print(f"The length of linked list ({length}) is not enough")


class Node:

    def __init__(self, data, next_node, previous_node):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class DoublyLinkedList:

    def __init__(self):
        self.head = None  # Define empty linked list

    # Get length of the linked list
    def get_length(self):

        if self.head is None:
            return 0

        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next_node

        return length

    # get index of node by data

    def get_index_by_data(self, data):
        if self.get_length() == 0:
            return -1
        current_node = self.head
        i = 0

        while i != (self.get_length()):
            if current_node.data == data:
                return i
            i += 1
            current_node = current_node.next_node
        return -2

    # Insertion at beginning

    def insert_at_beginning(self, data):
        if self.head is not None:
            new_node = Node(data, next_node=self.head, previous_node=None)
            self.head = new_node
        else:
            new_node = Node(data, None, None)
            self.head = new_node

    # Insertion at the end

    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data, None, None)
            self.head = new_node
            return
        current_node = self.head
        while True:
            if current_node.next_node is None:
                new_node = Node(data, next_node=None, previous_node=current_node)
                current_node.next_node = new_node
                break
            current_node = current_node.next_node

    # Insertion at an index
    def insert_at_index(self, data, index):
        length = self.get_length()

        if index == length:
            self.insert_at_end(data)
        elif index == 0:
            self.insert_at_beginning(data)
        elif index > length:
            raise LengthNotEnoughException(length)
        else:
            i = 0
            current_node = self.head

            # reach the required node
            while i != (index - 1):
                current_node = current_node.next_node
                i += 1

            new_node = Node(data, next_node=current_node.next_node, previous_node=current_node)
            current_node.next_node = new_node

    # Insertion after a particular node
    def insert_after_node(self, data, existing_data):
        index = self.get_index_by_data(existing_data)
        if index == -1:
            print("Linked list is empty")

        elif index == -2:
            print(f"{existing_data} does not exist in the linked list")
        else:
            self.insert_at_index(data, index+1)

    # Appending of a list
    def append_list(self, list_to_append):
        for element in list_to_append:
            self.insert_at_end(element)

    # Traversal

    def get_all_nodes(self):
        current_node = self.head
        nodes = []
        while current_node is not None:
            nodes.append(current_node)
            current_node = current_node.next_node

        return nodes

    def get_all_nodes_data(self):
        current_node = self.head
        nodes_data = []
        while current_node is not None:
            nodes_data.append(current_node.data)
            current_node = current_node.next_node

        return nodes_data

    # Deletion by index
    def delete_by_index(self, index):
        length = self.get_length()

        if index >= length:
            raise LengthNotEnoughException(length)
        elif index == 0:
            self.head = self.head.next_node
            self.head.previous_node = None
        else:
            previous_of_node_to_delete = self.head
            i = 0
            while i != (index-1):
                i += 1
                previous_of_node_to_delete = previous_of_node_to_delete.next_node

            temp = previous_of_node_to_delete.next_node
            previous_of_node_to_delete.next_node = previous_of_node_to_delete.next_node.next_node
            previous_of_node_to_delete.next_node.next_node.previous_node = previous_of_node_to_delete
            del temp

    # Deletion by data
    def delete_by_data(self, data):

        index = self.get_index_by_data(data)

        if index == -1:
            print("Linked list is empty")

        elif index == -2:
            print(f"{data} does not exist in the linked list")

        else:
            self.delete_by_index(index)
