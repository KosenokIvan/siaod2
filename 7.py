from deque import Deque

pos_deque = Deque()
result = ""
with open("input7.txt") as in_file:
    for line in in_file.readlines():
        num_str = line.strip("\n")
        num = int(num_str)
        if num < 0:
            result += num_str + "\n"
        else:
            pos_deque.append_end(num_str)
    while not pos_deque.is_empty():
        result += pos_deque.pop_start() + "\n"
result = result.strip()
print(result)
with open("result7.txt", "w") as out_file:
    out_file.write(result)
