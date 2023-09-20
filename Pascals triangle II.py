class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr = 0
        def generate_sequence(curr, n):
            if curr == rowIndex:
                return n
            arr = [1]
            for i in range(len(n)-1):
                arr.append(n[i] + n[i+1])
            arr.append(1)
            return generate_sequence(curr+1, arr)

        return generate_sequence(curr, [1])