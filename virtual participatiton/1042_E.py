#limit 2 * 10e5
import sys

input = sys.stdin.readline
print = sys.stdout.write
ans =[]

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    build = [0 for _ in range(n)]
    flag = 1
    if a[-1] != b[-1]:
        flag = 0
    build[-1] = a[-1]
    for idx in range(1, n):
        i = idx * -1 - 1
        if not (a[i] == b[i] or a[i] ^ a[i + 1] == b[i] or build[i + 1] ^ a[i] == b[i]):
            flag = 0
            break
        else:
            build[i] = b[i]
    if flag:
        ans.append("YES")
    else:
        ans.append("NO")

print("\n".join(ans))
