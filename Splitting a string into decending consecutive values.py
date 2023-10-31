class Solution:
    def splitString(self, s: str) -> bool:
        def is_valid(state):
            return state[1] == len(s)

        def get_candidates(state):
            candidates = []
            if state[0] == float("INF"):
                curr = ""
                for i in range(len(s)):
                    curr += s[i]
                    candidates.append((int(curr), i+1))
            else:
                curr = ""
                for i in range(state[1], len(s)):
                    curr += s[i]
                    if state[0] - int(curr) == 1: 
                        candidates.append((int(curr), i+1))
            return candidates


        def search(state, solutions):
            if is_valid(state):
                solutions.append(state)
                return
            
            for can in get_candidates(state):
                state = can
                search(state, solutions)
            

        solutions = []
        state = (float("INF"), -1)
        search(state, solutions)

        return len(solutions) > 1