from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(nums)):
            if target - nums[i] in memo:
                return [memo[target - nums[i]], i]
            memo[nums[i]] = i

        return []


s = Solution()
print(s.twoSum([3, 2, 4], target=6))
print(s.twoSum([3, 3], target=6))
