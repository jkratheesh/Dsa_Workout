class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        suff = [1]*len(nums)
        result = [1]*len(nums)
        n = len(nums)
        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i-1]
        
        for j in range(n-2,-1,-1):
            suff[j] = suff[j+1] * nums[j+1]

        for i in range(n):
            result[i] = pref[i] *suff[i]
        
        return result