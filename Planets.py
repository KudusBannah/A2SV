from collections import Counter
for i in range(int(input())):
    n, c = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    orbit_planents = Counter(nums)
    cost = 0
    for (orbit, count) in orbit_planents.items():
        if count < c:
            cost += count
        else:
            cost += c
    print(f"{cost}")