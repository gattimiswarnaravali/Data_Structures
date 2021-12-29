# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 23:25:18 2021

@author: SwarnaRavali
"""
from functools import reduce
class Solution:
    def get_product(self, arr):
        return reduce((lambda x,y:x*y),arr)
    def productExceptSelf(self, nums):
        length = len(nums)
        
        dict_t = {}
        for num in nums:
            dict_t[num] = dict_t.get(num,0)+1
            
        ans  = [0]*length
        nums1 = [1 if c==0 else c for c in nums]
        product = self.get_product(nums1)
        if 0 in dict_t:
            no_of_zeros = dict_t[0]
            if no_of_zeros >= 2:
                return ans
            elif no_of_zeros == 1:
                ans[nums.index(0)] = product
                return ans           
                
        
        for i in range(length):
            div = 1 if nums[i] == 0 else nums[i]
            ans[i] = int(product/div)
        return ans

    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # answer = [1]*len(nums)
        # answer[0] = 1
        # for i in range(1, len(nums)):
        #     answer[i] = answer[i-1] * nums[i-1]
        # rightProduct = 1
        # for i in range(len(nums)-1, -1, -1):
        #     print(i)
        #     answer[i] = answer[i] * rightProduct
        #     rightProduct *= nums[i]
        # return answer
        left = [1]*len(nums)
        right = [1]*len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        product = 1
        for i in range(len(nums)-1,-1,-1):
            left[i] = left[i]*product
            product *= nums[i]
        
        print(left, right)

sol = Solution()
print(sol.productExceptSelf1([1,2,3,2,3,1]))