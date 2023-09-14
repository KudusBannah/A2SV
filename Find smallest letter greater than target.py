class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l , r = 0, (len(letters) - 1)
        greater = letters[0]
        while l <= r:
            # Dont forget for overflows
            mid = (l+r)//2
            if letters[mid] > target:
                r = mid - 1
                greater = letters[mid]
            else:
                l = mid + 1
        return greater
