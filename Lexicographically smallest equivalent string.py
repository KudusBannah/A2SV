class UnionFind:
    def __init__(self):
        self.my_dict = {}
        for i in range(26):
            self.my_dict[chr(97+i)] = chr(97+i)

    
    def find(self, curr):
        if curr == self.my_dict[curr]:
            return curr
        self.my_dict[curr] = self.find(self.my_dict[curr])
        return self.my_dict[curr]

    def union(self, u, v):
        l, r = self.find(u), self.find(v)
        if l == r:
            return
        if l < r:
            self.my_dict[r] = l
            return
        self.my_dict[l] = r


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union_find = UnionFind()
        for i in range(len(s1)):
            union_find.union(s1[i], s2[i])
        
        ans = []
        for s in baseStr:
            ans.append(union_find.find(s))
        return "".join(ans)

        