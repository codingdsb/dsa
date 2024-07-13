class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self, size):
        if type(size) != int:
            raise TypeError("Size must be an integer")
        if size <= 0:
            raise Exception("Size must be atleast 1")

        self.size = size
        self.top = None

    # Get the length of filled elements

    def get_length(self):

        if self.top is None:
            return 0

        length = 0
        current_node = self.top
        while current_node is not None:
            length += 1
            current_node = current_node.next_node

        return length

    # check for emptiness

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    # check for fullness

    def is_full(self):
        if self.get_length() == self.size:
            return True
        else:
            return False

    # Push

    def push(self, data):

        if self.is_full():
            print("Stack-Overflow! 😔 Cannot add an element")
            return
        else:
            new_node = Node(data, next_node=self.top)
            self.top = new_node

    # Pop

    def pop(self):
        if self.is_empty():
            print("Stack is already empty! Nothing to pop.")
            return
        temp_node = self.top
        temp_node_data = self.top.data
        self.top = self.top.next_node
        del temp_node
        return temp_node_data

    # Peek function

    def peek(self, element_number):
        if self.is_empty():
            return IndexError("The stack is empty, cannot peek into it!")

        index = self.get_length() - element_number
        print(index)
        if 0 <= index < self.size:
            items = self.get_all_items()
            return items[index]
        else:
            raise IndexError(f"Invalid element number. Please provide a value from 1 to {self.get_length()}")

    # Display the stack
    def display(self):
        print(self.get_all_items())

    # get all data
    def get_all_items(self):
        current_node = self.top
        items = []
        while current_node is not None:
            items.append(current_node.data)
            current_node = current_node.next_node
        items.reverse()
        return items

    # stack top & bottom
    def stack_top(self):
        if self.is_empty():
            print("Sorry! Nothing to show. The stack is empty.")
        return self.top.data

    def stack_bottom(self):
        if self.is_empty():
            print("Sorry! Nothing to show. The stack is empty.")

        return self.get_all_items()[0]
