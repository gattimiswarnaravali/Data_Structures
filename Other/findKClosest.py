# Find K closest points
class Solution:
    def findKClosest(self,arr,k,x):
        l, r = 0,len(arr)-k
        
        while l < r:
            m = (l+r) // 2
            if x - arr[m] > arr[m+k] - x:
                l = m+1
            else:
                r = m
        return arr[l:l+k]
    
print(Solution().findKClosest([1,2,3,4,5,6],2, 5))
        
        
        
        