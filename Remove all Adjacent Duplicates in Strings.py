class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        letters = []
        consistencies = [1]
        for letter in s:
            if letters and letters[-1] == letter: consistencies[-1] += 1
            else: consistencies.append(1)

            letters.append(letter)
            if consistencies[-1] == k:
                del letters[-k:]
                consistencies.pop()

        return "".join(letters)