# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 10:36:43 2021

@author: SwarnaRavali
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if haystack == "":
            return -1
        
        start = 0
        end = len(needle)
        while(needle != haystack[start:end] and end <= len(haystack)):
            start += 1
            end += 1
        if needle == haystack[start:end]:
            return start
        else:
            return -1
        
            
            
        # for needle_index,needle_char in enumerate(needle):
        #     for hay_index, hay_char in enumerate(haystack):
        #         index = hay_index
        #         if needle_char == hay_char:
        #             while(needle_char==hay_char and needle_index<=len(needle)-1):
        #                 needle_index += 1
        #                 hay_index += 1
        #                 needle_char = needle[needle_index]
        #                 hay_char = haystack[hay_index]
        #                 if needle_index == len(needle)-1:
        #                     final_index = index
        #                     break
        #     break
        #return final_index
                
Sol = Solution()
print(Sol.strStr("aaaaaabbe", "bbe"))