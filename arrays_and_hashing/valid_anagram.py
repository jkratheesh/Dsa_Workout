#optimal is using dictionary with time o(n) and space o(n)
#also can use counter with same time and space

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        freq = {}

        for n in s:
            freq[n] = freq.get(n,0) + 1
        
        for ch in t:

            if ch not in freq:
                return False
            
            freq[ch] -= 1

            if freq[ch] < 0:
                return False
        return True