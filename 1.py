from deque import Deque

with open("books.txt", encoding="utf-8") as in_file:
    deque1 = Deque()
    deque2 = Deque()
    for line in in_file.readlines():
        if line:
            deque1.append_end(line)
sorted_length = 0
while not deque1.is_empty():
    min_title = deque1.pop_start()
    deque1.append_end(None)  # Маркер конца
    while True:
        next_title = deque1.pop_start()
        if next_title is None:
            break
        if next_title < min_title:
            min_title, next_title = next_title, min_title
        deque1.append_end(next_title)
    deque2.append_end(min_title)
with open("result1.txt", "w") as out_file:
    while not deque2.is_empty():
        out_file.write(deque2.pop_start())
