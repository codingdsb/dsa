class LengthNotEnoughException(Exception):

    def __init__(self, length):
        print(f"The length of linked list ({length}) is not enough")


class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class CircularLinkedList:

    def __init__(self):
        self.head = Node(None, None)
        self.head.next_node = self.head  # Self pointing

    # Get length of linked list
    def get_length(self):

        if self.head.data is None:
            return 0

        if self.head.next_node == self.head:
            return 1

        length = 1  # accounting for the head node
        current_node = self.head.next_node

        while current_node != self.head:
            length += 1
            current_node = current_node.next_node

        return length

    # get index by data

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

    # Insert after node

    def insert_after_node(self, existing_data, data):

        index = self.get_index_by_data(existing_data)

        if index == -1:
            print("Linked list is empty")
            return

        if index == -2:
            print(f"{existing_data} does not exist in the linked list")
            return

        i = 0
        current_node = self.head

        while i != index:
            i += 1
            current_node = current_node.next_node
        new_node = Node(data, current_node.next_node)
        current_node.next_node = new_node

    # Insert at beginning

    def insert_at_beginning(self, data):

        new_node = Node(data, self.head)

        if self.get_length() == 0:
            new_node.next_node = new_node
            self.head = new_node
            return

        if self.get_length() == 1:
            self.head.next_node = new_node
            self.head = new_node
            return

        current_node = self.head
        while current_node.next_node != self.head:
            current_node = current_node.next_node
        current_node.next_node = new_node
        self.head = new_node

    # get all nodes

    def get_all_nodes(self):
        if self.head.data is None:
            return []
        nodes = [self.head]
        current_node = self.head.next_node
        while current_node != self.head:
            nodes.append(current_node)
            current_node = current_node.next_node
        return nodes

    # get all nodes data

    def get_all_nodes_data(self):
        if self.head.data is None:
            return []

        nodes_data = [self.head.data]
        current_node = self.head.next_node

        while current_node != self.head:
            nodes_data.append(current_node.data)
            current_node = current_node.next_node

        return nodes_data

    # deletion by index

    def delete_by_index(self, index):
        if index >= self.get_length():
            raise LengthNotEnoughException(self.get_length())

        elif self.get_length() == 1:
            self.head.data = None

        else:

            i = 0
            previous_of_node_to_delete = self.head
            while i != (index - 1):
                i += 1
                previous_of_node_to_delete = previous_of_node_to_delete.next_node
            temp = previous_of_node_to_delete.next_node
            previous_of_node_to_delete.next_node = previous_of_node_to_delete.next_node.next_node
            del temp


    def delete_by_data(self, existing_data):

        index = self.get_index_by_data(existing_data)

        if index == -1:
            print("Linked list is empty")
        elif index == -2:
            print(f"{existing_data} does not exist in the linked list")
        else:
            self.delete_by_index(index)

