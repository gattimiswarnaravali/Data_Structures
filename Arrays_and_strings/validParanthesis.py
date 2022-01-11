# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 23:00:49 2022

@author: SwarnaRavali
"""

from collections import deque
dict_brackets = {']':'[',
                 '}':'{',
                 ')':'(',
                 '>':'<'}
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for c in s:
            if c in dict_brackets:
                if q:
                    par = q.pop() 
                    if dict_brackets[c] != par:
                        return False
                else:
                    q.append(c)
            else:
                q.append(c)
                
        return not q
    

sol = Solution()
print(sol.isValid('({})'))  