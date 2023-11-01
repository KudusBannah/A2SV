class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def is_valid(state):
            return len(state) == len(nums)

        def get_candidates(state):
            candidates = []
            return set(nums) - set(state)

        def search(state, solutions):
            if is_valid(state):
                solutions.append(state.copy())
                return
            
            for can in get_candidates(state):
                state.append(can)
                search(state, solutions)
                state.pop()

        

        solutions = []
        state = []
        search(state, solutions)
        return solutions