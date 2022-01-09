# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"
 
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        # punctuations = [".",",","!","?","!","'",'"',";",":","<",">"]
        # for punct in punctuations:
        #     paragraph = paragraph.replace(punct," ")
        # para_words = paragraph.split(" ")
        # para_words_lower = [word.lower() for word in para_words]
        # dict_words = {}
        # for word in para_words_lower:
        #     if word not in banned and word != "":
        #         if word in dict_words:
        #             dict_words[word] = dict_words[word]+1
        #         else:
        #             dict_words[word] = 1
            
        # repetion_list = list(dict_words.values())
        # ind = repetion_list.index(max(repetion_list))
        # return list(dict_words.keys())[ind]
        # punctuations = [".",",","!","?","!","'",'"',";",":","<",">"]
        paragraph = paragraph.lower()
        # for punct in punctuations:
        #     paragraph = paragraph.replace(punct," ")
        para_lower = re.sub(r"[!?',;.]+",' ',paragraph)
        para_words = para_lower.split(" ")
        
        counter_data = Counter(para_words).most_common()
        for word,_ in counter_data:
            if word not in banned:
                return word

# paragraph = "L, P! X! C; u! P? w! P. G, S? l? X? D. w? m? f? v, x? i. z; x' m! U' M! j? V; l. S! j? r, K. O? k? p? p, H! t! z' X! v. u; F, h; s? X? K. y, Y! L; q! y? j, o? D' y? F' Z; E? W; W' W! n! p' U. N; w? V' y! Q; J, o! T? g? o! N' M? X? w! V. w? o' k. W. y, k; o' m! r; i, n. k, w; U? S? t; O' g' z. V. N? z, W? j! m? W! h; t! V' T! Z? R' w, w? y? y; O' w; r? q. G, V. x? n, Y; Q. s? S. G. f, s! U? l. o! i. L; Z' X! u. y, Q. q; Q, D; V. m. q. s? Y, U; p? u! q? h? O. W' y? Z! x! r. E, R, r' X' V, b. z, x! Q; y, g' j; j. q; W; v' X! J' H? i' o? n, Y. X! x? h? u; T? l! o? z. K' z' s; L? p? V' r. L? Y; V! V' S. t? Z' T' Y. s? i? Y! G? r; Y; T! h! K; M. k. U; A! V? R? C' x! X. M; z' V! w. N. T? Y' w? n, Z, Z? Y' R; V' f; V' I; t? X? Z; l? R, Q! Z. R. R, O. S! w; p' T. u? U! n, V, M. p? Q, O? q' t. B, k. u. H' T; T? S; Y! S! i? q! K' z' S! v; L. x; q; W? m? y, Z! x. y. j? N' R' I? r? V! Z; s, O? s; V, I, e? U' w! T? T! u; U! e? w? z; t! C! z? U, p' p! r. x; U! Z; u! j; T! X! N' F? n! P' t, X. s; q'"
# banned = ["m","i","s","w","y","d","q","l","a","p","n","t","u","b","o","e","f","g","c","x"]

#paragraph = "a, a, a, a, b,b,b,c, c"
#banned = ["a"]
#paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#banned = ["hit"]

paragraph = "Bob. hIt, baLl"
banned = ["bob","hit"]
sol = Solution()
print(sol.mostCommonWord(paragraph, banned))