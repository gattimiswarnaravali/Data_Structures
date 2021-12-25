# Given an array of integers nums and an integer target, return indices of the 
# two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1]

class Solution:
    def twoSum(self, nums, target: int):
        map_num_ind = {}
        for i,num in enumerate(nums):
            required_num = target - num
            if required_num in map_num_ind:
                return [i, map_num_ind[required_num]]
            map_num_ind[num]=i
            

sol = Solution()
print(sol.twoSum([2,7,11,23], 9))