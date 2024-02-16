def solve(nums, k):
    i = 30
    while i >= 0 and k > 0:
        count = 0
        for num in nums:
            if num & (1 << i) == 0:
                count += 1

        if count <= k:
            k -= count
            for j in range(len(nums)):
                nums[j] |= (1 << i)

        i -= 1
    
    ans = nums[0]
    for i in range(1, len(nums)):
        ans &= nums[i]

    return ans



for i in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    print(solve(nums, k))