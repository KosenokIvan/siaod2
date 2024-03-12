from deque import Deque

KEY = "rpAmCRLXNIfPdk,itGOEUbnVuqKoxDe.aTgBHWQZvSwJlyYsF jczMh"

key_deque = Deque(KEY)
with open("message2.txt") as in_file:
    msg = in_file.read().strip("\n")
encrypted_msg = ""
for char in msg:
    while True:
        key_char = key_deque.pop_start()
        if key_char == char:
            key_deque.append_end(key_char)
            key_deque.append_end(key_deque.pop_start())
            encrypted_char = key_deque.pop_start()
            encrypted_msg += encrypted_char
            key_deque.append_end(encrypted_char)
            break
        key_deque.append_end(key_char)
with open("encrypted_msg2.txt", "w") as out_file:
    out_file.write(encrypted_msg)
