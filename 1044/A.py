import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    hash = [0 for _ in range(101)]
    flag = True
    if len(a) == 1:
        print("YES")
        flag = False

    for i in a:

        if hash[i] and flag:

            print("YES")
            flag = False
            break
        else:
            hash[i] = 1

    if flag:
        print("NO")



