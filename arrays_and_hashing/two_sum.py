#time complexity is o(n) and space complexity is o(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index,value in enumerate(nums):

            comp = target - value
            if comp in hashMap:
                return [hashMap[comp],index]
            

            hashMap[value] = index