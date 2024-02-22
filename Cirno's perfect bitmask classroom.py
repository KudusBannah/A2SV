def solve(x):
    count = 0
    for i in range(x.bit_length()):
        if x & (1<<i) != 0:
            count += 1
 
    # find the first 1
    i = 0
    while i < x.bit_length():
        if x & (1<<i) != 0:
            break
        i += 1
        
    if count > 1:
        return 1 << i
    else:
        # find the first 0
        j = 0
        while j < x.bit_length():
            if x & (1<<j) == 0:
                break
            j += 1
    return (1 << i) ^ (1 << j)
        
 
 
for i in range(int(input())):
    x = int(input())
    print(solve(x))