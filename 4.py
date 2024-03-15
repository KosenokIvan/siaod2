from stack import Stack


def check_parentheses(text_):
    parentheses_stack = Stack()
    for i, char in enumerate(text_):
        if char == "(":
            parentheses_stack.append(i)
        elif char == ")":
            if parentheses_stack.is_empty():
                return False
            parentheses_stack.pop()
    if parentheses_stack.is_empty():
        return True
    return False


with open("input4.txt") as in_file:
    text = in_file.read()
is_correct = check_parentheses(text)
print(is_correct)
with open("result4.txt", "w") as out_file:
    out_file.write(str(is_correct))
