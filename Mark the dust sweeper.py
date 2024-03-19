def solve(arr):
    idx = n-2
    for i in range(n-1):
        if arr[i] != 0:
            idx = i
            break
    return sum(arr[idx:]) + arr[idx+1:].count(0)


for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    print(solve(arr[0:n-1]))