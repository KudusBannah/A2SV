class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def backtrack(i):
            if i == n+1:
                return [[]]

            res_perms = []
            perms = backtrack(i+1)

            for p in perms:
                for j in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(j, i)
                    res_perms.append(p_copy)
            return res_perms

        ans = backtrack(1)
        ans.sort()
        return "".join([str(el) for el in ans[k-1]])