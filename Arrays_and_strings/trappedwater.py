from collections import deque
class Solution:
    def trap(self, height):
        # left_max = [0]*len(height)
        # right_max = [0]*len(height)
        
        # sizee = len(height)
        # left_max[0] = height[0]
        # right_max[sizee-1]=height[sizee-1]
        
        # for i in range(1,sizee):
        #     left_max[i] = max(height[i], left_max[i-1])
        # for i in range(sizee-2,0,-1):
        #     right_max[i] = max(height[i], right_max[i+1])        
            
        # ans=0
        # for i in range(1, sizee-1):
        #     ans += min(left_max[i],right_max[i])-height[i]
            
        # return ans
        ans = 0
        current = 0
        sta = []
        print(dir(sta))
        print(height)
        while(current<len(height)):
            while (len(sta)> 0 and (height[current]>height[sta[-1]])):
            # if (sta.qsize() is not 0):
            # if 1:
                top = sta.pop()
                if len(sta)==0:
                    break;
                dist = current-sta[-1]-1
                bound_ht = min(height[current], height[sta[-1]])-height[top]
                ans+=dist*bound_ht
            sta.append(current)
            current+=1
        return ans
    

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))