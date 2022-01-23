class Solution:
    def reverse(self, x: int) -> int:
        # len_int = len(str(x))
        # new_num = 0
        # ctr = 0
        # while len_int:
        #     div,mod = divmod(x,10**(len_int-1))
        #     print(div,mod)
        #     len_int -= 1
        #     x = mod
        #     new_num += div*(10**ctr)
        #     ctr+=1
        result = 0

        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        while x:
            result = result * 10 + x % 10
            x //= 10

        return 0 if result > pow(2, 31) else result * symbol
        # print("check")
        # print(ans)        
        
class Solution1:
    def __init__(self):        
        # handle 32 bit overflow  
        self.mina = -2**31  
        self.maxa = 2**31 - 1  
    def reverse(self, x: int) -> int:  
        if x > 0:  # handle positive numbers  
            a =  int(str(x)[::-1])  
        if x <=0:  # handle negative numbers  
            a = -1 * int(str(x*-1)[::-1])  
        if a not in range(self.mina, self.maxa):  
            return 0  
        else:  
            return a
        
print("Chekc")
print(Solution().reverse(123))