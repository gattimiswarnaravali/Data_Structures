# Given a string s, find the length of the longest substring without
#  repeating characters.
 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = ""
# Output: 0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenght = 0
        map_str = {}
        i = 0
        len_str = len(s)
        for j in range(len_str):
            
            if s[j] in map_str:
                i = max(map_str[s[j]], i)
                
            lenght = max(lenght, j-i+1)
            map_str[s[j]] = j+1
            
        return lenght
    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabdefgha"))