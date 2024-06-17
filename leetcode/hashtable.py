class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]
        # return []

        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable: #找到
                return hashtable[target-num], i 
                # hashtable[21-19] = hashtable[2] ; i = 4。
                # 即 return 第一個數的 index (已在hashtable中) & 現在找到的 index
            hashtable[nums[i]] = i #沒找到就把數字 & 其 index 放進 hashtable 中
            print('hashtable: ', hashtable)
        return []
    
# 定義 nums 和 target
nums = [2, 7, 11, 15, 19]
target = 21

# 創建 Solution 對象
solution = Solution()

# 調用 twoSum 方法並打印結果
result = solution.twoSum(nums, target)

print('已找到! 此兩數的 index 為: ', result)