# Given n non-negative integers a1, a2, ..., an , where each represents
# a point at coordinate (i, ai). n vertical lines are drawn such that the 
# two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, 
# which, together with the x-axis forms a container, such that the container 
# contains the most water.

# Notice that you may not slant the container.


def maxArea(height) -> int:
    area = 0
    i = 0
    j = len(height)-1
    while(i<j):
        area = max(area, (j-i)*min(height[i], height[j]))
        if height[i] < height[j]:
            i+=1
        else:
            j-=1
    return area
                
print(maxArea([2,3,4,5,18,17,6]))