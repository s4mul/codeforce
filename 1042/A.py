import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    for j in range(n):
        cnt += max(a[j] - b[j], 0)

    print(cnt + 1)


