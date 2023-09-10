class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_needed = 0
        k_tickets = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                time_needed += min(tickets[i], k_tickets)
            else:
                time_needed += min(tickets[i], k_tickets-1)
        return time_needed