from stack import Stack

with open("input6.txt") as in_file:
    text = in_file.read().strip("\n")
num_stack = Stack()
letters_stack = Stack()
others_stack = Stack()
buffer_stack = Stack()
result = ""
for char in text:
    if char.isdigit():
        num_stack.append(char)
    elif char.isalpha():
        letters_stack.append(char)
    else:
        others_stack.append(char)
while not num_stack.is_empty():
    buffer_stack.append(num_stack.pop())
while not buffer_stack.is_empty():
    result += buffer_stack.pop()
while not letters_stack.is_empty():
    buffer_stack.append(letters_stack.pop())
while not buffer_stack.is_empty():
    result += buffer_stack.pop()
while not others_stack.is_empty():
    buffer_stack.append(others_stack.pop())
while not buffer_stack.is_empty():
    result += buffer_stack.pop()
with open("result6.txt", "w") as out_file:
    print(result)
    out_file.write(result)
