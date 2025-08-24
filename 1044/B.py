import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    g = list(map(int, input().split()))
    g.sort()
    ans = 0
    flag = n % 2
    for i in range(n // 2):
        
        ans += g[i * 2 + 1 + flag]
    if flag:
        ans += g[0]

    print(ans)



