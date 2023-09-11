class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for item in s:
            if item == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score*2, 1)
        return score