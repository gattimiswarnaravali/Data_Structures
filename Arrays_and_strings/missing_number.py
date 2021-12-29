class Solution:
    def missingNumber(self, nums):
        #lent = len(nums)
        #for i in range(0,lent+1):
        #    if i not in nums:
        #        return i
            
        # num_set = set(nums)
        # n = len(nums) + 1
        # for number in range(n):
        #     if number not in num_set:
        #         return number
        
        #Bit Operation
        # missing = len(nums)
        # for i, num in enumerate(nums):
        #     print(missing,i,num)
        #     missing ^= i ^ num
        #     print("    ",missing)
        # return missing
        
        #Gaussian
        lent = len(nums)
        expected = (lent*(lent+1))//2
        original = sum(nums)
        return expected-original
        
sol = Solution()
print(sol.missingNumber([1,0,3,2,4]))