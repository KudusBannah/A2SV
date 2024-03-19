def solve(s):
    count, max_ = 1, 0
    for i in range(n-1):
        if s[i] == s[i+1] == ".":
            count += 1
            max_ = max(count, max_)
        else:
            count = 1
    return 2 if max_ > 2 else s.count(".")


for i in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s))
