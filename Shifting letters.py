class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        post_fix = [0] * len(shifts)
        post_fix[-1] = shifts[-1]
        for i in range(len(shifts)-2, -1, -1):
            post_fix[i] += shifts[i] + post_fix[i+1]

        output = []
        for i in range(len(shifts)):
            ascii_value = ord(s[i]) + (post_fix[i] % 26)
            while ascii_value > 122:
                ascii_value = 96 + ascii_value % 122
            output.append(chr(ascii_value))
        return "".join(output)