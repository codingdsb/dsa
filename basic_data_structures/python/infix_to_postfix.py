from stack_by_array import Stack

operator_precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

'''
Function to convert infix to postfix
'''


def infix_to_postfix(expression):
    operator_stack = Stack(len(expression))

    postfix_expression = ''

    for character in expression:

        if character == '(':
            operator_stack.push(character)

        elif character == ')':
            foundopener = False
            while foundopener is False:
                popped_operator = operator_stack.pop()
                if popped_operator == '(':
                    foundopener = True
                else:
                    postfix_expression += popped_operator

        elif character in operator_precedence.keys():

            if operator_stack.top == -1 or operator_stack.stack_top() == '(':
                operator_stack.push(character)
            elif operator_precedence[character] > operator_precedence[operator_stack.stack_top()]:
                operator_stack.push(character)
            else:
                pushed = False
                while pushed is False:
                    if (not operator_stack.is_empty()) and operator_precedence[character] <= operator_precedence[
                        operator_stack.stack_top()]:
                        popped_operator = operator_stack.pop()
                        postfix_expression += popped_operator
                        continue
                    operator_stack.push(character)
                    pushed = True


        else:
            postfix_expression += character

    while operator_stack.top > -1:
        popped_operator = operator_stack.pop()
        postfix_expression += popped_operator

    return postfix_expression