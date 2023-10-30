class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def is_valid(state):
            return len(state) == k
        
        def get_candidates(state):
            start = max(state) if state else 0
            candidates = []
            for i in range(start+1, n+1):
                candidates.append(i)
            return candidates

        def search(state):
            if is_valid(state):
                solutions.append(state.copy())
                return 
            
            for candidate in get_candidates(state):
                state.append(candidate)
                search(state)
                state.pop()


        solutions = []
        state = []
        search([])
        return solutions