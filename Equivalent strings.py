memo = {}
def is_equal(a, b):
    if (a,b) in memo: return memo[a,b]
    if len(a) == 1: return a == b
    if len(a)%2 == 1: return a == b

    a1, a2 = a[:len(a)//2], a[len(a)//2:]
    b1, b2 = b[:len(a)//2], b[len(a)//2:]
    
    if (a1 == b1 and a2 == b2) or (a1 == b2 and a2 == b1): 
        memo[a, b] = True
        return True
    memo[a,b] = (is_equal(a1, b1) and is_equal(a2, b2)) or (is_equal(a1, b2) and is_equal(a2, b1))
    return memo[a, b]



a = input()
b = input()
if is_equal(a,b): print("YES")
else: print("NO")