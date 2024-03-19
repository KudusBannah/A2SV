for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        arr[i] = n - arr[i] + 1

    print(*arr)