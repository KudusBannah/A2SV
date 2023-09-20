class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def checkPower(x):
            if x < 1:
                return False
            if x == 1:
                return True
            return checkPower(x/3)
        return checkPower(n)