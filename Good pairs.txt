for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    curr = [(n, i) for i, n in enumerate(nums)]
    curr.sort()
    print(f"{curr[0][1] + 1} {curr[-1][1] + 1}")