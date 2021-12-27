# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:25:42 2021

@author: SwarnaRavali
"""

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n//2+n%2):
            for j in range(n//2):
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = temp
                
Sol = Solution()
mt = [[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]]
Sol.rotate(mt)
