# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 22:37:39 2022

@author: SwarnaRavali
"""
import collections
class Solution:
    def firstUniqChar1(self, s: str) -> int:
        # dict_c = {}
        # for index,c in enumerate(s):
        #     if c in dict_c:
        #         dict_c[c] = (dict_c[c][0]+1,index)
        #     else:
        #         dict_c[c] = (1,index)
        
        # print(dict_c)
        # for key, val in dict_c.items():
        #     if val[0] < 2:
        #         return val[1] 
        # return -1
        dict_t = {}
        for c in s:
            dict_t[c] = dict_t.get(c,0)+1
            
        for ind, c in enumerate(s):
            if dict_t[c] == 1:
                return ind
        return -1
        
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
            

sol = Solution()
print(sol.firstUniqChar1('leetcode'))        