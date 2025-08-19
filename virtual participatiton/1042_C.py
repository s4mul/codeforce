 
import sys
 
 
input = sys.stdin.readline
print = sys.stdout.write
checklist = dict()
ans = []
 
for _ in range(int(input())):
    S = []
 
    n, k = map(int, input().split())
    a = map(int, input().split())
    for i in a:
        idx = i % k
        S.append(min(idx, k - idx))
 
 
    a = map(int, input().split())
    res = True
    T = []
    for i in a:
        idx = i % k
        T.append(min(idx, k - idx))
    S.sort()
    T.sort()
    for i in range(n):
        if S[i] != T[i]:
            res = False
            break
    if res:
        ans.append("YES\n")
    else:
        ans.append("NO\n")
print(''.join(ans))
