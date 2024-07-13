# The following code can be extended to closure matching which matches all kinds of closures: (), {}, [], '', ""

class Stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.paren = [None] * size  # paren is just the short for parenthesis array

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def push(self, data):
        self.top += 1
        self.paren[self.top] = data

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is already empty")
        self.paren[self.top] = None
        self.top -= 1


def match_parenthesis(expression: str) -> dict:
    """
    Function to do the parenthesis matching task
    returns True with success message if the parenthesis are balanced
    returns False with failure message if the parenthesis are unbalanced
    """

    stk = Stack(
        len(expression))  # stack size = len of expression: for worst case when all characters of the expression = (
    for character in expression:
        if character == "(":
            stk.push(character)
            continue
        if character == ")":
            try:
                stk.pop()
            except IndexError:
                return {
                    "result": False,
                    "message": "Unexpected closing parenthesis \')\'"
                }
    if stk.is_empty():
        return {
            "result": True,
            "message": "Expression is balanced"
        }
    else:
        opened_brackets = 0
        for p in stk.paren:
            if p is None:
                break
            opened_brackets += 1
        return {
            "result": False,
            "message": f"{opened_brackets} opened parenthesis are not closed"
        }

