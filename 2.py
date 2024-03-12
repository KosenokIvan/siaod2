from deque import Deque
from encrypt import KEY

key_deque = Deque(KEY)
with open("encrypted_msg2.txt") as in_file:
    encrypted_msg = in_file.read().strip("\n")
decrypted_msg = ""
for char in encrypted_msg:
    while True:
        key_char = key_deque.pop_end()
        if key_char == char:
            key_deque.append_start(key_char)
            key_deque.append_start(key_deque.pop_end())
            decrypted_char = key_deque.pop_end()
            decrypted_msg += decrypted_char
            key_deque.append_start(decrypted_char)
            break
        key_deque.append_start(key_char)
with open("result2.txt", "w") as out_file:
    out_file.write(decrypted_msg)
