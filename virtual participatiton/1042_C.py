import sys
from collections import defaultdict

it = iter(sys.stdin.buffer.read().split())

def nxt_int():

    return int(next(it))

t = nxt_int()
for _ in range(t):
    checklist = dict()
    n = nxt_int()
    k = nxt_int()

    cnt = 0
    for i in range(n):
        idx = nxt_int() % k
        idx = min(idx, abs(k - idx))

        if not checklist.get(idx):
            checklist[idx] = 1
        else:
            checklist[idx] += 1

    res = True
    for i in range(n):
        idx = nxt_int() % k
        idx = min(idx, abs(k - idx))
        if checklist.get(idx):
            checklist[idx] -= 1
        else:
            res = False


    if res:
        print("YES")
    else:
        print("NO")

