class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        state = [-1] * n
        disliked_rel = defaultdict(list)
        for rel in dislikes:
            disliked_rel[rel[0]].append(rel[1])
            disliked_rel[rel[1]].append(rel[0])

        def dfs(curr, parent):
            if state[curr-1] != -1:
                return not (state[curr - 1] == parent)

            state[curr-1] = (parent + 1) % 2
            for person in disliked_rel[curr]:
                if dfs(person, state[curr-1]) == False:
                    return False
            return True


        for i in range(1, n+1):
            if state[i-1] == -1:
                if dfs(i, 0) == False:
                    return False
        return True
        