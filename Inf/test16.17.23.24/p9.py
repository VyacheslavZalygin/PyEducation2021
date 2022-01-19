import sys

s = sys.stdin.read().strip()
max_len = None
cur_len = 0
for e in s:
    if  (cur_len % 3 == 0 and e == "X") or \
        (cur_len % 3 == 1 and e == "Y") or \
        (cur_len % 3 == 2 and e == "Z"):
         cur_len += 1
    else:
        if (max_len == None or max_len < cur_len) and cur_len != 0:
            max_len = cur_len
        cur_len = 0
        if e == "X":
            cur_len += 1

if (max_len == None or max_len < cur_len) and cur_len != 0:
    max_len = cur_len

print(max_len)