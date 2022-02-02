class Solution:
    def valid_paranthesis(self, strn):
        left_min, left_max = 0,0
        
        for s in strn:
            if s == "(":
                left_min += 1
                left_max += 1
            elif s == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0
        
print(Solution().valid_paranthesis("((()))()"))