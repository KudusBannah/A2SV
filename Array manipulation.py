def arrayManipulation(n, queries):
    diff_arr = [0] * (n + 2) 
    for st,end, k in queries:
        diff_arr[st] += k 
        diff_arr[end + 1] -= k 
    for i in range(1,len(diff_arr)):
        diff_arr[i] += diff_arr[i - 1] 
    return max(diff_arr) 