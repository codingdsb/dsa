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

    def pop(self) -> str:
        if self.is_empty():
            raise IndexError("Stack is already empty")
        temp = self.paren[self.top]
        self.paren[self.top] = None
        self.top -= 1
        return temp


def check_corresponding_brace(opening_brace, closing_brace):
    if (opening_brace == "(" and closing_brace == ")") or (opening_brace == "[" and closing_brace == "]") or (
            opening_brace == "{" and closing_brace == "}"):
        return True
    return False


def match_brackets(expression: str) -> dict:
    stk = Stack(len(expression))

    for character in expression:

        if character == "(" or character == "[" or character == "{":
            stk.push(character)
            continue
        if character == ")" or character == "]" or character == "}":
            try:
                popped_brace = stk.pop()
                is_corresponding_brace = check_corresponding_brace(popped_brace, character)
                if is_corresponding_brace is False:
                    return {
                        "result": False,
                        "message": f"Expected to close {popped_brace} first, but got {character}"
                    }

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
            "message": f"{opened_brackets} opened brackets are not closed"
        }