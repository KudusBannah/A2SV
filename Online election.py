class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.winners = {}
        self.getWinners()
    
    def getWinners(self):
        hashmap = defaultdict(int)
        max_ = self.persons[0]
        for i in range(len(self.persons)):
            hashmap[self.persons[i]] += 1
            if hashmap[self.persons[i]] >= hashmap[max_]:
                max_ = self.persons[i]
            self.winners[i] = max_
        
    def q(self, t: int) -> int:
        l, r = 0, len(self.persons) - 1
        best = -1
        while l <= r:
            mid = l + (r-l)//2
            if self.times[mid] > t:
                r = mid - 1
            else:
                l = mid + 1
                best = mid
        return self.winners[best]