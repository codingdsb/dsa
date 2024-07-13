class Stack:

    def __init__(self, size):
        if type(size) != int:
            raise TypeError("Size must be an integer")
        if size <= 0:
            raise Exception("Size must be atleast 1")
        self.size = size
        self.top = -1
        self.items = [None] * size

    # Check for emptiness
    '''
    def is_empty(self):  # This method takes O(n) time
        for item in self.items:
            if item is not None:
                return False

        return True
        
        ⭐⭐⭐THIS METHOD IS USELESS BECAUSE IF THE FIRST INDEX ITSELF IS EMPTY, OTHERS
        MUST BE EMPTY AS IN A STACK UNTIL WE FILL THE LOWER INDICES HIGHER CAN'T
        BE FILLED!!!!⭐⭐⭐
    '''

    def is_empty(self):  # This also takes O(1) time as the alternate mentioned below
        if self.items[0] is None:
            return True
        return False

    '''
    ⭐⭐⭐ Alternate way to check for emptiness: ⭐⭐⭐
    if self.top = -1: true otherwise false => ⭐Takes O(1) time⭐
    '''

    # Check for "fullness"
    def is_full(self):  # This method takes O(n) time
        for item in self.items:
            if item is None:
                return False

        return True

    '''
    ⭐⭐⭐ Alternate way to check for fullness: ⭐⭐⭐
    if self.top = (self.size -1) : true otherwise false => ⭐Takes O(1) time⭐
    '''

    # push
    def push(self, item_data):
        if self.is_full():
            raise IndexError("Stack-Overflow! 😔 Cannot add an element")
        self.top += 1
        self.items[self.top] = item_data

    # pop
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is already empty")
        temp = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return temp

    # peek from top
    def peek(self, element_number):

        if self.is_empty():
            return IndexError("The stack is empty, cannot peek into it!")

        index = self.top - element_number + 1
        if 0 <= index < self.size:
            return self.items[index]
        else:
            raise IndexError(f"Invalid element number. Please provide a value from 1 to {self.size}")

    # display the stack
    def display(self):
        if self.is_empty():
            print("Sorry! Nothing to show. The stack is empty.")
        else:
            i = self.top
            while i>=0:
                print(self.items[i])
                i-=1

    # stack top and bottom
    def stack_top(self):
        if self.is_empty():
            print("Sorry! Nothing to show. The stack is empty.")
        return self.items[self.top]

    def stack_bottom(self):
        if self.is_empty():
            print("Sorry! Nothing to show. The stack is empty.")
        return self.items[0]
