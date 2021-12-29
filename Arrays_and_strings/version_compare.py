# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         ver1 = [int(i) for i in version1.split(".")]
#         ver2 = [int(i) for i in version2.split(".")]
#         n1, n2 = len(ver1),len(ver2)
        
#         for i in range(max(n1,n2)):
#             val1 = ver1[i] if i < n1 else 0
#             val2 = ver2[i] if i < n2 else 0
            
#             if val1 != val2:
#                 return -1 if val1<val2 else 1
            
#         return 0
    
class Solution:

    DELIM = '.'
    def compareVersion(self, version1: str, version2: str) -> int:
	    
        return self.cmp(self.from_str(version1), self.from_str(version2))
		
    def cmp(self,a, b):
        print(a,b)
        """Return 1 if a > b; -1 if a < b; and 0 if a == b."""
        return (a>b) - (a<b)
			
    def from_str(self,string):
        """Convert the version number from a string to a tuple. Drop
        any trailing zeroes."""
        version_list = [int(num) for num in string.split(".")]
        while version_list[-1] == 0 and len(version_list) > 1:
            del version_list[-1]
        return tuple(version_list)   
        
        
            
        
sol = Solution()
print(sol.compareVersion("0.00.0", "1.00.01"))
        