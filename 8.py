from stack import Stack

lines_stack = Stack()
with open("input8.txt") as in_file:
    for line in in_file.readlines():
        lines_stack.append(line)
with open("result8.txt", "w") as out_file:
    while not lines_stack.is_empty():
        line = lines_stack.pop()
        print(line.strip("\n"))
        out_file.write(line)
