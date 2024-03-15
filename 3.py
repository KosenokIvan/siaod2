from stack import Stack


def hanoi(stacks_, from_index, to_index, n, result_str):
    if n <= 1:
        disk_size = stacks_[from_index].pop()
        stacks_[to_index].append(disk_size)
        result_str += f"Move disk (size = {disk_size}) from {from_index + 1} to {to_index + 1}\n"
        return result_str
    else:
        indexes = list(range(3))
        indexes.remove(from_index)
        indexes.remove(to_index)
        temp_index = indexes[0]
        result_str = hanoi(stacks_, from_index, temp_index, n - 1, result_str)
        result_str = hanoi(stacks_, from_index, to_index, 1, result_str)
        result_str = hanoi(stacks_, temp_index, to_index, n - 1, result_str)
        return result_str


with open("hanoi3.txt") as in_file:
    disks = sorted([int(line) for line in in_file.readlines() if line])
stacks = Stack(disks), Stack(), Stack()
result = hanoi(stacks, 0, 2, len(disks), "")
print(result)
with open("result3.txt", "w") as out_file:
    out_file.write(result)
