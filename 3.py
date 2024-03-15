from stack import Stack


def hanoi(stacks_, from_index, to_index, n):
    if n <= 1:
        stacks_[to_index].append(stacks_[from_index].pop())
    else:
        indexes = list(range(3))
        indexes.remove(from_index)
        indexes.remove(to_index)
        temp_index = indexes[0]
        hanoi(stacks_, from_index, temp_index, n - 1)
        hanoi(stacks_, from_index, to_index, 1)
        hanoi(stacks_, temp_index, to_index, n - 1)


with open("hanoi3.txt") as in_file:
    disks = sorted([int(line) for line in in_file.readlines() if line])
stacks = Stack(disks), Stack(), Stack()
hanoi(stacks, 0, 2, len(disks))
result = ""
for stack in stacks:
    while not stack.is_empty():
        result += str(stack.pop()) + " "
    result += "\n"
print(result)
with open("result3.txt", "w") as out_file:
    out_file.write(result)
