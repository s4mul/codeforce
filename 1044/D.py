import sys
from collections import deque
input = sys.stdin.readline
#time:  n log n

def slice(i, n, jockey):
    hit = jockey[i]
    fall(0, i, jockey, n)
    return hit

def fall(base, i, jockey, n, real):
    if i >= n or jockey[i] == 0:
        return 0
    dmg = i - base + 1
    if jockey[i + 1] - dmg <= 0:
        if real:
            jockey[i + 1] = 0
        return jockey[i + 1] + fall(i + 1, i + 2, jockey, n, real)
    else:
        if real:
            jockey[i + 1] -= dmg
        return dmg
a = [1, 1, 1, 0]
print(fall(0, 0, a, 3, True))
print(a)
for _ in range(int(input())):
    n = int(input())
    jockey = list(map(int, input().split()))
    bottom = deque([(0, n-1)])
    hit = 0
    while bottom:

        head, tail = bottom.popleft()
        maxreduce = jockey[head] + jockey[head + 1] - 1
        maxidx = 0
        for i in range(head + 1, tail):
            dmg = fall(head, i, jockey, n, False)
            if dmg >= maxreduce:
                maxreduce = dmg
                maxidx = i

        hit += jockey[maxidx]
        fall(head, maxidx, jockey, n, True)
        newtail = newhead = maxidx
        while jockey[newhead] == 0 and newhead < tail:
            newhead += 1
        while jockey[newtail] == 0 and newtail > head:
            newtail -= 1

        if newhead > tail:
            bottom.append(newhead, tail)
        if newtail < tail:
            bottom.append(head, newtail)

    print(hit)


