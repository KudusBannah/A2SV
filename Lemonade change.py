class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten_bill, five_bill = 0, 0

        for bill in bills:
            if bill != 5:
                change = bill - 5
                if change == 5 and five_bill > 0:
                    five_bill -= 1
                    ten_bill += 1
                elif change == 15 and (five_bill > 0 and ten_bill > 0):
                    five_bill -= 1
                    ten_bill -= 1
                elif change == 15 and (five_bill > 2):
                    five_bill -= 3
                else:
                    return False
            else:
                five_bill += 1
        
        return True