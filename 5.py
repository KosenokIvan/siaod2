from deque import Deque


def check_brackets(text_):
    brackets_deque = Deque()
    for i, char in enumerate(text_):
        if char == "[":
            brackets_deque.append_end(i)
        elif char == "]":
            if brackets_deque.is_empty():
                return False
            brackets_deque.pop_end()
    return brackets_deque.is_empty()


with open("input5.txt") as in_file:
    text = in_file.read()
is_correct = check_brackets(text)
print(is_correct)
with open("result5.txt", "w") as out_file:
    out_file.write(str(is_correct))
