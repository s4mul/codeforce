for i in range(int(input())):
    n = int(input())

    for j in range(n - 1):
        if j % 2 == 0:
            print(-1, end=' ')
        else:
            print(3, end=' ')
    if n % 2 == 0:
        print(2)
    else:
        print(-1)



