for i in range(int(input())):
    a, b = list(map(int, input().split()))
    total_teams = (a+b)//4
    min_group = min(a, b)

    start, end = 0, total_teams
    best = 0
    while start <= end:
        mid = (start+end)//2
        if mid <= min_group:
            start = mid + 1
            best = mid
        else:
            end = mid - 1
    print(best)