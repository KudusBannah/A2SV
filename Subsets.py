class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def is_valid(state):
            return len(state) <= len(nums)

        def get_candidates(state):
            candidates = []
            start = max(state) if state else float("-inf")
            for num in nums:
                if num > start:
                    candidates.append(num)
            return candidates

        def search(state, solutions):
            if is_valid(state):
                solutions.append(state.copy()) 
        
            for can in get_candidates(state):
                state.add(can)
                search(state, solutions)
                state.remove(can)
                

        solutions = []
        state = set()
        search(state, solutions)
        return solutions