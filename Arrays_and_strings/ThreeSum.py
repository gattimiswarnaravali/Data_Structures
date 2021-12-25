class Solution:
    def threeSum(self, nums: list):
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 -val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1,val2,complement))))
                    seen[val2] = i
        return res
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,7,11,23,-9, -2]))