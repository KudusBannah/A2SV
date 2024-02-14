class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        if satisfaction[-1] <= 0:
            return 0

        ans = 0
        for i in range(len(satisfaction)):
            j, curr_ans = i, 0
            while j < len(satisfaction):
                curr_ans += satisfaction[j] * (j - i + 1)
                j += 1

            ans = max(ans, curr_ans)

        return ans
        