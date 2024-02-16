def solve(a, b):
    differences = set()
    standby = 0
    for i in range(len(a)):
        if a[i] >= b[i]:
            if b[i] == 0:
                standby = max(standby, a[i])
            else:
                diff = a[i] - b[i]
                differences.add(diff)
        else:
            return "NO"

    if len(differences) == 1:
        if standby <= list(differences)[0]:
            return "YES"
        else:
            return "NO"
    if len(differences) == 0:
        return "YES"
    return "NO"


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    print(solve(a, b))