class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def checkPower(x):
            if x < 1:
                return False
            if x == 1:
                return True
            return checkPower(x/4)
        return checkPower(n)