class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s)+2)
        
        for st, e, d in shifts:
            arr[st+1] += (1 if d == 1 else -1)
            arr[e+2] += (-1 if d == 1 else 1)

        ans = ""
        for i in range(1, len(arr)-1):
            arr[i] += arr[i-1]
            curr = (ord(s[i-1]) - ord("a") + arr[i]) % 26
            ans += chr(curr+ord("a"))
        print(arr)
        
        return ans