'''
598. Range Addition II

You are given an m x n matrix M initialized with all 0's and an array of operations ops, 
where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.
'''

class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min_x, min_y = m, n
        count = 1
        # for a, b in ops:
        #     print('第', count, '次')
        #     print('a: ', a, 'b: ', b) # a 代表每個 list of list 中的第 0 位置，b 則是第 1 位置 
        #     min_x = min(min_x, a)
        #     min_y = min(min_y, b)
        #     print('min_x: ', min_x, 'min_y: ', min_y)
        #     print('min_x * min_y: ', min_x * min_y)
        #     count += 1
        # return min_x * min_y

        for a, b in ops:
            print('第', count, '次')
            print('a: ', a, 'b: ', b) # a 代表每個 list of list 中的第 0 位置，b 則是第 1 位置 
            if a <= min_x:
                min_x = a
            if b <= min_y:
                min_y = b
            print('min_x: ', min_x, 'min_y: ', min_y)
            print('min_x * min_y: ', min_x * min_y)
            count += 1
        return min_x * min_y

        
calculate_range = Solution()
calculate_range.maxCount(3, 3, [[2,2],[3,3],[3,3]]) 
# 思路: 找"什麼範圍會被每一次的操作覆蓋?" --> 所有操作矩陣的重合
# 以此例子來說，以原始 input (m, n) 做為比較基準
# 各矩陣的 column & row 分別都要以 2, 3, 3 去和基準比較，再回存最小值 (min_x & min_y)
# 因此 min_x & min_y 最小值皆為 2
# min_x * min_y 即為每次操作會被覆蓋的範圍 = 最大整數出現的次數


# calculate_range.maxCount(3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,2]])

# 時間複雜度: O(n), 空間複雜度: O(1)