from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1

        left_max = height[left_idx]
        right_max = height[right_idx]

        volume = 0

        while left_idx < right_idx:
            if height[left_idx] > left_max:
                left_max = height[left_idx]

            if height[right_idx] > right_max:
                right_max = height[right_idx]

            if left_max <= right_max:
                volume += left_max - height[left_idx]
                left_idx += 1
            else:
                volume += right_max - height[right_idx]
                right_idx -= 1

        return volume


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
