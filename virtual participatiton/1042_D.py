import sys
from collections import deque
input = sys.stdin.readline

class node:
    def __init__(self):
        self.inter = 0
        self.inc = []
        self.hasLeaf = 0

    def finter(self):
        self.inter += 1

    def finc(self, i):
        self.inc.append(i)

    def get_inter(self):
        return self.inter

    def get_inc(self):
        return self.inc


for _ in range(int(input())):
    n = int(input())
    nodes = [node() for __ in range(n)] # 0 base
    visited = [False for __ in range(n)]

    for i in range(n - 1):
        a, b = map(int, input().split())
        a -= 1#0base
        b -= 1
        nodes[a].finter()
        nodes[a].finc(b)
        nodes[b].finter()
        nodes[b].finc(a)

    maxLeaf = 0
    leaves = 0
    flag = 0
    for i in range(n):
        leaf = 0
        for child in nodes[i].get_inc():
            if nodes[child].get_inter() == 1:
                leaf += 1
                leaves += 1
            else:
                flag = 1
        if leaf > maxLeaf:
            maxLeaf = leaf


    print(leaves - 1 - maxLeaf + flag)




