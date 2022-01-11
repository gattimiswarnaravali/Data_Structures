# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

# class Solution:
#     def reorderLogFiles(self, logs):
#         l = filter(lambda l: l[l.find(" ") + 1].isalpha(), logs)
#         d = filter(lambda l: l[l.find(" ") + 1].isdigit(), logs)
#         return sorted(l, key = lambda x: (x[x.find(" "):], x[:x.find(" ")])) + list(d)
        
        
class Solution:
    def reorderLogFiles(self, logs):

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
sol = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(sol.reorderLogFiles(logs))

# l = filter(lambda l: l[l.find(" ") + 1].isalpha(), logs)   
# print([lambda l: l[l.find(" ") + 1].isalpha(), logs])
# xa = [[1, 2,6, 3],[4,3,6,2],[3,4,2,1]]
# # vv= lambda n:(n*n)
# # print(vv([4,6]))

# # summy = [lambda x:( n for n in x)]
# print(sorted(xa, key = lambda x:x[0]))

# # print(summy([3,4]))
d = ['g1 act car', 'ab1 off key dog', 'a8 act zoo']
print(list(filter(lambda l: l[l.find(" ") + 1].isalpha(), logs)))
# print(sorted(d, key = lambda x:x[:x.find(" ")]))
print(logs[1][logs[1].find(" ") + 1].isalpha())
_id, rest,s = logs[0].split(" ", maxsplit=2)
print(_id)
print(rest)
print(s)
