for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    sorted_ = sorted(nums, reverse=True)

    for i in range(len(nums)):
        if nums[i] != sorted_[0]:
            nums[i] = nums[i] - sorted_[0]
        else:
            nums[i] = nums[i] - sorted_[1]
    
    print(" ".join(list(map(str, nums))))