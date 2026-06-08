#the most optimal solution using hash set, can use brute force but that is
# o(n**2), the optimal one is time compelxity of O(n) 
# space compelexity of O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()

        for x in nums:
            if x in result:
                return True
            result.add(x)
        return False