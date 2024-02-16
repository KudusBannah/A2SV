class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = n & 1
        for i in range(1, n.bit_length()):
            if (n >> i) & 1 == curr:
                return False
            curr = (n >> i) & 1

        return True
        