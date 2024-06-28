class Solution:
    def fib(self, n: int) -> int:
        if n < 2: #前兩個數字是已知的，直接返回 n
            return n
        
        a, b = 0, 1
        for i in range(2, n + 1): 
        # 在 Fibonacci 數列中，前兩個數字是已知的：F(0) = 0 和 F(1) = 1。因此從2開始迭代
            a, b = b, a + b
            # print('a: ', a, 'b: ', b)
        return b

calculate_fib = Solution()
print(calculate_fib.fib(30))

# 時間複雜度: O(n) --> 這個算法的主要部分是一個從 2 到 n 的迭代循環。在每次迭代中，進行的是常數時間操作（更新兩個變數）。因此，迭代的總次數是 n - 1（因為迭代從 2 到 n）。
# 空間複雜度: O(1) --> 空間複雜度是算法運行時所需的空間隨輸入大小的變化情況。這個算法只使用了固定數量的額外變數（a, b, 和 i）。