class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = sorted(nums)
        n = len(nums)
        l = 1
        lt = 1
        for i in range(n-1):
            if N[i]==N[i+1]-1:
                lt+=1
                l=max(lt,l)
            elif N[i]!=N[i+1]:
                lt=1
        return l
